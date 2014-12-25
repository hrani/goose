import sys
from goose.IPythonConsole import IPythonConsole
from PyQt4 import Qt, QtCore, QtGui
from PyQt4.QtGui import *
from goose.config import *
from goose.MdiArea import MdiArea
# print(QtCore.PYQT_VERSION_STR)

class MainWindow(QMainWindow):
    def __init__(self, application, models):
        super(MainWindow, self).__init__()
        self.setWindowFlags( self.windowFlags()
                           # | QtCore.Qt.WindowContextHelpButtonHint
                           # | QtCore.Qt.CustomizeWindowHint
                           | QtCore.Qt.WindowMinimizeButtonHint
                           | QtCore.Qt.WindowMaximizeButtonHint
                           )
        self.application = application
        self.centralWidget = self.getCentralWidget()
        (self.toolbar, self.menus) = self.getMenuBar()
        self.setup()
        # self.addToolBar(self.toolbar)
        # self.menuBar       = self.getMenuBar()

        self.setCentralWidget(self.centralWidget)
        # self.centralWidget.tileSubWindows()
        self.centralWidget.setViewMode(QMdiArea.TabbedView)
        self.centralWidget.setDocumentMode(True)
        # self.setWindowState(QtCore.Qt.WindowFullScreen)
        # self.showFullScreen()
        [self.load(model) for model in models]

    def getMenuBar(self):
        menubar = self.menuBar()

        # toolbar = QToolBar("Main", self)
        menus = { "file"    : menubar.addMenu("File")
                , "view"    : menubar.addMenu("View")
                , "widgets" : menubar.addMenu("Widgets")
                , "help"    : menubar.addMenu("Help")
                }
        # menu = QMenu()
        # menu.addAction("a")
        # menu.addAction("b")
        # menu.addAction("c")
        # menus["file"].setMenu(menu)
        menus["view"].addAction(createFullScreenAction(menubar, self))
        menus["view"].addAction(createHideMenuBarAction(menubar, menubar))

        # fullscreen.triggered.connect(self.showFullScreen)
        return (menubar, menus)

    def setup(self):
        self.setWindowTitle("Moose")
        self.setDockOptions( QMainWindow.AnimatedDocks
                           | QMainWindow.AllowNestedDocks
                           | QMainWindow.AllowTabbedDocks
                           | QMainWindow.ForceTabbedDocks
                           | QMainWindow.VerticalTabs
                           )
        self.setWindowIcon(QIcon(APPLICATION_ICON_PATH))
        self.setAcceptDrops(True)

    def getCentralWidget(self):
        centralWidget = MdiArea()
        # background = QBrush( QColor(255, 255, 255, 255)
        #                    , QPixmap(APPLICATION_BACKGROUND_PATH)
        #                    )
        # # background.setColor()
        # centralWidget.setBackground(background)
        w = IPythonConsole(globals())
        w.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        centralWidget.addSubWindow(w)
        centralWidget.addSubWindow(IPythonConsole(globals()))
        centralWidget.addSubWindow(IPythonConsole(globals()))
        return centralWidget

# http://stackoverflow.com/questions/8568500/pyqt-getting-file-name-for-file-dropped-in-app

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile().toLocal8Bit().data()
            if os.path.isfile(path):
                print path

    def load(self, filename):
        INFO("Loading -> " + filename)

    def unload(self, model):
        pass

def createAction(name, parent, slot, shortcut = None):
    action = QAction(name, parent)
    action.triggered.connect(slot)
    if shortcut is not None:
        action.setShortcut(shortcut)
    return action


def createHideMenuBarAction(parent, menubar):
    def slot():
        if menubar.isVisible():
            menubar.hide()
        else:
            menubar.show()

    action = createAction( "Hide MenuBar"
                         , parent
                         , slot
                         , QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_M)
                         )
    action.setCheckable(True)
    action.setShortcutContext(QtCore.Qt.ApplicationShortcut)
    return action



def createFullScreenAction(parent, widget):
    def slot():
        if widget.isFullScreen():
            widget.showNormal()
        else:
            widget.showFullScreen()

    action = createAction( "Full Screen"
                         , parent
                         , slot
                         , QKeySequence(QtCore.Qt.Key_F11)
                         )
    action.setCheckable(True)
    action.setShortcutContext(QtCore.Qt.ApplicationShortcut)
    return action
