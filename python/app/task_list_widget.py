"""
Copyright (c) 2023, Scott Ballard - Quantum Images Inc.

Your use of this software as distributed in this GitHub repository, is governed by the MIT License

Your use of the Shotgun Pipeline Toolkit is governed by the applicable
license agreement between you and Autodesk / Shotgun.

Read LICENSE and SHOTGUN_LICENSE for full details about the licenses that pertain to this software.
"""

import sgtk

from .ui.task_list_widget import Ui_Form
from .task_token_base_widget import TaskTokenBaseWidget
from sgtk.platform.qt import QtCore, QtGui

logger = sgtk.platform.get_logger(__name__)


class TaskListComboBoxWidget(TaskTokenBaseWidget):
    def __init__(self, definition, parent):
        super(TaskListComboBoxWidget, self).__init__(form=Ui_Form, definition=definition, parent=parent)

        self.ui.comboBox.addItem(QtGui.QIcon(':/res/block.png'), f'Select {self.name}')

        if 'items' not in definition:
            raise ValueError('"items" definition missing from List widget definition, please check the configuration.')

        self.ui.comboBox.addItems(definition['items'])

    def text(self):
        if self.token_widget().currentIndex() == 0:
            return None

        return self.token_widget().currentText()

    def token_widget(self):
        return self.ui.comboBox
