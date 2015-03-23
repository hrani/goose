from PyQt4 import QtGui, QtCore
import MainWindow
import sys
a = 23



class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.textEdit = QtGui.QTextEdit()

        but1 = QtGui.QPushButton('write')
        but1.clicked.connect(self.but_write)

        but2 = QtGui.QPushButton('read')
        but2.clicked.connect(self.but_read)

        self.a = {'text': ''}
        self.console = EmbedIPython()#testing=123, a=globals())
        self.console.kernel.shell.run_cell('%pylab qt')

        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        vbox.addWidget(self.textEdit)
        vbox.addWidget(self.console)
        hbox.addWidget(but1)
        hbox.addWidget(but2)
        vbox.addLayout(hbox)

        b = QtGui.QWidget()
        b.setLayout(vbox)
        self.setCentralWidget(b)

    def but_read(self):
        self.a['text'] = self.textEdit.toPlainText()
        self.console.execute("print('a[\\\'text\\\'] = \"'+ a['text'] +'\"')")

    def but_write(self):
        self.textEdit.setText(str(self.console.kernel.user_ns))


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
