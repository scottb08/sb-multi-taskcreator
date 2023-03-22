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


class ShortcodeFieldWidgetHook(HookClass):
    """
    Hook called when a file needs to be copied
    """

    def create_widget(self, **kwargs):
        widget = ShortCodeFieldWidget(entity_type=kwargs['entity_type'], field_name=kwargs['field_name'],
                                      hook_data=kwargs['hook_data'],
                                      yml_data=kwargs['data'], app=kwargs['app'],
                                      entity_schema=kwargs['entity_schema'],
                                      selected_entities=kwargs['selected_entities'],
                                      parent=kwargs['parent_widget'])
        return widget


class ShortCodeFieldWidget(QtGui.QWidget):
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
        super(ShortCodeFieldWidget, self).__init__(parent=parent)

        self._field_widget = None
        self.entity_type = entity_type
        self._field_name = field_name
        self.hook_data = hook_data
        self._yml_data = yml_data
        self.app = app
        self.entity_schema = entity_schema
        self.selected_entities = selected_entities
        self._parent_widget = parent
        self.valid = True
        self._required = False

        self.label = None

        self.layout = QtGui.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        if self.field_name not in self.entity_schema:
            logger.warning(f'Unable to find field "{self.field_name}" in "{self.entity_type}"'
                           ' entity schema, skipping field...')
            self.valid = False

        field_data_type = self.entity_schema[self.field_name]['data_type']['value']
        display_name = self.entity_schema[self.field_name]['name']['value']
        description = self.entity_schema[self.field_name]['description']['value']
        self.required = self.yml_data.get('required', False)
        self.callback = self.yml_data.get('callback', None)
        self.hook_data = self.yml_data.get('hook_data', None)

        self.label = QtGui.QLabel(f'{display_name}:', parent=self.parent_widget)
        self.layout.addWidget(self.label)

        if self.required:
            font = QtGui.QFont()
            font.setBold(True)
            self.label.setFont(font)

        if field_data_type == 'text':
            self.input_widget = QtGui.QLineEdit(self.parent_widget)
            self.field_widget = QtGui.QLineEdit(self.parent_widget)
            self.field_widget.setReadOnly(True)

            # Valid widget
            self.valid_widget = QtGui.QLabel('')

            # Add to layout
            self.layout.addWidget(self.input_widget)
            self.layout.addWidget(self.field_widget)
            self.layout.addWidget(self.valid_widget)

            # Set Regex validator if defined in config
            regex_input_mask = self.hook_data.get('regex_input_mask', None)
            if regex_input_mask:
                regex = QtCore.QRegExp(regex_input_mask)
                regex_val = QtGui.QRegExpValidator(regex)
                self.input_widget.setValidator(regex_val)

            if description:
                self.field_widget.setToolTip(description)

            self.input_widget.textChanged.connect(self.update_field_widget)

        else:
            logger.warning(f'Unsupported ShotGrid field type "{field_data_type}", will not show in dialog.')
            self.valid = False

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
        if not self.valid or self.required and not self.widget_field_data():
            return False

        return True

    # Methods
    def update_field_widget(self):
        """
        Using the user selected entities in the main UI and the user input populate the shortcode_format
        definition defined in the hook
        :return: None
        """
        self.selected_entities['user_input'] = self.input_widget.text()

        shortcode_format = self.hook_data.get('shortcode_format', None)

        if not shortcode_format:
            shortcode_format = '{user_input}'

        shortcode = shortcode_format.format(**self.selected_entities)
        self.field_widget.setText(shortcode)

        self.validate_short_code(shortcode)

    def validate_short_code(self, shortcode):
        filters = [
            ['project', 'is', self.context.project],
            [self.field_name, 'is', shortcode],
        ]
        fields = ['code']
        result = self.shotgun.find_one(self.entity_type, filters, fields)

        if result:
            self.valid = False
            self.valid_widget.setText(' DUPLICATE ')
            self.valid_widget.setStyleSheet('background-color: rgb(255, 0, 0);\ncolor: rgb(0, 0, 0);')
        else:
            self.valid = True
            self.valid_widget.setText(' VALID ')
            self.valid_widget.setStyleSheet('background-color: rgb(0, 255, 0);\ncolor: rgb(0, 0, 0);')

        self.field_widget_changed.emit()

    def widget_field_data(self):
        if isinstance(self.field_widget, QtGui.QLineEdit):
            return self.field_widget.text()

        else:
            raise NotImplementedError(f'Widget user input return type not implemented for: {type(self.field_widget)}')




