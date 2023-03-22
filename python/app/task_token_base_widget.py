"""
Copyright (c) 2023, Scott Ballard - Quantum Images Inc.

Your use of this software as distributed in this GitHub repository, is governed by the MIT License

Your use of the Shotgun Pipeline Toolkit is governed by the applicable
license agreement between you and Autodesk / Shotgun.

Read LICENSE and SHOTGUN_LICENSE for full details about the licenses that pertain to this software.
"""

import sgtk
from sgtk.platform.qt import QtCore, QtGui

logger = sgtk.platform.get_logger(__name__)


class TaskTokenBaseWidget(QtGui.QWidget):
    def __init__(self, form, definition, parent):
        super(TaskTokenBaseWidget, self).__init__(parent=parent)

        self._required = True

        # now load in the UI that was created in the UI designer
        self.ui = form()
        self.ui.setupUi(self)

        self.name = definition.get('name', 'Not Defined')
        self.delineator = definition.get('delineator', None)    # per widget delineator override

        # Task token required
        if 'required' in definition:
            self.required = definition['required']

        if not self.required:
            self.ui.label.setText(f'{self.name} (optional)')
        else:
            self.ui.label.setText(self.name)

        # tooltip
        if 'tooltip' in definition:
            self.token_widget().setToolTip(definition['tooltip'])

    def get_task_name(self, task_name, delineator):
        if not task_name:
            return self.text()
        else:
            delin = self.delineator if self.delineator is not None else delineator
            return f'{delin}{self.text()}'

    def text(self):
        pass

    def token_widget(self):
        pass

    def valid(self):
        if isinstance(self.token_widget(), QtGui.QComboBox):

            if not self.required and self.token_widget().currentIndex() == 0:
                return True

            elif self.token_widget().currentIndex() > 0:
                return True

            return False

        elif isinstance(self.token_widget(), QtGui.QLineEdit):
            if self.required and not self.text():
                return False

            return True

        else:
            raise ValueError(f'Unknown token widget type: {type(self.token_widget())}')

    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
