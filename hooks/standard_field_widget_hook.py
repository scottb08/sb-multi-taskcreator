"""
Copyright (c) 2023, Scott Ballard - Quantum Images Inc.

Your use of this software as distributed in this GitHub repository, is governed by the MIT License

Your use of the Shotgun Pipeline Toolkit is governed by the applicable
license agreement between you and Autodesk / Shotgun.

Read LICENSE and SHOTGUN_LICENSE for full details about the licenses that pertain to this software.
"""

import sgtk
from sgtk.platform.qt import QtCore, QtGui

HookClass = sgtk.get_hook_baseclass()

logger = sgtk.platform.get_logger(__name__)


class StandardFieldWidgetHook(HookClass):
    """
    Hook called when a file needs to be copied
    """

    def create_widget(self, **kwargs):
        widget = EntityFieldWidget(entity_type=kwargs['entity_type'], field_name=kwargs['field_name'],
                                   hook_data=kwargs['hook_data'],
                                   yml_data=kwargs['data'], app=kwargs['app'],
                                   entity_schema=kwargs['entity_schema'],
                                   selected_entities=kwargs['selected_entities'],
                                   parent=kwargs['parent_widget'])
        return widget


class EntityFieldWidget(QtGui.QWidget):
    field_widget_changed = QtCore.Signal()

    def __init__(self, entity_type, field_name, hook_data, yml_data, app, entity_schema, selected_entities, parent):
        """

        :param entity_type: str - ShotGrid entity type
        :param field_name: str - ShotGrid entity field name
        :param hook_data: dict - metadata the hook might need
        :param yml_data: dict - data from app config
        :param app: object - TK application
        :param entity_schema: dict - ShotGrid entity type database schema
        :param parent: object - QT parent widget
        """
        super(EntityFieldWidget, self).__init__(parent=parent)

        self._field_widget = None
        self.entity_type = entity_type
        self._field_name = field_name
        self.hook_data = hook_data
        self._yml_data = yml_data
        self.app = app
        self.entity_schema = entity_schema
        self.selected_entities = selected_entities
        self._parent_widget = parent
        self._valid = True
        self._required = False
        self.label = None

        # Get user selected entities from parent UI
        self.selected_entities = selected_entities

        # Create layout
        self.layout = QtGui.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        if self.field_name not in self.entity_schema:
            logger.warning(f'Unable to find field "{self.field_name}" '
                           f'in "{self.entity_type}" entity schema, skipping field...')
            self.valid = False

        field_data_type = self.entity_schema[self.field_name]['data_type']['value']
        display_name = self.entity_schema[self.field_name]['name']['value']
        description = self.entity_schema[self.field_name]['description']['value']
        editable = self.yml_data.get('editable', True)
        self.required = self.yml_data.get('required', False)
        self.callback = self.yml_data.get('callback', None)

        self.label = QtGui.QLabel(f'{display_name}:', parent=self.parent_widget)
        self.label.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.layout.addWidget(self.label)

        if self.required:
            font = QtGui.QFont()
            font.setBold(True)
            self.label.setFont(font)

        if field_data_type == 'text':
            self.field_widget = QtGui.QLineEdit(self.parent_widget)
            if not editable:
                self.field_widget.setReadOnly(not editable)
            self.field_widget.textChanged.connect(lambda: self.field_widget_changed.emit())

        elif field_data_type == 'list':
            schema_list_values = self.entity_schema[self.field_name]['properties']['valid_values']['value']
            self.field_widget = QtGui.QComboBox(self.parent_widget)
            for item in schema_list_values:
                self.field_widget.addItem(item, item)

            # Signal
            self.field_widget.currentIndexChanged.connect(lambda: self.field_widget_changed.emit())

        elif field_data_type == 'entity':
            link_entity_type = self.entity_schema[self.field_name]['properties']['valid_types']['value'][0]
            self.field_widget = QtGui.QComboBox(self.parent_widget)

            # Propagate combobox
            order = self.yml_data.get('order', [])
            display_field = self.yml_data.get('display_field', 'code')
            filters = self.yml_data.get('filters', [])

            # Expand filter definition if str
            if isinstance(filters, str):
                filters = eval(filters.format(**self.selected_entities))

            fields = ['code']
            results = self.shotgun.find(link_entity_type, filters, fields, order)

            if link_entity_type in ['TaskTemplate']:
                self.field_widget.addItem('', None)

            for result in results:
                self.field_widget.addItem(result[display_field], result)

            # Signal
            self.field_widget.currentIndexChanged.connect(lambda: self.field_widget_changed.emit())

        else:
            logger.warning(f'Unsupported ShotGrid field type "{field_data_type}", will not show in dialog.')
            self._valid = False

        if self.field_widget:
            self.layout.addWidget(self.field_widget)

            if description:
                self.field_widget.setToolTip(description)

    # Properties
    @property
    def field_widget(self):
        return self._field_widget

    @field_widget.setter
    def field_widget(self, value):
        self._field_widget = value

    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        if value in ['Step']:
            raise ValueError('Creating Steps in this app is not supported. Use the ShotGrid web interface.')

        self._entity_type = value

    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value

    @property
    def yml_data(self):
        return self._yml_data

    @property
    def shotgun(self):
        return self.app.shotgun

    @property
    def context(self):
        return self.app.context

    @property
    def parent_widget(self):
        return self._parent_widget

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value

    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value

    @property
    def field_valid(self):
        if self.required and not self.widget_field_data():
            return False

        return True

    # Methods
    def widget_field_data(self):
        if isinstance(self.field_widget, QtGui.QLineEdit):
            return self.field_widget.text()

        elif isinstance(self.field_widget, QtGui.QComboBox):
            data = self.field_widget.itemData(self.field_widget.currentIndex())
            return data

        else:
            raise NotImplementedError(f'Widget return type not implemented for: {type(self.field_widget)}')




