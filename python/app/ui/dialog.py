# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from tank.platform.qt import QtCore
for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls

from tank.platform.qt import QtGui
for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls


from  . import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 386)
        font = QFont()
        font.setFamily(u"Arial")
        Dialog.setFont(font)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_3 = QFrame(Dialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 8, 0, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"color: rgb(30, 167, 224);")

        self.horizontalLayout.addWidget(self.label_2)

        self.taskTemplateComboBox = QComboBox(Dialog)
        self.taskTemplateComboBox.setObjectName(u"taskTemplateComboBox")

        self.horizontalLayout.addWidget(self.taskTemplateComboBox)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.createTaskButton = QPushButton(Dialog)
        self.createTaskButton.setObjectName(u"createTaskButton")
        self.createTaskButton.setEnabled(False)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.createTaskButton.setFont(font1)
        self.createTaskButton.setStyleSheet(u"QPushButton:enabled  {\n"
"    color: rgb(30, 167, 224);\n"
"}")

        self.gridLayout_2.addWidget(self.createTaskButton, 1, 0, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 9, 0, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox  {\n"
"    color: rgb(30, 167, 224);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.assignTaskCheckBox = QCheckBox(self.groupBox)
        self.assignTaskCheckBox.setObjectName(u"assignTaskCheckBox")
        self.assignTaskCheckBox.setChecked(True)

        self.gridLayout_3.addWidget(self.assignTaskCheckBox, 0, 0, 1, 1)

        self.switchTaskContextCheckBox = QCheckBox(self.groupBox)
        self.switchTaskContextCheckBox.setObjectName(u"switchTaskContextCheckBox")

        self.gridLayout_3.addWidget(self.switchTaskContextCheckBox, 0, 1, 1, 1)

        self.close_checkBox = QCheckBox(self.groupBox)
        self.close_checkBox.setObjectName(u"close_checkBox")
        self.close_checkBox.setChecked(True)

        self.gridLayout_3.addWidget(self.close_checkBox, 0, 2, 1, 1)

        self.gridLayout.addWidget(self.groupBox, 5, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox  {\n"
"    color: rgb(30, 167, 224);\n"
"}")
        self.taskEntitiesLayout = QVBoxLayout(self.groupBox_2)
        self.taskEntitiesLayout.setObjectName(u"taskEntitiesLayout")

        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QGroupBox  {\n"
"    color: rgb(30, 167, 224);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.taskNameLabel = QLabel(self.groupBox_3)
        self.taskNameLabel.setObjectName(u"taskNameLabel")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.taskNameLabel.setFont(font2)

        self.gridLayout_4.addWidget(self.taskNameLabel, 3, 1, 1, 1)

        self.validInvalidLabel = QLabel(self.groupBox_3)
        self.validInvalidLabel.setObjectName(u"validInvalidLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.validInvalidLabel.sizePolicy().hasHeightForWidth())
        self.validInvalidLabel.setSizePolicy(sizePolicy1)
        self.validInvalidLabel.setMinimumSize(QSize(50, 0))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setBold(False)
        font3.setWeight(50)
        self.validInvalidLabel.setFont(font3)
        self.validInvalidLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.validInvalidLabel, 3, 2, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: rgb(30, 167, 224);")

        self.gridLayout_4.addWidget(self.label, 3, 0, 1, 1)

        self.taskDefinitionLayout = QHBoxLayout()
        self.taskDefinitionLayout.setSpacing(2)
        self.taskDefinitionLayout.setObjectName(u"taskDefinitionLayout")

        self.gridLayout_4.addLayout(self.taskDefinitionLayout, 0, 0, 1, 3)

        self.line_2 = QFrame(self.groupBox_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 2, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.previousTaskLabel = QLabel(Dialog)
        self.previousTaskLabel.setObjectName(u"previousTaskLabel")
        self.previousTaskLabel.setTextFormat(Qt.RichText)
        self.previousTaskLabel.setOpenExternalLinks(True)
        self.previousTaskLabel.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.previousTaskLabel)

        self.taskUrlLabel = QLabel(Dialog)
        self.taskUrlLabel.setObjectName(u"taskUrlLabel")
        self.taskUrlLabel.setAlignment(Qt.AlignCenter)
        self.taskUrlLabel.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.taskUrlLabel)

        self.entityUrlLabel = QLabel(Dialog)
        self.entityUrlLabel.setObjectName(u"entityUrlLabel")
        self.entityUrlLabel.setAlignment(Qt.AlignCenter)
        self.entityUrlLabel.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.entityUrlLabel)

        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        QWidget.setTabOrder(self.taskTemplateComboBox, self.assignTaskCheckBox)
        QWidget.setTabOrder(self.assignTaskCheckBox, self.switchTaskContextCheckBox)
        QWidget.setTabOrder(self.switchTaskContextCheckBox, self.createTaskButton)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"The Current Sgtk Environment", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Task Creation Template:", None))
        self.createTaskButton.setText(QCoreApplication.translate("Dialog", u"Create New Task", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Creation Options", None))
        self.assignTaskCheckBox.setText(QCoreApplication.translate("Dialog", u"Assign Task to Me", None))
        self.switchTaskContextCheckBox.setText(QCoreApplication.translate("Dialog", u"Switch to Task Context", None))
        self.close_checkBox.setText(QCoreApplication.translate("Dialog", u"Close After Creation", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Task Creation Context", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Task Name Definition", None))
        self.taskNameLabel.setText("")
        self.validInvalidLabel.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"New Task Name:", None))
        self.previousTaskLabel.setText(QCoreApplication.translate("Dialog", u"Previous Task Created: ", None))
        self.taskUrlLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.entityUrlLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi
