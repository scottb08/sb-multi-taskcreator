"""
Copyright (c) 2023, Scott Ballard - Quantum Images Inc.

Your use of this software as distributed in this GitHub repository, is governed by the MIT License

Your use of the Shotgun Pipeline Toolkit is governed by the applicable
license agreement between you and Autodesk / Shotgun.

Read LICENSE and SHOTGUN_LICENSE for full details about the licenses that pertain to this software.
"""

import sgtk
from .ui.task_entity_widget import Ui_Form
from sgtk.platform.qt import QtCore, QtGui

from .create_entity_dialog import CreateEntityDialog
from .utils import get_custom_entity_display_name

logger = sgtk.platform.get_logger(__name__)


class TaskEntityWidget(QtGui.QWidget):
    entity_dict_signal = QtCore.Signal(dict)

    def __init__(self, task_entity_data, parent_entity, dialog, app, parent):
        """

        :param task_entity_data: dict
        :param parent_entity: object
        :param dialog: QDialog
        :param app: object
        :param parent: object
        """
        super(TaskEntityWidget, self).__init__(parent=parent)
        self._parent_entity = None
        self.entity_query_filter = []
        self.create_entity_button = None

        # child_entity = task_entity_data.get('child_entity')
        self.parent_entity = parent_entity
        self.task_entity_data = task_entity_data
        self.entity_creation_data = task_entity_data.get('entity_creation', None)
        self.entity_type = task_entity_data['type']
        self.use_completer = task_entity_data['use_completer'] if 'use_completer' in task_entity_data else None
        self.entity_link_field = task_entity_data['entity_link_field'] if 'entity_link_field' \
                                                                          in task_entity_data else None
        self.override_name = task_entity_data['override_name'] if 'override_name' \
                                                                  in task_entity_data else None
        self.display_field = task_entity_data['display_field']
        self.fields = task_entity_data['fields']
        self.query_filter = task_entity_data['filters']
        self.order = task_entity_data['order']
        self.limit = task_entity_data['limit']

        self.dialog = dialog
        self.app = app
        self.sg = self.app.shotgun
        self.context = self.app.context

        # now load in the UI that was created in the UI designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Create autocompleter combobox
        self.entityComboBox = QtGui.QComboBox()
        self.ui.horizontalLayout.addWidget(self.combobox)

        # Add create entity button
        if self.entity_type not in ['Step'] and self.entity_creation_data:
            self.create_entity_button = QtGui.QPushButton('+', self)
            self.create_entity_button.setEnabled(False)
            self.create_entity_button.setMaximumSize(QtCore.QSize(35, 16777215))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setWeight(75)
            font.setBold(True)
            self.create_entity_button.setFont(font)
            self.ui.horizontalLayout.addWidget(self.create_entity_button)
            self.create_entity_button.released.connect(self.create_entity)

        # Get entity display name for custom entities
        self.display_name = get_custom_entity_display_name(self.entity_type)
        if self.override_name:
            self.display_name = self.override_name
        self.ui.entityNameLabel.setText(f'{self.display_name}:')

        self.combobox.currentIndexChanged.connect(self.emit_entity_selection_change)
        self.combobox.currentIndexChanged.connect(self.save_selection)

    def create_entity(self):
        selected_entities = self.dialog.get_user_selected_entities()

        dialog = CreateEntityDialog(task_entity_data=self.task_entity_data, selected_entities=selected_entities,
                                    app=self.app, parent=self.parent())
        dialog.entity_created.connect(self.update_entity_combobox)
        dialog.open()

    @property
    def parent_entity(self):
        return self._parent_entity

    @parent_entity.setter
    def parent_entity(self, value):
        self._parent_entity = value

    @property
    def combobox(self):
        return self.entityComboBox

    @property
    def entity_dict(self):
        if self.blocked():
            return None

        return self.combobox.itemData(self.combobox.currentIndex())

    def emit_entity_selection_change(self):
        self.entity_dict_signal.emit(self.entity_dict)

    def blocked(self):
        """
        Blocked when more than one item in combobox and set to index 0 (Select <entity type>)
        :return: bool
        """
        if self.combobox.count() > 1 and self.combobox.currentIndex() == 0 \
                or 'Select ' in self.combobox.currentText():
            return True

        return False

    def save_selection(self):
        if not self.blocked():
            self.dialog.settings.setValue(f'{self.entity_type}_combobox', self.combobox.currentText())

    @QtCore.Slot(dict)
    def update_query_filter(self, entity):
        """
        Update the ShotGrid query to filter by the given entity and the defined entity field
        :param entity: dict
        :return:
        """
        # Special query case for Step
        if entity and self.entity_type in ['Step']:
            self.entity_query_filter = [['entity_type', 'is', entity['type']]]
        else:
            self.entity_query_filter = [[self.entity_link_field, 'is', entity]]

        self.update_entity_combobox()

    def update_entity_combobox(self):
        self.combobox.clear()

        if self.parent_entity and not self.parent_entity.entity_dict:
            self.combobox.activated.emit(self.combobox.currentIndex())
            return

        # Don't include project in Step or CustomNonProjectEntity
        if self.entity_type not in ['Step'] and 'NonProject' not in self.entity_type:
            filters = [['project', 'is', self.context.project]]
        else:
            filters = []
        filters.extend(self.query_filter)
        filters.extend(self.entity_query_filter)

        fields = self.fields
        results = self.sg.find(self.entity_type, filters, fields, self.order, limit=self.limit)

        # Add Block item
        if len(results) > 1:
            self.combobox.addItem(QtGui.QIcon(':/res/block.png'), f'Select {self.display_name}')

        for result in results:
            self.combobox.addItem(result[self.display_field], result)

        self.combobox.activated.emit(self.combobox.currentIndex())

        if self.create_entity_button:
            self.create_entity_button.setEnabled(True)
            self.create_entity_button.setStyleSheet('color: rgb(30, 167, 224);')

        self.restore_user_selection()

    def restore_user_selection(self):
        """
        Restore the previous selection made by the user
        :return: None
        """

        # Restore previous selection
        text = self.dialog.settings.value(f'{self.entity_type}_combobox', None)
        if text:
            index = self.combobox.findText(text, QtCore.Qt.MatchCaseSensitive)
            if index > 0:
                self.combobox.setCurrentIndex(index)
