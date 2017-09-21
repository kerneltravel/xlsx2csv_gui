# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\dev_works\pyexcel2csv_gui\winmain\main.ui'
#
# Created: Thu Sep 21 20:17:41 2017
#      by: PyQt4 UI code generator 4.10
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(539, 192)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/ico.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnSelectExcelFile = QtGui.QPushButton(self.centralWidget)
        self.btnSelectExcelFile.setMinimumSize(QtCore.QSize(100, 50))
        self.btnSelectExcelFile.setObjectName(_fromUtf8("btnSelectExcelFile"))
        self.horizontalLayout.addWidget(self.btnSelectExcelFile)
        self.excelfilepath = QtGui.QLineEdit(self.centralWidget)
        self.excelfilepath.setObjectName(_fromUtf8("excelfilepath"))
        self.horizontalLayout.addWidget(self.excelfilepath)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "excel export to csv with all quota", None))
        self.btnSelectExcelFile.setText(_translate("MainWindow", "open excel", None))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

