from PyQt4 import QtCore, QtGui, QtSql
from winmain.winmain import MainWindow

if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
