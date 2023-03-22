# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task_entity_widget.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 49)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.entityNameLabel = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entityNameLabel.sizePolicy().hasHeightForWidth())
        self.entityNameLabel.setSizePolicy(sizePolicy)
        self.entityNameLabel.setMinimumSize(QtCore.QSize(125, 0))
        self.entityNameLabel.setObjectName("entityNameLabel")
        self.horizontalLayout.addWidget(self.entityNameLabel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.entityNameLabel.setText(QtGui.QApplication.translate("Form", "Entity Label:", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
