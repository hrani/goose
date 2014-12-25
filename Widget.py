class Widget(QWidget):

    def __init__(self, model, application, parent, window, globals, signals, **kwargs):
        self.model = model
        self.window = window
        self.application = application
        self.globals     = globals
        self.signals     = signals

    def busy():
        pass

    def free():
        pass

    def update():
        pass
