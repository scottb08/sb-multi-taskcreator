# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_entity_widget.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 49)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.entityNameLabel = QLabel(Form)
        self.entityNameLabel.setObjectName(u"entityNameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entityNameLabel.sizePolicy().hasHeightForWidth())
        self.entityNameLabel.setSizePolicy(sizePolicy)
        self.entityNameLabel.setMinimumSize(QSize(125, 0))

        self.horizontalLayout.addWidget(self.entityNameLabel)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.entityNameLabel.setText(QCoreApplication.translate("Form", u"Entity Label:", None))
    # retranslateUi
