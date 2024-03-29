# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 386)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Dialog.setFont(font)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 8, 0, 1, 1)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("color: rgb(30, 167, 224);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.taskTemplateComboBox = QtGui.QComboBox(Dialog)
        self.taskTemplateComboBox.setObjectName("taskTemplateComboBox")
        self.horizontalLayout.addWidget(self.taskTemplateComboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.createTaskButton = QtGui.QPushButton(Dialog)
        self.createTaskButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.createTaskButton.setFont(font)
        self.createTaskButton.setStyleSheet("QPushButton:enabled  {\n"
"    color: rgb(30, 167, 224);\n"
"}")
        self.createTaskButton.setObjectName("createTaskButton")
        self.gridLayout_2.addWidget(self.createTaskButton, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 9, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setStyleSheet("QGroupBox  {\n"
"    color: rgb(30, 167, 224);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.assignTaskCheckBox = QtGui.QCheckBox(self.groupBox)
        self.assignTaskCheckBox.setChecked(True)
        self.assignTaskCheckBox.setObjectName("assignTaskCheckBox")
        self.gridLayout_3.addWidget(self.assignTaskCheckBox, 0, 0, 1, 1)
        self.switchTaskContextCheckBox = QtGui.QCheckBox(self.groupBox)
        self.switchTaskContextCheckBox.setObjectName("switchTaskContextCheckBox")
        self.gridLayout_3.addWidget(self.switchTaskContextCheckBox, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 5, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setStyleSheet("QGroupBox  {\n"
"    color: rgb(30, 167, 224);\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.taskEntitiesLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.taskEntitiesLayout.setObjectName("taskEntitiesLayout")
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setStyleSheet("QGroupBox  {\n"
"    color: rgb(30, 167, 224);\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.taskNameLabel = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.taskNameLabel.setFont(font)
        self.taskNameLabel.setText("")
        self.taskNameLabel.setObjectName("taskNameLabel")
        self.gridLayout_4.addWidget(self.taskNameLabel, 3, 1, 1, 1)
        self.validInvalidLabel = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validInvalidLabel.sizePolicy().hasHeightForWidth())
        self.validInvalidLabel.setSizePolicy(sizePolicy)
        self.validInvalidLabel.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setWeight(50)
        font.setBold(False)
        self.validInvalidLabel.setFont(font)
        self.validInvalidLabel.setText("")
        self.validInvalidLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.validInvalidLabel.setObjectName("validInvalidLabel")
        self.gridLayout_4.addWidget(self.validInvalidLabel, 3, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color: rgb(30, 167, 224);")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 3, 0, 1, 1)
        self.taskDefinitionLayout = QtGui.QHBoxLayout()
        self.taskDefinitionLayout.setSpacing(2)
        self.taskDefinitionLayout.setObjectName("taskDefinitionLayout")
        self.gridLayout_4.addLayout(self.taskDefinitionLayout, 0, 0, 1, 3)
        self.line_2 = QtGui.QFrame(self.groupBox_3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 2, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previousTaskLabel = QtGui.QLabel(Dialog)
        self.previousTaskLabel.setTextFormat(QtCore.Qt.RichText)
        self.previousTaskLabel.setOpenExternalLinks(True)
        self.previousTaskLabel.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.previousTaskLabel.setObjectName("previousTaskLabel")
        self.horizontalLayout_2.addWidget(self.previousTaskLabel)
        self.taskUrlLabel = QtGui.QLabel(Dialog)
        self.taskUrlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.taskUrlLabel.setOpenExternalLinks(True)
        self.taskUrlLabel.setObjectName("taskUrlLabel")
        self.horizontalLayout_2.addWidget(self.taskUrlLabel)
        self.entityUrlLabel = QtGui.QLabel(Dialog)
        self.entityUrlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.entityUrlLabel.setOpenExternalLinks(True)
        self.entityUrlLabel.setObjectName("entityUrlLabel")
        self.horizontalLayout_2.addWidget(self.entityUrlLabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.taskTemplateComboBox, self.assignTaskCheckBox)
        Dialog.setTabOrder(self.assignTaskCheckBox, self.switchTaskContextCheckBox)
        Dialog.setTabOrder(self.switchTaskContextCheckBox, self.createTaskButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Task Creation Template:", None, QtGui.QApplication.UnicodeUTF8))
        self.createTaskButton.setText(QtGui.QApplication.translate("Dialog", "Create New Task", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Creation Options", None, QtGui.QApplication.UnicodeUTF8))
        self.assignTaskCheckBox.setText(QtGui.QApplication.translate("Dialog", "Assign Task to Me", None, QtGui.QApplication.UnicodeUTF8))
        self.switchTaskContextCheckBox.setText(QtGui.QApplication.translate("Dialog", "Switch to Task Context", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Task Creation Context", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Task Name Definition", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "New Task Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.previousTaskLabel.setText(QtGui.QApplication.translate("Dialog", "Previous Task Created: ", None, QtGui.QApplication.UnicodeUTF8))
        self.taskUrlLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.entityUrlLabel.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
