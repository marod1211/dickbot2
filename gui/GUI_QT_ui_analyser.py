# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_QT_ui_analyser.ui'
#
# Created: Sun Aug 21 21:38:51 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 748)
        Form.setMinimumSize(QtCore.QSize(722, 748))
        Form.setMaximumSize(QtCore.QSize(722, 748))
        self.button_analyse = QtGui.QPushButton(Form)
        self.button_analyse.setGeometry(QtCore.QRect(380, 160, 281, 31))
        self.button_analyse.setObjectName("button_analyse")
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 80, 571, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 115, 571, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.combobox_strategy = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.combobox_strategy.setObjectName("combobox_strategy")
        self.horizontalLayout.addWidget(self.combobox_strategy)
        self.combobox_gamestage = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.combobox_gamestage.setObjectName("combobox_gamestage")
        self.horizontalLayout.addWidget(self.combobox_gamestage)
        self.combobox_actiontype = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.combobox_actiontype.setObjectName("combobox_actiontype")
        self.horizontalLayout.addWidget(self.combobox_actiontype)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(300, 160, 71, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(240, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 340, 281, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vLayout_bar = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vLayout_bar.setContentsMargins(0, 0, 0, 0)
        self.vLayout_bar.setObjectName("vLayout_bar")
        self.widget = QtGui.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.vLayout_bar.addWidget(self.widget)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 200, 281, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vLayout_fundschange = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vLayout_fundschange.setContentsMargins(0, 0, 0, 0)
        self.vLayout_fundschange.setObjectName("vLayout_fundschange")
        self.widget_2 = QtGui.QWidget(self.verticalLayoutWidget_2)
        self.widget_2.setObjectName("widget_2")
        self.vLayout_fundschange.addWidget(self.widget_2)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(380, 340, 281, 401))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtGui.QWidget(self.horizontalLayoutWidget_3)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.lcdNumber_2 = QtGui.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(143, 160, 71, 31))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 170, 51, 20))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget_4 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(380, 200, 281, 121))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_4 = QtGui.QWidget(self.horizontalLayoutWidget_4)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4.addWidget(self.widget_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.button_analyse.setText(QtGui.QApplication.translate("Form", "Show Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Strategy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Game Stage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Action Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Strategy Analyser", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Return %", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Total hads", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
