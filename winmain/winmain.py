# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from string import *
from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Ui_main import Ui_MainWindow

import os
from pyexcel_xlsx import get_data
# python's stdlib csv not support import unicode data. so use unicodecsv as csv
import unicodecsv as csv

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.xlsfilepath = ""

    @pyqtSignature("")
    def on_btnSelectExcelFile_clicked(self):
        format = 'xlsx'
        initialPath = QtCore.QDir.currentPath() 
        fileName = QtGui.QFileDialog.getOpenFileName(self, u"select excel file, extension must be xlsx",initialPath,"%s Files (*.%s);;All Files (*)" % (format.upper(), format))
        finalcsv = ""
        if fileName!="":
            self.xlsfilepath = fileName
            self.excelfilepath.setText(fileName)
            data = get_data(str(self.xlsfilepath.toLocal8Bit()))
            
            # supporse windows's path is default encoded as 'gbk' charset. so first to decode by 'gbk',and reencode to 'utf8', AS our python and pyQT source is in utf8 mode.
            csvfilepath = u"%s%s"%(os.path.splitext(str(self.xlsfilepath.toLocal8Bit()).decode('gbk').encode('utf8') )[0], ".csv")
            
            # at least one tab in csv. we just use the first tab to export csv. and ignore the later tabs.
            if len(data)>0:
                i = 0
                for itm in data:
                    csvfile = open(csvfilepath, 'wb')
                    spamwriter = csv.writer(csvfile, encoding='utf-8', delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL)
                    #csvfile.seek(0)
                    for row in data[itm]:
                        spamwriter.writerow(row)
                    csvfile.close()
                    QMessageBox.information(self,QString(u'export successful'), QString(u'csv file is exported to %s'%csvfilepath))
                    i = i+1
                    
                    # ignore the later tabs.
                    if i>0:
                        break;
                        

    def closeEvent(self, event):
        pass
        
