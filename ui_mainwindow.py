# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(553, 427)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.groupBox_Particulas = QGroupBox(self.centralwidget)
        self.groupBox_Particulas.setObjectName(u"groupBox_Particulas")
        self.gridLayout = QGridLayout(self.groupBox_Particulas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_id = QLineEdit(self.groupBox_Particulas)
        self.lineEdit_id.setObjectName(u"lineEdit_id")

        self.gridLayout.addWidget(self.lineEdit_id, 0, 1, 1, 1)

        self.spinBox_destinoY = QSpinBox(self.groupBox_Particulas)
        self.spinBox_destinoY.setObjectName(u"spinBox_destinoY")
        self.spinBox_destinoY.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_destinoY, 4, 1, 1, 1)

        self.label_origenX = QLabel(self.groupBox_Particulas)
        self.label_origenX.setObjectName(u"label_origenX")

        self.gridLayout.addWidget(self.label_origenX, 1, 0, 1, 1)

        self.label_destinoY = QLabel(self.groupBox_Particulas)
        self.label_destinoY.setObjectName(u"label_destinoY")

        self.gridLayout.addWidget(self.label_destinoY, 4, 0, 1, 1)

        self.label_green = QLabel(self.groupBox_Particulas)
        self.label_green.setObjectName(u"label_green")

        self.gridLayout.addWidget(self.label_green, 8, 0, 1, 1)

        self.spinBox_origenX = QSpinBox(self.groupBox_Particulas)
        self.spinBox_origenX.setObjectName(u"spinBox_origenX")
        self.spinBox_origenX.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_origenX, 1, 1, 1, 1)

        self.pushButton_AgregarInicio = QPushButton(self.groupBox_Particulas)
        self.pushButton_AgregarInicio.setObjectName(u"pushButton_AgregarInicio")

        self.gridLayout.addWidget(self.pushButton_AgregarInicio, 10, 0, 1, 2)

        self.spinBox_green = QSpinBox(self.groupBox_Particulas)
        self.spinBox_green.setObjectName(u"spinBox_green")
        self.spinBox_green.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_green, 8, 1, 1, 1)

        self.label_origenY = QLabel(self.groupBox_Particulas)
        self.label_origenY.setObjectName(u"label_origenY")

        self.gridLayout.addWidget(self.label_origenY, 2, 0, 1, 1)

        self.spinBox_destinoX = QSpinBox(self.groupBox_Particulas)
        self.spinBox_destinoX.setObjectName(u"spinBox_destinoX")
        self.spinBox_destinoX.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_destinoX, 3, 1, 1, 1)

        self.spinBox_red = QSpinBox(self.groupBox_Particulas)
        self.spinBox_red.setObjectName(u"spinBox_red")
        self.spinBox_red.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_red, 7, 1, 1, 1)

        self.lineEdit_velocidad = QLineEdit(self.groupBox_Particulas)
        self.lineEdit_velocidad.setObjectName(u"lineEdit_velocidad")

        self.gridLayout.addWidget(self.lineEdit_velocidad, 5, 1, 1, 1)

        self.label_velocidad = QLabel(self.groupBox_Particulas)
        self.label_velocidad.setObjectName(u"label_velocidad")

        self.gridLayout.addWidget(self.label_velocidad, 5, 0, 1, 1)

        self.spinBox_blue = QSpinBox(self.groupBox_Particulas)
        self.spinBox_blue.setObjectName(u"spinBox_blue")
        self.spinBox_blue.setMaximum(255)
        self.spinBox_blue.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.spinBox_blue, 9, 1, 1, 1)

        self.label_blue = QLabel(self.groupBox_Particulas)
        self.label_blue.setObjectName(u"label_blue")

        self.gridLayout.addWidget(self.label_blue, 9, 0, 1, 1)

        self.label_id = QLabel(self.groupBox_Particulas)
        self.label_id.setObjectName(u"label_id")

        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)

        self.label_destinoX = QLabel(self.groupBox_Particulas)
        self.label_destinoX.setObjectName(u"label_destinoX")

        self.gridLayout.addWidget(self.label_destinoX, 3, 0, 1, 1)

        self.label_red = QLabel(self.groupBox_Particulas)
        self.label_red.setObjectName(u"label_red")

        self.gridLayout.addWidget(self.label_red, 7, 0, 1, 1)

        self.spinBox_origenY = QSpinBox(self.groupBox_Particulas)
        self.spinBox_origenY.setObjectName(u"spinBox_origenY")
        self.spinBox_origenY.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_origenY, 2, 1, 1, 1)

        self.label_color = QLabel(self.groupBox_Particulas)
        self.label_color.setObjectName(u"label_color")

        self.gridLayout.addWidget(self.label_color, 6, 0, 1, 1)

        self.pushButton_AgregarFinal = QPushButton(self.groupBox_Particulas)
        self.pushButton_AgregarFinal.setObjectName(u"pushButton_AgregarFinal")

        self.gridLayout.addWidget(self.pushButton_AgregarFinal, 11, 0, 1, 2)

        self.pushButton_Mostrar = QPushButton(self.groupBox_Particulas)
        self.pushButton_Mostrar.setObjectName(u"pushButton_Mostrar")

        self.gridLayout.addWidget(self.pushButton_Mostrar, 12, 0, 1, 2)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.groupBox_Particulas)

        self.salida_Particulas = QPlainTextEdit(self.centralwidget)
        self.salida_Particulas.setObjectName(u"salida_Particulas")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.salida_Particulas)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 553, 21))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Algoritmia", None))
        self.groupBox_Particulas.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.label_origenX.setText(QCoreApplication.translate("MainWindow", u"Origen(x):", None))
        self.label_destinoY.setText(QCoreApplication.translate("MainWindow", u"Destino(Y)", None))
        self.label_green.setText(QCoreApplication.translate("MainWindow", u"green:", None))
        self.pushButton_AgregarInicio.setText(QCoreApplication.translate("MainWindow", u"Agregar al Inicio", None))
        self.label_origenY.setText(QCoreApplication.translate("MainWindow", u"Origen(Y)", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_blue.setText(QCoreApplication.translate("MainWindow", u"blue:", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"iD:", None))
        self.label_destinoX.setText(QCoreApplication.translate("MainWindow", u"Destino(X)", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"red:", None))
        self.label_color.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.pushButton_AgregarFinal.setText(QCoreApplication.translate("MainWindow", u"Agregar al Final", None))
        self.pushButton_Mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
    # retranslateUi

