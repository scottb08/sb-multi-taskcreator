"""
Copyright (c) 2023, Scott Ballard - Quantum Images Inc.

Your use of this software as distributed in this GitHub repository, is governed by the MIT License

Your use of the Shotgun Pipeline Toolkit is governed by the applicable
license agreement between you and Autodesk / Shotgun.

Read LICENSE and SHOTGUN_LICENSE for full details about the licenses that pertain to this software.
"""

import sgtk
from .ui.create_entity_dialog import Ui_Dialog
from sgtk.platform.qt import QtCore, QtGui
from .utils import get_custom_entity_display_name

logger = sgtk.platform.get_logger(__name__)


class CreateEntityDialog(QtGui.QDialog):
    entity_created = QtCore.Signal()

    def __init__(self, task_entity_data, selected_entities, app, parent):
        """

        :param parent: object
        """
        super(CreateEntityDialog, self).__init__(parent=parent)

        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.creationLabel.setVisible(False)
        self.ui.entityUrlLabel.setVisible(False)

        # self.setModal(True)

        self.entity_schema = None
        self.widget_grps = []
        self.entity_type = task_entity_data['type']
        self.override_name = task_entity_data['override_name'] if 'override_name' \
                                                                  in task_entity_data else None
        self.entity_creation_data = task_entity_data.get('entity_creation', None)
        if not self.entity_creation_data:
            raise ValueError('Unable to find entity_creation data in config YML file.')

        # Update selected entities to include entity_type "type" for when creating the dialog when there
        # aren't any existing entities
        self.selected_entities = selected_entities
        if self.entity_type not in self.selected_entities:
            self.selected_entities.update({self.entity_type: {'type': self.entity_type}})

        self.app = app
        self.sg = app.shotgun
        self.context = app.context

        # Get entity display name for custom entities
        self.display_name = get_custom_entity_display_name(self.entity_type)
        if self.override_name:
            self.display_name = self.override_name

        title = f'Create a New {self.display_name}'
        self.setWindowTitle(title)
        self.ui.dialogTitle.setText(title)
        self.ui.createEntityButton.setText(f'Create {self.display_name}')

        self.build_ui_field_widgets()

        # Signals
        self.ui.createEntityButton.released.connect(self.create_shotgrid_entity)

    def build_ui_field_widgets(self):
        """

        :return:
        """
        if 'fields' not in self.entity_creation_data:
            raise ValueError('Fields definition missing from entity_creation data in config.')

        fields = self.entity_creation_data['fields']
        entity_schema = self.get_sg_schema()

        for field, data in fields.items():
            hook = data.get('hook', None)
            hook_data = data.get('hook', None)
            if not hook:
                logger.warning(f'Hook not defined for field "{field}", skipping...')
                continue

            widget = self.app.execute_hook_expression(hook, 'create_widget', base_class=None,
                                                      entity_type=self.entity_type, field_name=field,
                                                      hook_data=hook_data,
                                                      data=data, app=self.app, entity_schema=entity_schema,
                                                      selected_entities=self.selected_entities,
                                                      parent_widget=self.parent())

            # Add widget to layout
            if not widget.valid:
                del widget

            else:
                widget.field_widget_changed.connect(self.update_create_button)
                self.ui.fieldsVerticalLayout.addWidget(widget)
                self.widget_grps.append(widget)

    def get_sg_schema(self):
        return self.sg.schema_field_read(entity_type=self.entity_type, project_entity=self.context.project)

    def update_ui_field_values(self, field_values_dict):
        """
        From the given dict update the UI field_widgets with the corresponding values
        :param field_values_dict:
        :return: None
        """

        for field_name, field_value in field_values_dict.items():
            for widget_grp in self.widget_grps:
                if field_name == widget_grp.field_name:
                    if isinstance(widget_grp.field_widget, QtGui.QLineEdit):
                        widget_grp.field_widget.setText(field_value)

    def update_create_button(self):
        self.ui.createEntityButton.setEnabled(False)
        for widget_grp in self.widget_grps:
            if not widget_grp.field_valid:
                return

        self.ui.createEntityButton.setEnabled(True)

    def create_shotgrid_entity(self):
        data = {
            'project': self.context.project,
        }

        for widget in self.widget_grps:
            data[widget.field_name] = widget.widget_field_data()

        entity = self.sg.create(self.entity_type, data)

        # Display ShotGrid Entity link
        display_name = get_custom_entity_display_name(entity['type'])

        self.ui.creationLabel.setVisible(True)
        self.ui.entityUrlLabel.setVisible(True)
        entity_url = f'{self.sg.base_url}/detail/{entity["type"]}/{entity["id"]}'
        self.ui.creationLabel.setText(f'Last {display_name} "{entity["code"]}" Created:')
        self.ui.entityUrlLabel.setText(f'<a style="color:#4383a8" href=\"{entity_url}\"> ShotGrid Entity Link</a>')

        # Update calling UI entity combobox with new entity
        self.entity_created.emit()
