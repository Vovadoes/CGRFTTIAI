# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files/ResultWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(510, 150)
        Form.setMinimumSize(QtCore.QSize(510, 150))
        Form.setMaximumSize(QtCore.QSize(510, 150))
        Form.setStyleSheet("")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_39 = QtWidgets.QLabel(Form)
        self.label_39.setMinimumSize(QtCore.QSize(300, 0))
        self.label_39.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_10.setEnabled(False)
        self.doubleSpinBox_10.setMinimumSize(QtCore.QSize(214, 25))
        self.doubleSpinBox_10.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.doubleSpinBox_10.setFont(font)
        self.doubleSpinBox_10.setStyleSheet("color: black; background-color: white;")
        self.doubleSpinBox_10.setDecimals(2)
        self.doubleSpinBox_10.setMinimum(-999999999.0)
        self.doubleSpinBox_10.setMaximum(999999999.0)
        self.doubleSpinBox_10.setSingleStep(0.001)
        self.doubleSpinBox_10.setProperty("value", 0.0)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.gridLayout_18.addWidget(self.doubleSpinBox_10, 0, 2, 1, 1)
        self.label_40 = QtWidgets.QLabel(Form)
        self.label_40.setMinimumSize(QtCore.QSize(60, 0))
        self.label_40.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.gridLayout_18.addWidget(self.label_40, 0, 3, 1, 1)
        self.label_41 = QtWidgets.QLabel(Form)
        self.label_41.setMinimumSize(QtCore.QSize(30, 0))
        self.label_41.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.gridLayout_18.addWidget(self.label_41, 0, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(Form)
        self.label_38.setMinimumSize(QtCore.QSize(20, 0))
        self.label_38.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.gridLayout_18.addWidget(self.label_38, 0, 1, 1, 1)
        self.gridLayout_18.setColumnStretch(3, 1)
        self.gridLayout.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Расчет реальной наращенной суммы с учетом инфляции"))
        self.label_39.setText(_translate("Form", "<html><head/><body><p>Вывод: брутто-ставка с учетом инфляции равна: </p></body></html>"))
        self.label_40.setText(_translate("Form", "%"))
        self.label_41.setText(_translate("Form", "<html><head/><body><p>r</p></body></html>"))
        self.label_38.setText(_translate("Form", "="))
        self.pushButton.setText(_translate("Form", "ОК"))
