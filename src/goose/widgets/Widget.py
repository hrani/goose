"""Contains base class for all windows of the interface"""

from PyQt4 import Qt, QtCore, QtGui
from PyQt4.QtGui import QWidget

class Widget(QWidget):
    """Base class for all windows shown in the interface"""

    def __init__(self, model, model, application, parent, signals):
        super(Widget, self).__init__(parent)
        self._model         = model
        self._application   = application
        self._parent        = parent
        self._signals       = signals

    def show_busy(self):
        """Convey the user that the window is busy updating"""
        pass

    def show_free(self):
        """Convey the user that the window has updated.
           Called after show_busy()
        """
        pass

    def update_state(self, data):
        """Called by the main window whenever simulation data is available."""
        pass
