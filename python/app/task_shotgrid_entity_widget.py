"""
Copyright (c) 2023, Scott Ballard - Quantum Images Inc.

Your use of this software as distributed in this GitHub repository, is governed by the MIT License

Your use of the Shotgun Pipeline Toolkit is governed by the applicable
license agreement between you and Autodesk / Shotgun.

Read LICENSE and SHOTGUN_LICENSE for full details about the licenses that pertain to this software.
"""

import sgtk

from .ui.task_shotgrid_entity_widget import Ui_Form
from .task_token_base_widget import TaskTokenBaseWidget
from sgtk.platform.qt import QtCore, QtGui

logger = sgtk.platform.get_logger(__name__)


class TaskShotgridEntityComboBoxWidget(TaskTokenBaseWidget):
    def __init__(self, definition, app, parent):
        super(TaskShotgridEntityComboBoxWidget, self).__init__(form=Ui_Form, definition=definition, parent=parent)

        entity_type = definition['entity_type']
        entity_filter = definition['filters']
        display_field = definition['display_field']
        fields = definition['fields']
        order = definition['order']

        self.token_widget().addItem(QtGui.QIcon(':/res/block.png'), f'Select {self.name}')

        filters = []

        # Special use to allow project to be injected into yml definition (as a str & converted to list)
        # ex: filters: "[['project', 'is', {project}]]"  >> [['project', 'is', {'type': 'Project', 'id': 123}]]
        entity_filter = str(entity_filter)  # convert unicode to str (Maya 2018)
        if isinstance(entity_filter, str):
            entity_filter = eval(entity_filter.format(project=app.context.project))

        filters.extend(entity_filter)

        results = app.shotgun.find(entity_type, filters, fields, order)

        if results:
            for result in results:
                self.token_widget().addItem(result[display_field], result)

    def text(self):
        if self.token_widget().currentIndex() == 0:
            return None

        return self.token_widget().currentText()

    def token_widget(self):
        return self.ui.comboBox

