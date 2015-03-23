    def


    @pyqtSlot(object, str)
    def model_load(moose, filename):
        SIGNALS["pre"]["model"]["load"].emit(moose, filename)
        modelpath = moose.loadModel(filename)
        SIGNALS["post"]["model"]["load"].emit(moose, modelpath)

    @pyqtSlot(object, str)
    def model_delete(moose, modelpath):
        SIGNALS["pre"]["model"]["delete"].emit(moose, modelpath)
        moose.delete(filename)
        SIGNALS["post"]["model"]["delete"].emit(moose, modelpath)

    @pyqtSlot(object, str)
    def model_load(moose, filename):
        SIGNALS["pre"]["model"]["load"].emit(moose, filename)
        modelpath = moose.loadModel(filename)
        SIGNALS["post"]["model"]["load"].emit(moose, modelpath)

    @pyqtSlot(object, str)
    def model_delete(moose, modelpath):
        SIGNALS["pre"]["model"]["delete"].emit(moose, modelpath)
        moose.delete(filename)
        SIGNALS["post"]["model"]["delete"].emit(moose, modelpath)


    @pyqtSlot(object, str)
    def model_close(self, filename):
        pass

    @pyqtSlot(object, str)
    def model_create(self, filename):
        pass

    def setup_slots(self):




        self.signals["pre"]["model"]["new"].triggered.connect(model_new )
        self.signals["pre"]["model"]["load"].triggered.connect(model_open)
        self.signals["pre"]["model"]["load"].triggered.connect(model_open)

        self.signals["pre"]["model"]["load"].triggered.connect(open)

        self.signals["pre"]["model"]["load"].triggered.connect(open)









        def create_toggle_menu_bar_action(actions):

        def setup_hide_menu_bar_action(menubar):

            def target(action, menubar):
                if menubar.isVisible():
                    signals["pre"]["menubar"]["hide"].emit()
                    action.setText("Show Menubar")
                    signals["post"]["menubar"]["hide"].emit()
                else:
                    signals["pre"]["menubar"]["show"].emit()
                    action.setText("Hide Menubar")
                    signals["post"]["menubar"]["show"].emit()

            action = QAction("Hide Menubar", self)
            action.setToolTip("Hide the menubar")
            action.setShortcut(QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_M))
            action.setShortcutContext(QtCore.Qt.ApplicationShortcut)
            action.triggered.connect(lambda : target(action, menubar))

            return action



        def setup_full_screen_action():
            action = QAction("Fullscreen", self)
            action.setToolTip("Toggle fullscreen mode")
            action.setShortcut(QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_F11))
            action.setShortcutContext(QtCore.Qt.ApplicationShortcut)
            action.setCheckable(True)
            return action



        def create_connect_action(actions):
        def create_tile_action(actions):
        def create_tabify_action(actions):
        def create_

        self.actions["new"]         = create_new_action()
        self.actions["open"]        = create_open_action()
        self.actions["connect"]     = create_connect_action()
        self.actions["quit"]        = create_quit_action()

        self.actions["toggle_menu_bar"]             =
        self.actions["toggle_full_screen"]          =
        self.actions["tile"]                        =
        self.actions["tabify"]                      =
        self.actions["toggle_interactive_python"]   =



    def setup_actions(self):
        self.newAction
        self.openAction
        self.hideMenuBarAction
        self.fullScreenAction
        self.quitAction
        self.connectAction
        self.tileAction
        self.tabifyAction
        self.toggleTerminalAction





    def setShortcuts(self):
        fullScreenShortcut = QShortcut(QKeySequence(Qt.Qt.Key_F11), self);
        fullScreenShortcut.setContext(Qt.Qt.ApplicationShortcut)







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
        INFO("Loading : " + filename)
        # moose.loadFile()

    def unload(self, model):
        pass


#def connect(hostname, )

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



    def create_slots(self):

        @pyqtSlot(bool)
        def toggle_fullscreen_slot():
            if checked:
                self.signals["fullscreen"]["enable"].emit()
            else:
                self.signals["fullscreen"]["disable"].emit()

        @pyqtSlot(bool)
        def toggle_menubar_slot():
            if checked:
                self.signals["menubar"]["show"].emit()
            else:
                self.signals["menubar"]["hide"].emit()

        @pyqtSlot()
        def new_slot():
            if checked:
                self.signals["fullscreen"]["enable"].emit()
            else:
                self.signals["fullscreen"]["disable"].emit()

        @pyqtSlot()
        def open_slot():
            if checked:
                self.signals["menubar"]["show"].emit()
            else:
                self.signals["menubar"]["hide"].emit()

        @pyqtSlot()
        def connect_slot():


        @pyqtSlot()
        def quit_slot():
            application.exit(0)

        self.signals["new"].triggered.connect(new_slot)
        self.signals["open"].triggered.connect(open_slot)
        self.signals["connect"].triggered.connect(connect_slot)
        self.signals["quit"].triggered.connect(quit_slot)


def createFullScreenAction(parent, widget):
    """Creates an action to toggle full screen mode
    """
    def slot():
        """
        """
        if widget.isFullScreen():
            widget.showNormal()
        else:
            widget.showFullScreen()

    action = createAction("Full Screen"
                         , parent
                         , slot
                         , QKeySequence(QtCore.Qt.Key_F11)
                         )
    action.setCheckable(True)
    action.setShortcutContext(QtCore.Qt.ApplicationShortcut)
    return action
