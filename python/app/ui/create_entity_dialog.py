# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_entity_dialog.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 400)
        font = QFont()
        font.setFamily(u"Arial")
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dialogTitle = QLabel(Dialog)
        self.dialogTitle.setObjectName(u"dialogTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialogTitle.sizePolicy().hasHeightForWidth())
        self.dialogTitle.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.dialogTitle.setFont(font1)
        self.dialogTitle.setStyleSheet(u"color: rgb(30, 167, 224);")

        self.verticalLayout.addWidget(self.dialogTitle)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.fieldsVerticalLayout = QVBoxLayout()
        self.fieldsVerticalLayout.setObjectName(u"fieldsVerticalLayout")

        self.verticalLayout.addLayout(self.fieldsVerticalLayout)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(7)
        self.label.setFont(font2)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.creationLabel = QLabel(Dialog)
        self.creationLabel.setObjectName(u"creationLabel")
        self.creationLabel.setEnabled(True)
        sizePolicy.setHeightForWidth(self.creationLabel.sizePolicy().hasHeightForWidth())
        self.creationLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.creationLabel)

        self.entityUrlLabel = QLabel(Dialog)
        self.entityUrlLabel.setObjectName(u"entityUrlLabel")
        self.entityUrlLabel.setEnabled(True)
        sizePolicy.setHeightForWidth(self.entityUrlLabel.sizePolicy().hasHeightForWidth())
        self.entityUrlLabel.setSizePolicy(sizePolicy)
        self.entityUrlLabel.setTextFormat(Qt.RichText)
        self.entityUrlLabel.setAlignment(Qt.AlignCenter)
        self.entityUrlLabel.setOpenExternalLinks(True)
        self.entityUrlLabel.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout.addWidget(self.entityUrlLabel)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFont(font)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.createEntityButton = QPushButton(Dialog)
        self.createEntityButton.setObjectName(u"createEntityButton")
        self.createEntityButton.setEnabled(False)
        self.createEntityButton.setFont(font1)
        self.createEntityButton.setStyleSheet(u"QPushButton:enabled  {\n"
"    color: rgb(30, 167, 224);\n"
"}")

        self.verticalLayout.addWidget(self.createEntityButton)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dialogTitle.setText(QCoreApplication.translate("Dialog", u"Create a New Enitty", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Bold fields are required", None))
        self.creationLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.entityUrlLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.createEntityButton.setText(QCoreApplication.translate("Dialog", u"Create Entity", None))
    # retranslateUi
