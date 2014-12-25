#! /usr/bin/env python
#http://stackoverflow.com/questions/11513132/embedding-ipython-qt-console-in-a-pyqt-application/11525205#11525205
# http://stackoverflow.com/questions/11513132/embedding-ipython-qt-console-in-a-pyqt-application/11940456#11940456
\
import sys
from goose.config import *
from goose.MainWindow import MainWindow
from PyQt4 import Qt, QtCore, QtGui
from PyQt4.QtGui import *

def main():
    application    = QtGui.QApplication(sys.argv)
    application.setWindowIcon(QIcon(APPLICATION_ICON_PATH))
    window =  MainWindow(application, sys.argv[1:])
    window.setWindowState(QtCore.Qt.WindowMaximized)
    window.show()
    sys.exit(application.exec_())

main()
# QtGui.qApp = app
#     icon = QtGui.QIcon(os.path.join(config.KEY_ICON_DIR,'moose_icon.png'))
#     app.setWindowIcon(icon)
#     # instantiate the main window
#     #moose.loadModel('../Demos/Genesis_files/Kholodenko.g','/kho')
    # sys.excepthook = mWindow.handleException
    # start the Qt main loop execution, exiting from this script
    #http://code.google.com/p/subplot/source/browse/branches/mzViewer/PyMZViewer/mpl_custom_widget.py
    #http://eli.thegreenplace.net/files/prog_code/qt_mpl_bars.py.txt
    #http://lionel.textmalaysia.com/a-simple-tutorial-on-gui-programming-using-qt-designer-with-pyqt4.html
    #http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg13241.html
    # with the same return code of Qt application
    # config.settings[config.KEY_FIRSTTIME] = 'False' # string not boolean

