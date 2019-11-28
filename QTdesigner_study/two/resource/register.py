# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        Form.setStyleSheet("\n"
                           "QWidget#Form{\n"
                           "    border-image: url(:/register/images/register_gackground2.jpg);;\n"
                           "\n"
                           "}\n"
                           "")
        self.main_menue_btn = QtWidgets.QPushButton(Form)
        self.main_menue_btn.setGeometry(QtCore.QRect(20, 20, 61, 61))
        self.main_menue_btn.setStyleSheet("QPushButton {\n"
                                          "    border-radius:30px;\n"
                                          "    background-color:rgb(255, 170, 255);\n"
                                          "    border:2px solid rgb(239, 208, 188);\n"
                                          "    color:white;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    border:4px double rgb(251, 107, 255);\n"
                                          "}\n"
                                          "QPushButton:checked {\n"
                                          "    background-color:rgb(255, 0, 255);\n"
                                          "}")
        self.main_menue_btn.setCheckable(True)
        self.main_menue_btn.setObjectName("main_menue_btn")
        self.reset_menue_btn = QtWidgets.QPushButton(Form)
        self.reset_menue_btn.setGeometry(QtCore.QRect(20, 120, 61, 61))
        self.reset_menue_btn.setStyleSheet("QPushButton {\n"
                                           "    border-radius:30px;\n"
                                           "    background-color:rgb(255, 170, 255);\n"
                                           "    border:2px solid rgb(239, 208, 188);\n"
                                           "    color:white;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    border:4px double rgb(251, 107, 255);\n"
                                           "}\n"
                                           "QPushButton:checked {\n"
                                           "    background-color:rgb(255, 0, 255);\n"
                                           "}")
        self.reset_menue_btn.setCheckable(True)
        self.reset_menue_btn.setObjectName("reset_menue_btn")
        self.exit_menue_btn = QtWidgets.QPushButton(Form)
        self.exit_menue_btn.setGeometry(QtCore.QRect(100, 80, 61, 61))
        self.exit_menue_btn.setStyleSheet("QPushButton {\n"
                                          "    border-radius:30px;\n"
                                          "    background-color:rgb(255, 170, 255);\n"
                                          "    border:2px solid rgb(239, 208, 188);\n"
                                          "    color:white;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    border:4px double rgb(251, 107, 255);\n"
                                          "}\n"
                                          "QPushButton:checked {\n"
                                          "    background-color:rgb(255, 0, 255);\n"
                                          "}")
        self.exit_menue_btn.setCheckable(True)
        self.exit_menue_btn.setObjectName("exit_menue_btn")
        self.about_menue_btn = QtWidgets.QPushButton(Form)
        self.about_menue_btn.setGeometry(QtCore.QRect(130, 10, 61, 61))
        self.about_menue_btn.setStyleSheet("QPushButton {\n"
                                           "    border-radius:30px;\n"
                                           "    background-color:rgb(255, 170, 255);\n"
                                           "    border:2px solid rgb(239, 208, 188);\n"
                                           "    color:white;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    border:4px double rgb(251, 107, 255);\n"
                                           "}\n"
                                           "QPushButton:checked {\n"
                                           "    background-color:rgb(255, 0, 255);\n"
                                           "}")
        self.about_menue_btn.setCheckable(True)
        self.about_menue_btn.setObjectName("about_menue_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 200, 241, 229))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("background-color:transparent;\n"
                                    "color:rgb(199, 255, 217);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid lightgray")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setStyleSheet("background-color:transparent;\n"
                                      "color:rgb(199, 255, 217);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid lightgray")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color:rgb(238, 210, 163);\n"
                                   "font: 14pt \"华文琥珀\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setStyleSheet("background-color:transparent;\n"
                                      "color:rgb(199, 255, 217);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid lightgray")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    font: 20pt \"华文行楷\";\n"
                                      "    color:rgb(238, 210, 163);\n"
                                      "    background-color:rgb(87, 141, 176);\n"
                                      "    border-radius:20px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color:rgb(0, 170, 255);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:rgb(85, 85, 255);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.retranslateUi(Form)
        self.main_menue_btn.clicked.connect(Form.show_hide_menue)
        self.about_menue_btn.clicked.connect(Form.about_yz)
        self.exit_menue_btn.clicked.connect(Form.reset)
        self.reset_menue_btn.clicked.connect(Form.exit_pane)
        self.pushButton.clicked.connect(Form.check_register)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menue_btn.setText(_translate("Form", "菜单"))
        self.reset_menue_btn.setText(_translate("Form", "退出"))
        self.exit_menue_btn.setText(_translate("Form", "重置"))
        self.about_menue_btn.setText(_translate("Form", "关于"))
        self.label_2.setStyleSheet(_translate("Form", "color:rgb(238, 210, 163);\n"
                                                      "font: 14pt \"华文琥珀\";"))
        self.label_2.setText(_translate("Form", "密       码："))
        self.label_3.setText(_translate("Form", "确认密码："))
        self.pushButton.setText(_translate("Form", "注册"))
        self.label.setStyleSheet(_translate("Form", "color:rgb(238, 210, 163);\n"
                                                    "font: 14pt \"华文琥珀\";"))
        self.label.setText(_translate("Form", "账       号："))


import register_images_rc
