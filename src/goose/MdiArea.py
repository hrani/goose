"""Contains multi document interface window implementation for the MainWindow.
"""
from PyQt4 import Qt, QtCore, QtGui
from PyQt4.QtGui import *
from goose.utils.config import *

class MdiArea(QMdiArea):
    """Multi Document Interface window. Allows any number of child widgets
       to be displayed in tiled or tabified manner.
    """
    def __init__(self):
        super(MdiArea, self).__init__()
        self._background_image = QImage(APPLICATION_BACKGROUND_PATH)
        self._background      = None

    def resizeEvent(self, event):
        """Called every time the window is resized.
           Resizes and shows the moose image in the background.
           Source : http://qt-project.org/faq/answer/when_setting_a_background_pixmap_for_a_widget_it_is_tiled_if_the_pixmap_is_
        """
        self._background = QImage( event.size()
                                 , QImage.Format_ARGB32_Premultiplied
                                 )
        painter = QPainter(self._background)
        painter.fillRect( self._background.rect()
                        , QColor(255, 255, 255, 255)
                        )
        scaled = self._background_image.scaled( event.size()
                                              , QtCore.Qt.KeepAspectRatio
                                              )
        scaled_rect = scaled.rect()
        scaled_rect.moveCenter(self._background.rect().center())
        painter.drawImage(scaled_rect, scaled)
        self.setBackground(QBrush(self._background))
        super(MdiArea, self).resizeEvent(event)
