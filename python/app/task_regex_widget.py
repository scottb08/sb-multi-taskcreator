"""
Copyright (c) 2023, Scott Ballard - Quantum Images Inc.

Your use of this software as distributed in this GitHub repository, is governed by the MIT License

Your use of the Shotgun Pipeline Toolkit is governed by the applicable
license agreement between you and Autodesk / Shotgun.

Read LICENSE and SHOTGUN_LICENSE for full details about the licenses that pertain to this software.
"""

import sgtk

from .ui.task_regex_widget import Ui_Form
from .task_token_base_widget import TaskTokenBaseWidget
from sgtk.platform.qt import QtCore, QtGui

logger = sgtk.platform.get_logger(__name__)


class TaskRegexLineEditWidget(TaskTokenBaseWidget):
    def __init__(self, definition, parent):
        super(TaskRegexLineEditWidget, self).__init__(form=Ui_Form, definition=definition, parent=parent)

        if 'regex' not in definition:
            raise ValueError('"regex" key missing from Regex widget definition, please check configuration.')

        regex_widget = QtGui.QRegExpValidator(QtCore.QRegExp(definition['regex']))
        self.ui.lineEdit.setValidator(regex_widget)

    def text(self):
        return self.token_widget().text()

    def token_widget(self):
        return self.ui.lineEdit
