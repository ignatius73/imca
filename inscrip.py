# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inscrip.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1247, 927)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 246, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(-20, 60, 1281, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_33 = QtGui.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(30, 410, 246, 18))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(Form)
        self.label_34.setGeometry(QtCore.QRect(30, 700, 141, 18))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(40, 730, 121, 69))
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 30, 41, 20))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 820, 1181, 64))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_15.addWidget(self.checkBox)
        spacerItem = QtGui.QSpacerItem(99, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_15.addWidget(self.checkBox_2)
        spacerItem1 = QtGui.QSpacerItem(99, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.horizontalLayout_15.addWidget(self.checkBox_3)
        spacerItem2 = QtGui.QSpacerItem(99, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.checkBox_6 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.horizontalLayout_15.addWidget(self.checkBox_6)
        spacerItem3 = QtGui.QSpacerItem(99, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.horizontalLayout_15.addWidget(self.checkBox_5)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(979, 900, 101, 22))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1100, 900, 101, 22))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(33, 110, 1191, 291))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.lnNombre = QtGui.QLineEdit(self.widget)
        self.lnNombre.setObjectName(_fromUtf8("lnNombre"))
        self.horizontalLayout.addWidget(self.lnNombre)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.cBSexo = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBSexo.sizePolicy().hasHeightForWidth())
        self.cBSexo.setSizePolicy(sizePolicy)
        self.cBSexo.setObjectName(_fromUtf8("cBSexo"))
        self.cBSexo.addItem(_fromUtf8(""))
        self.cBSexo.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cBSexo)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.hSEdad = QtGui.QSlider(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hSEdad.sizePolicy().hasHeightForWidth())
        self.hSEdad.setSizePolicy(sizePolicy)
        self.hSEdad.setProperty("value", 50)
        self.hSEdad.setOrientation(QtCore.Qt.Horizontal)
        self.hSEdad.setTickPosition(QtGui.QSlider.NoTicks)
        self.hSEdad.setTickInterval(5)
        self.hSEdad.setObjectName(_fromUtf8("hSEdad"))
        self.horizontalLayout.addWidget(self.hSEdad)
        self.lnEdad = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnEdad.sizePolicy().hasHeightForWidth())
        self.lnEdad.setSizePolicy(sizePolicy)
        self.lnEdad.setMinimumSize(QtCore.QSize(125, 0))
        self.lnEdad.setObjectName(_fromUtf8("lnEdad"))
        self.horizontalLayout.addWidget(self.lnEdad)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lnDni = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnDni.sizePolicy().hasHeightForWidth())
        self.lnDni.setSizePolicy(sizePolicy)
        self.lnDni.setObjectName(_fromUtf8("lnDni"))
        self.horizontalLayout_2.addWidget(self.lnDni)
        spacerItem4 = QtGui.QSpacerItem(37, 13, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.dENac = QtGui.QDateEdit(self.widget)
        self.dENac.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dENac.setWrapping(True)
        self.dENac.setAccelerated(True)
        self.dENac.setCalendarPopup(True)
        self.dENac.setObjectName(_fromUtf8("dENac"))
        self.horizontalLayout_2.addWidget(self.dENac)
        spacerItem5 = QtGui.QSpacerItem(37, 13, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lnLugar = QtGui.QLineEdit(self.widget)
        self.lnLugar.setObjectName(_fromUtf8("lnLugar"))
        self.horizontalLayout_2.addWidget(self.lnLugar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.cBCivil = QtGui.QComboBox(self.widget)
        self.cBCivil.setObjectName(_fromUtf8("cBCivil"))
        self.cBCivil.addItem(_fromUtf8(""))
        self.cBCivil.addItem(_fromUtf8(""))
        self.cBCivil.addItem(_fromUtf8(""))
        self.cBCivil.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cBCivil)
        spacerItem6 = QtGui.QSpacerItem(37, 13, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_3.addWidget(self.label_11)
        self.cBHijos = QtGui.QComboBox(self.widget)
        self.cBHijos.setObjectName(_fromUtf8("cBHijos"))
        self.cBHijos.addItem(_fromUtf8(""))
        self.cBHijos.addItem(_fromUtf8(""))
        self.cBHijos.addItem(_fromUtf8(""))
        self.cBHijos.addItem(_fromUtf8(""))
        self.cBHijos.addItem(_fromUtf8(""))
        self.cBHijos.addItem(_fromUtf8(""))
        self.cBHijos.addItem(_fromUtf8(""))
        self.cBHijos.addItem(_fromUtf8(""))
        self.cBHijos.addItem(_fromUtf8(""))
        self.cBHijos.addItem(_fromUtf8(""))
        self.cBHijos.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cBHijos)
        spacerItem7 = QtGui.QSpacerItem(37, 13, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_3.addWidget(self.label_12)
        self.lnFamiliar = QtGui.QLineEdit(self.widget)
        self.lnFamiliar.setObjectName(_fromUtf8("lnFamiliar"))
        self.horizontalLayout_3.addWidget(self.lnFamiliar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_4.addWidget(self.label_13)
        self.lnCalle = QtGui.QLineEdit(self.widget)
        self.lnCalle.setObjectName(_fromUtf8("lnCalle"))
        self.horizontalLayout_4.addWidget(self.lnCalle)
        self.label_14 = QtGui.QLabel(self.widget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_4.addWidget(self.label_14)
        self.lnNum = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnNum.sizePolicy().hasHeightForWidth())
        self.lnNum.setSizePolicy(sizePolicy)
        self.lnNum.setObjectName(_fromUtf8("lnNum"))
        self.horizontalLayout_4.addWidget(self.lnNum)
        self.label_15 = QtGui.QLabel(self.widget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_4.addWidget(self.label_15)
        self.lnPiso = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnPiso.sizePolicy().hasHeightForWidth())
        self.lnPiso.setSizePolicy(sizePolicy)
        self.lnPiso.setObjectName(_fromUtf8("lnPiso"))
        self.horizontalLayout_4.addWidget(self.lnPiso)
        self.label_16 = QtGui.QLabel(self.widget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_4.addWidget(self.label_16)
        self.lnDepto = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnDepto.sizePolicy().hasHeightForWidth())
        self.lnDepto.setSizePolicy(sizePolicy)
        self.lnDepto.setObjectName(_fromUtf8("lnDepto"))
        self.horizontalLayout_4.addWidget(self.lnDepto)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_17 = QtGui.QLabel(self.widget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_5.addWidget(self.label_17)
        self.lineEdit_12 = QtGui.QLineEdit(self.widget)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.horizontalLayout_5.addWidget(self.lineEdit_12)
        spacerItem8 = QtGui.QSpacerItem(37, 13, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.label_18 = QtGui.QLabel(self.widget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_5.addWidget(self.label_18)
        self.lineEdit_11 = QtGui.QLineEdit(self.widget)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.horizontalLayout_5.addWidget(self.lineEdit_11)
        spacerItem9 = QtGui.QSpacerItem(37, 13, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.label_19 = QtGui.QLabel(self.widget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_5.addWidget(self.label_19)
        self.lineEdit_15 = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.horizontalLayout_5.addWidget(self.lineEdit_15)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_20 = QtGui.QLabel(self.widget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_6.addWidget(self.label_20)
        self.lineEdit_14 = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.horizontalLayout_6.addWidget(self.lineEdit_14)
        self.label_21 = QtGui.QLabel(self.widget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_6.addWidget(self.label_21)
        self.lineEdit_16 = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_16.sizePolicy().hasHeightForWidth())
        self.lineEdit_16.setSizePolicy(sizePolicy)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.horizontalLayout_6.addWidget(self.lineEdit_16)
        self.label_22 = QtGui.QLabel(self.widget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_6.addWidget(self.label_22)
        self.lineEdit_17 = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_17.sizePolicy().hasHeightForWidth())
        self.lineEdit_17.setSizePolicy(sizePolicy)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.horizontalLayout_6.addWidget(self.lineEdit_17)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(30, 430, 1191, 261))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_24 = QtGui.QLabel(self.widget1)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_8.addWidget(self.label_24)
        self.lntitulo = QtGui.QLineEdit(self.widget1)
        self.lntitulo.setObjectName(_fromUtf8("lntitulo"))
        self.horizontalLayout_8.addWidget(self.lntitulo)
        self.label_26 = QtGui.QLabel(self.widget1)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_8.addWidget(self.label_26)
        self.dateEdit_2 = QtGui.QDateEdit(self.widget1)
        self.dateEdit_2.setCurrentSection(QtGui.QDateTimeEdit.YearSection)
        self.dateEdit_2.setCalendarPopup(False)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.horizontalLayout_8.addWidget(self.dateEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_27 = QtGui.QLabel(self.widget1)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_9.addWidget(self.label_27)
        self.lineEdit_20 = QtGui.QLineEdit(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_20.sizePolicy().hasHeightForWidth())
        self.lineEdit_20.setSizePolicy(sizePolicy)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.horizontalLayout_9.addWidget(self.lineEdit_20)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.label_25 = QtGui.QLabel(self.widget1)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_9.addWidget(self.label_25)
        self.lineEdit_21 = QtGui.QLineEdit(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_21.sizePolicy().hasHeightForWidth())
        self.lineEdit_21.setSizePolicy(sizePolicy)
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.horizontalLayout_9.addWidget(self.lineEdit_21)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_28 = QtGui.QLabel(self.widget1)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_10.addWidget(self.label_28)
        self.lineEdit_22 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.horizontalLayout_10.addWidget(self.lineEdit_22)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_29 = QtGui.QLabel(self.widget1)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_11.addWidget(self.label_29)
        self.lineEdit_23 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.horizontalLayout_11.addWidget(self.lineEdit_23)
        self.label_31 = QtGui.QLabel(self.widget1)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.horizontalLayout_11.addWidget(self.label_31)
        self.lineEdit_24 = QtGui.QLineEdit(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_24.sizePolicy().hasHeightForWidth())
        self.lineEdit_24.setSizePolicy(sizePolicy)
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.horizontalLayout_11.addWidget(self.lineEdit_24)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_30 = QtGui.QLabel(self.widget1)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_12.addWidget(self.label_30)
        self.lineEdit_25 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.horizontalLayout_12.addWidget(self.lineEdit_25)
        self.label_32 = QtGui.QLabel(self.widget1)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_12.addWidget(self.label_32)
        self.lineEdit_26 = QtGui.QLineEdit(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_26.sizePolicy().hasHeightForWidth())
        self.lineEdit_26.setSizePolicy(sizePolicy)
        self.lineEdit_26.setObjectName(_fromUtf8("lineEdit_26"))
        self.horizontalLayout_12.addWidget(self.lineEdit_26)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.widget2 = QtGui.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(32, 13, 1191, 41))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.line_2 = QtGui.QFrame(self.widget2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_7.addWidget(self.line_2)
        self.label = QtGui.QLabel(self.widget2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_7.addWidget(self.label)
        self.cBCarrera = QtGui.QComboBox(self.widget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBCarrera.sizePolicy().hasHeightForWidth())
        self.cBCarrera.setSizePolicy(sizePolicy)
        self.cBCarrera.setObjectName(_fromUtf8("cBCarrera"))
        self.cBCarrera.addItem(_fromUtf8(""))
        self.cBCarrera.addItem(_fromUtf8(""))
        self.cBCarrera.addItem(_fromUtf8(""))
        self.cBCarrera.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.cBCarrera)
        spacerItem11 = QtGui.QSpacerItem(150, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.label_2 = QtGui.QLabel(self.widget2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.lnCiclo = QtGui.QLineEdit(self.widget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnCiclo.sizePolicy().hasHeightForWidth())
        self.lnCiclo.setSizePolicy(sizePolicy)
        self.lnCiclo.setObjectName(_fromUtf8("lnCiclo"))
        self.horizontalLayout_7.addWidget(self.lnCiclo)
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(190, 730, 1031, 71))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget3 = QtGui.QWidget(self.splitter)
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.widget3)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_23 = QtGui.QLabel(self.widget3)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_13.addWidget(self.label_23)
        self.lineEdit_29 = QtGui.QLineEdit(self.widget3)
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.horizontalLayout_13.addWidget(self.lineEdit_29)
        self.label_35 = QtGui.QLabel(self.widget3)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.horizontalLayout_13.addWidget(self.label_35)
        self.lineEdit_30 = QtGui.QLineEdit(self.widget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_30.sizePolicy().hasHeightForWidth())
        self.lineEdit_30.setSizePolicy(sizePolicy)
        self.lineEdit_30.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.horizontalLayout_13.addWidget(self.lineEdit_30)
        self.widget4 = QtGui.QWidget(self.splitter)
        self.widget4.setObjectName(_fromUtf8("widget4"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.widget4)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_36 = QtGui.QLabel(self.widget4)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.horizontalLayout_14.addWidget(self.label_36)
        self.lineEdit_27 = QtGui.QLineEdit(self.widget4)
        self.lineEdit_27.setObjectName(_fromUtf8("lineEdit_27"))
        self.horizontalLayout_14.addWidget(self.lineEdit_27)
        self.label_37 = QtGui.QLabel(self.widget4)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.horizontalLayout_14.addWidget(self.label_37)
        self.lineEdit_28 = QtGui.QLineEdit(self.widget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_28.sizePolicy().hasHeightForWidth())
        self.lineEdit_28.setSizePolicy(sizePolicy)
        self.lineEdit_28.setObjectName(_fromUtf8("lineEdit_28"))
        self.horizontalLayout_14.addWidget(self.lineEdit_28)
        self.label_4.setBuddy(self.lnNombre)
        self.label_5.setBuddy(self.cBSexo)
        self.label_6.setBuddy(self.lnEdad)
        self.label_7.setBuddy(self.lnDni)
        self.label_8.setBuddy(self.dENac)
        self.label_9.setBuddy(self.lnLugar)
        self.label_11.setBuddy(self.cBHijos)
        self.label_12.setBuddy(self.lnFamiliar)
        self.label_13.setBuddy(self.lnCalle)
        self.label_14.setBuddy(self.lnNum)
        self.label_15.setBuddy(self.lnPiso)
        self.label_16.setBuddy(self.lnDepto)
        self.label_17.setBuddy(self.lineEdit_12)
        self.label_18.setBuddy(self.lineEdit_11)
        self.label_19.setBuddy(self.lineEdit_15)
        self.label_20.setBuddy(self.lineEdit_14)
        self.label_21.setBuddy(self.lineEdit_16)
        self.label_22.setBuddy(self.lineEdit_17)
        self.label_24.setBuddy(self.lntitulo)
        self.label_27.setBuddy(self.lineEdit_20)
        self.label_25.setBuddy(self.lineEdit_21)
        self.label_28.setBuddy(self.lineEdit_22)
        self.label_29.setBuddy(self.lineEdit_23)
        self.label_31.setBuddy(self.lineEdit_24)
        self.label_30.setBuddy(self.lineEdit_25)
        self.label_32.setBuddy(self.lineEdit_26)
        self.label.setBuddy(self.cBCarrera)
        self.label_2.setBuddy(self.lnCiclo)
        self.label_23.setBuddy(self.lineEdit_29)
        self.label_35.setBuddy(self.lineEdit_30)
        self.label_36.setBuddy(self.lineEdit_27)
        self.label_37.setBuddy(self.lineEdit_28)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.cBCarrera, self.lnCiclo)
        Form.setTabOrder(self.lnCiclo, self.cBSexo)
        Form.setTabOrder(self.cBSexo, self.lnDepto)
        Form.setTabOrder(self.lnDepto, self.lnNum)
        Form.setTabOrder(self.lnNum, self.lnDni)
        Form.setTabOrder(self.lnDni, self.lnCalle)
        Form.setTabOrder(self.lnCalle, self.lnNombre)
        Form.setTabOrder(self.lnNombre, self.lineEdit_11)
        Form.setTabOrder(self.lineEdit_11, self.lineEdit_12)
        Form.setTabOrder(self.lineEdit_12, self.lineEdit_14)
        Form.setTabOrder(self.lineEdit_14, self.lineEdit_15)
        Form.setTabOrder(self.lineEdit_15, self.lnPiso)
        Form.setTabOrder(self.lnPiso, self.dENac)
        Form.setTabOrder(self.dENac, self.lnLugar)
        Form.setTabOrder(self.lnLugar, self.cBHijos)
        Form.setTabOrder(self.cBHijos, self.lnFamiliar)
        Form.setTabOrder(self.lnFamiliar, self.lineEdit_16)
        Form.setTabOrder(self.lineEdit_16, self.lineEdit_17)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Datos Personales del alumno</span></p></body></html>", None))
        self.label_33.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Estudios Cursados</span></p></body></html>", None))
        self.label_34.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Datos Laborales</span></p></body></html>", None))
        self.groupBox.setTitle(_translate("Form", "Trabaja", None))
        self.radioButton.setText(_translate("Form", "Sí", None))
        self.radioButton_2.setText(_translate("Form", "No", None))
        self.groupBox_2.setTitle(_translate("Form", "Documentación Presentada", None))
        self.checkBox.setText(_translate("Form", "Fotocpoia DNI", None))
        self.checkBox_2.setText(_translate("Form", "Fotocopia Título Secundario/Polimodal", None))
        self.checkBox_3.setText(_translate("Form", "Número de registro", None))
        self.checkBox_6.setText(_translate("Form", "Fotos", None))
        self.checkBox_5.setText(_translate("Form", "Certificado Médico", None))
        self.pushButton.setText(_translate("Form", "&Siguiente >>", None))
        self.pushButton_2.setText(_translate("Form", "&Limpiar", None))
        self.label_4.setText(_translate("Form", "Apellido y Nombres", None))
        self.label_5.setText(_translate("Form", "Sexo", None))
        self.cBSexo.setItemText(0, _translate("Form", "Femenino", None))
        self.cBSexo.setItemText(1, _translate("Form", "Masculino", None))
        self.label_6.setText(_translate("Form", "Edad", None))
        self.label_7.setText(_translate("Form", "Documento único", None))
        self.label_8.setText(_translate("Form", "Fecha de Nacimiento", None))
        self.dENac.setDisplayFormat(_translate("Form", "dd/MM/yyyy", None))
        self.label_9.setText(_translate("Form", "Lugar de Nacimiento", None))
        self.label_10.setText(_translate("Form", "Estado civil", None))
        self.cBCivil.setItemText(0, _translate("Form", "Solterx", None))
        self.cBCivil.setItemText(1, _translate("Form", "Casadx", None))
        self.cBCivil.setItemText(2, _translate("Form", "Divorciadx", None))
        self.cBCivil.setItemText(3, _translate("Form", "En Convivencia", None))
        self.label_11.setText(_translate("Form", "Hijos", None))
        self.cBHijos.setItemText(0, _translate("Form", "No", None))
        self.cBHijos.setItemText(1, _translate("Form", "1", None))
        self.cBHijos.setItemText(2, _translate("Form", "2", None))
        self.cBHijos.setItemText(3, _translate("Form", "3", None))
        self.cBHijos.setItemText(4, _translate("Form", "4", None))
        self.cBHijos.setItemText(5, _translate("Form", "5", None))
        self.cBHijos.setItemText(6, _translate("Form", "6", None))
        self.cBHijos.setItemText(7, _translate("Form", "7", None))
        self.cBHijos.setItemText(8, _translate("Form", "8", None))
        self.cBHijos.setItemText(9, _translate("Form", "9", None))
        self.cBHijos.setItemText(10, _translate("Form", "10", None))
        self.label_12.setText(_translate("Form", "Familiares a Cargo", None))
        self.label_13.setText(_translate("Form", "Domicilio - Calle", None))
        self.label_14.setText(_translate("Form", "N°", None))
        self.label_15.setText(_translate("Form", "Piso", None))
        self.label_16.setText(_translate("Form", "Depto", None))
        self.label_17.setText(_translate("Form", "Localidad/Barrio", None))
        self.label_18.setText(_translate("Form", "Partido", None))
        self.label_19.setText(_translate("Form", "CP", None))
        self.label_20.setText(_translate("Form", "Teléfono", None))
        self.label_21.setText(_translate("Form", "Móvil", None))
        self.label_22.setText(_translate("Form", "Correo Electrónico", None))
        self.label_24.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Título nivel medio o polimodal</span></p></body></html>", None))
        self.label_26.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Año de Egreso</span></p></body></html>", None))
        self.dateEdit_2.setDisplayFormat(_translate("Form", "yyyy", None))
        self.label_27.setText(_translate("Form", "Escuela", None))
        self.label_25.setText(_translate("Form", "Distrito", None))
        self.label_28.setText(_translate("Form", "Otros Estudios", None))
        self.label_29.setText(_translate("Form", "Institución", None))
        self.label_31.setText(_translate("Form", "Año de Egreso", None))
        self.label_30.setText(_translate("Form", "Institución", None))
        self.label_32.setText(_translate("Form", "Año de Egreso", None))
        self.label.setText(_translate("Form", "Carrera", None))
        self.cBCarrera.setItemText(0, _translate("Form", "FOBA", None))
        self.cBCarrera.setItemText(1, _translate("Form", "Tecnicatura", None))
        self.cBCarrera.setItemText(2, _translate("Form", "Profesorado de Artes Plásticas", None))
        self.cBCarrera.setItemText(3, _translate("Form", "Cursos Extraprogramáticos", None))
        self.label_2.setText(_translate("Form", "Año", None))
        self.label_23.setText(_translate("Form", "Actividad", None))
        self.label_35.setText(_translate("Form", "Horario Habitual", None))
        self.label_36.setText(_translate("Form", "Obra Social", None))
        self.label_37.setText(_translate("Form", "Teléfono de Emergencias", None))
