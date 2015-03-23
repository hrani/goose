import rpyc
import os
import time
from threading import Thread
from PyQt4 import QtGui
from PyQt4.QtGui import *
import sys
from threading import Thread

class CoolWidget(QTextEdit):   # exposing names is not limited to methods :)
    def __init__(self, host, port):
        super(QTextEdit,self).__init__()
        connection = rpyc.classic.connect(host, port)

    def update(self):
        super(self, QTextEdit).update()
        print(connection)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    print(sys.argv)
    w = CoolWidget(sys.argv[0], sys.argv[1])
    w.show()
    sys.exit(app.exec_())
    # from rpyc.utils.server import ThreadedServer
    # ThreadedServer(CoolService, port = 18871).start()
