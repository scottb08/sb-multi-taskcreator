"""
Copyright (c) 2023, Scott Ballard - Quantum Images Inc.

Your use of this software as distributed in this GitHub repository, is governed by the MIT License

Your use of the Shotgun Pipeline Toolkit is governed by the applicable
license agreement between you and Autodesk / Shotgun.

Read LICENSE and SHOTGUN_LICENSE for full details about the licenses that pertain to this software.
"""

import sgtk
from pprint import pprint, pformat
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog

from .task_entity_widget import TaskEntityWidget
from .task_list_widget import TaskListComboBoxWidget
from .task_regex_widget import TaskRegexLineEditWidget
from .task_shotgrid_entity_widget import TaskShotgridEntityComboBoxWidget
from .utils import get_custom_entity_display_name

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)

overlay_widget = sgtk.platform.import_framework("tk-framework-qtwidgets", "overlay_widget")


def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system.

    # we pass the dialog class to this method and leave the actual construction to be carried out by toolkit.
    app_instance.engine.show_dialog(app_instance.get_setting("display_name"), app_instance, AppDialog)


class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """

    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)

        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.previousTaskLabel.setVisible(False)
        self.ui.taskUrlLabel.setVisible(False)
        self.ui.entityUrlLabel.setVisible(False)
        self._overlay_widget = overlay_widget.ShotgunOverlayWidget(self)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()
        self.engine = self._app.engine
        self.sg = self._app.shotgun
        self.context = self.engine.context

        # Setup app settings
        sg_project = self.context.project['name']
        self.settings = QtCore.QSettings(f'Shotgun\\Toolkit\\{sg_project}', self._app.instance_name)

        # logging happens via a standard toolkit logger
        logger.info(self._app.get_setting('display_name'))
        self._app.logger.info(f'App version: {self._app.version}')

        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - An Sgtk API instance, via self._app.sgtk

        self.task_templates = self._app.get_setting('task_templates')
        self.task_name_delineator = self._app.get_setting('task_name_delineator')
        self.entity_widget = None
        self.step_widget = None
        self.task_context_widgets = []
        self.task_name_widgets = []
        self.task_name_valid = False

        self.build_task_template_menu()

        # Disable context switching in non-DCCs or engines that don't support context switching (doesn't make sense)
        if not self.engine.context_change_allowed or \
                self.engine.instance_name in ['tk-shell', 'tk-desktop', 'tk-shotgun']:
            self.ui.switchTaskContextCheckBox.setEnabled(False)

        self.restore_preferences()

        # Signals
        self.ui.taskTemplateComboBox.currentIndexChanged.connect(self.template_init)
        self.ui.createTaskButton.released.connect(self.create_task)
        self.ui.taskTemplateComboBox.currentIndexChanged.connect(self.save_preferences)
        self.ui.assignTaskCheckBox.stateChanged.connect(self.save_preferences)
        self.ui.switchTaskContextCheckBox.stateChanged.connect(self.save_preferences)
        self.ui.close_checkBox.stateChanged.connect(self.save_preferences)

        # Restore previous template selection
        task_creation_template = self.settings.value('taskCreationTemplate', None)
        if task_creation_template:
            index = self.ui.taskTemplateComboBox.findText(task_creation_template, QtCore.Qt.MatchCaseSensitive)
            self.ui.taskTemplateComboBox.setCurrentIndex(index)

    def build_task_template_menu(self):
        # Add Block item
        self.ui.taskTemplateComboBox.addItem(QtGui.QIcon(':/res/block.png'),
                                             'Select Task Template')

        for task_template in self.task_templates:
            self.ui.taskTemplateComboBox.addItem(task_template['template_name'], task_template)

    def template_init(self):
        """
        Build UI widgets for user selected Task Template
        :return: None
        """
        self.clear_ui()

        if self.ui.taskTemplateComboBox.currentIndex() == 0:
            return

        data = self.ui.taskTemplateComboBox.itemData(self.ui.taskTemplateComboBox.currentIndex())
        if not data or 'task_entity' not in data:
            return

        task_entity = data['task_entity']
        task_name_definitions = data['task_name_definitions']

        self.build_task_creation_context_widgets(task_entity, parent_entity=None)

        if self.task_context_widgets:
            self.task_context_widgets[0].update_entity_combobox()

        if task_name_definitions:
            self.build_task_name_definition_widgets(task_name_definitions)

    def build_task_creation_context_widgets(self, task_entity_data, parent_entity=None):
        child_entity = task_entity_data.get('child_entity')

        widget = TaskEntityWidget(task_entity_data, parent_entity=parent_entity,
                                  dialog=self, app=self._app, parent=self)
        widget.entityComboBox.currentIndexChanged.connect(self.validate_task_name)

        # Define Step widget
        if widget.entity_type in ['Step']:
            self.step_widget = widget
            self.entity_widget = parent_entity

        if parent_entity:
            parent_entity.entity_dict_signal.connect(widget.update_query_filter)

        self.task_context_widgets.append(widget)
        self.ui.taskEntitiesLayout.addWidget(widget)

        if child_entity:
            widget = self.build_task_creation_context_widgets(child_entity, parent_entity=widget)

        return widget

    def build_task_name_definition_widgets(self, task_name_definitions):
        for task_name_definition in task_name_definitions:

            if 'widget' not in task_name_definition:
                raise ValueError('widget key name missing from "task_name_definitions" definition. '
                                 'Please check configuration')

            widget_type = task_name_definition['widget']

            # List Widget
            if widget_type == 'list':
                widget = TaskListComboBoxWidget(definition=task_name_definition, parent=self)
                self.task_name_widgets.append(widget)
                self.ui.taskDefinitionLayout.addWidget(widget)
                widget.ui.comboBox.currentIndexChanged.connect(self.assemble_task_name)

            # List Widget
            elif widget_type == 'entity':
                widget = TaskShotgridEntityComboBoxWidget(definition=task_name_definition, app=self._app, parent=self)
                self.task_name_widgets.append(widget)
                self.ui.taskDefinitionLayout.addWidget(widget)
                widget.ui.comboBox.currentIndexChanged.connect(self.assemble_task_name)

            # Regex Widget
            elif widget_type == 'regex':
                widget = TaskRegexLineEditWidget(definition=task_name_definition, parent=self)
                self.task_name_widgets.append(widget)
                self.ui.taskDefinitionLayout.addWidget(widget)
                widget.ui.lineEdit.editingFinished.connect(self.assemble_task_name)

            else:
                raise ValueError(f'Unknown Task Name Definition Widget: {widget_type}')

    def get_user_selected_entities(self):
        """
        Get the user selected entities from the parent UI drop-down menus + current project
        :return: dict
        """
        selected_context_data = {'Project': self.context.project}

        for widget in self.task_context_widgets:
            if widget.entity_type and widget.entity_dict:
                selected_context_data[widget.entity_type] = widget.entity_dict

        return selected_context_data

    def clear_ui(self):
        """
        Clear the widgets under the Task Creation Context and Task Name Definition layouts
        :return:
        """
        self.task_context_widgets = []
        self.task_name_widgets = []
        self.ui.taskNameLabel.setText('')
        self.ui.validInvalidLabel.setText('')
        self.ui.validInvalidLabel.setStyleSheet('')

        layouts = [self.ui.taskEntitiesLayout, self.ui.taskDefinitionLayout]

        for layout in layouts:
            while layout.count() != 0:
                child = layout.takeAt(0)
                widget = child.widget()
                widget.setParent(None)
                del widget

    def assemble_task_name(self):
        """
        Assemble all the Task Widgets values selected by user into complete task name
        :return: None
        """
        self.ui.taskNameLabel.setText('')
        self.validate_task_name()

        if not self.task_name_widgets:
            return

        task_name = ''

        for widget in self.task_name_widgets:
            if not widget.valid():
                return

            if widget.text():
                task_name += widget.get_task_name(task_name, self.task_name_delineator)

        self.ui.taskNameLabel.setText(task_name)

        self.validate_task_name()

    def validate_task_name(self):
        """
        Check the proposed Task name against Tasks in Shotgun to ensure its unique (if set in config)
        :return:
        """

        task_name = self.ui.taskNameLabel.text()
        entity_dict = self.entity_widget.entity_dict
        step_entity = self.step_widget.entity_dict

        if not task_name or not entity_dict or not step_entity:
            self.ui.validInvalidLabel.setStyleSheet('')
            self.ui.validInvalidLabel.setText('')
            self.ui.createTaskButton.setEnabled(False)
            return

        filters = [
            ['project', 'is', self.engine.context.project],
            ['content', 'is', task_name],
            ['entity', 'is', entity_dict],
            ['step', 'is', step_entity],
        ]
        fields = ['content']
        results = self.sg.find_one('Task', filters, fields)

        if results:
            self.ui.validInvalidLabel.setStyleSheet('background-color: rgb(255, 0, 0);\ncolor: rgb(255, 255, 255);')
            self.ui.validInvalidLabel.setText('   D U P L I C A T E   ')
            self.task_name_valid = False

        else:
            self.ui.validInvalidLabel.setStyleSheet('background-color: rgb(0, 255, 0);\ncolor: rgb(0, 0, 0);')
            self.ui.validInvalidLabel.setText('   V A L I D   ')
            self.task_name_valid = True

        self.enable_create_task_button()

    def enable_create_task_button(self):
        self.ui.createTaskButton.setEnabled(False)

        if not self.task_name_valid:
            return

        for widget in self.task_context_widgets:
            if widget.blocked():
                return

        if self.step_widget.blocked():
            return

        self.ui.createTaskButton.setEnabled(True)

    def validate_task_template_structure(self):
        pass

    def create_task(self):
        """
        Create Task in Shotgun from user selected Task name and context
        :return:
        """
        entity = self.entity_widget.entity_dict
        task_name = self.ui.taskNameLabel.text()
        step = self.step_widget.combobox.itemData(self.step_widget.combobox.currentIndex())

        data = {
            'project': self.context.project,
            'content': task_name,
            'entity': entity,
            'step': step,
        }

        if self.ui.assignTaskCheckBox.isChecked():
            data['task_assignees'] = [self.context.user]

        try:
            # Create Task
            self._overlay_widget.show_message(
                '<h2 style="color:#4383a8">Creating Task, please wait...</h2>')
            QtGui.QApplication.instance().processEvents()
            task = self.sg.create('Task', data)
            logger.info(f'Task created: {pformat(task)}')

            # Display ShotGrid Task link
            display_name = get_custom_entity_display_name(entity['type'])

            self.ui.previousTaskLabel.setVisible(True)
            self.ui.taskUrlLabel.setVisible(True)
            self.ui.entityUrlLabel.setVisible(True)
            task_url = f'{self.sg.base_url}/detail/Task/{task["id"]}'
            entity_url = f'{self.sg.base_url}/detail/{entity["type"]}/{entity["id"]}'
            self.ui.previousTaskLabel.setText(f'Last Task "{task["content"]}" Created:')
            self.ui.taskUrlLabel.setText(f'<a style="color:#4383a8" href=\"{task_url}\">ShotGrid Task Link</a> ')
            self.ui.entityUrlLabel.setText(f'<a style="color:#4383a8" href=\"{entity_url}\">'
                                           f'ShotGrid {display_name} Link</a>')

            if self.ui.switchTaskContextCheckBox.isChecked() and self.ui.switchTaskContextCheckBox.isEnabled():
                self.switch_to_context(task)

            QtGui.QMessageBox.information(
                self,
                'Task Created',
                f'<h2 style="color:#4383a8">Task "{task["content"]}" created successfully.</h2>',
                QtGui.QMessageBox.Ok
            )

        except Exception as err:
            logger.error(f'Failed to create task: {err}')
            QtGui.QMessageBox.critical(
                self,
                'Error',
                f'<h2 style="color:#4383a8">Failed to create Task, please contact support\n{err}.</h2>',
                QtGui.QMessageBox.Ok
            )

        finally:
            self._overlay_widget.hide()
            self.validate_task_name()

            if self.ui.close_checkBox.isChecked():
                self.close()


    def save_preferences(self):
        self.settings.setValue('switchTaskContext', int(self.ui.switchTaskContextCheckBox.isChecked()))
        self.settings.setValue('assignTaskToMe', int(self.ui.assignTaskCheckBox.isChecked()))
        self.settings.setValue('closeDialog', int(self.ui.close_checkBox.isChecked()))

        if self.ui.taskTemplateComboBox.currentIndex() > 0:
            self.settings.setValue('taskCreationTemplate', self.ui.taskTemplateComboBox.currentText())

    def restore_preferences(self):
        switch_task_context = self.settings.value('switchTaskContext', True)
        self.ui.switchTaskContextCheckBox.setChecked(int(switch_task_context))

        assign_task = self.settings.value('assignTaskToMe', True)
        self.ui.assignTaskCheckBox.setChecked(int(assign_task))

        close_dialog = self.settings.value('closeDialog', True)
        self.ui.close_checkBox.setChecked(int(close_dialog))

    def switch_to_context(self, task):
        """
        Given the entity, generate a context and switch to it.
        :param task: dict
        :return: None
        """

        if self.engine.context_change_allowed:
            try:
                self._overlay_widget.show_message(
                    '<h2 style="color:#4383a8">Creating folder structure, please wait...</h2>')
                QtGui.QApplication.instance().processEvents()
                self._app.sgtk.create_filesystem_structure('Task', task['id'])

                self._overlay_widget.show_message(
                    '<h2 style="color:#4383a8">Switching context, please wait...</h2>')
                QtGui.QApplication.instance().processEvents()
                context = self._app.sgtk.context_from_entity('Task', task['id'])
                if context:
                    self.engine.change_context(context)

            except Exception as err:
                logger.error(f'Failed to create folder structure or switch context: {err}')
                raise err

