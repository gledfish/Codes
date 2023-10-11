import sys
from multiprocessing import Process, Pipe
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton


class Receiver(QThread):
    messageReceived = pyqtSignal(str)

    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def run(self):
        while True:
            if self.conn.poll():
                msg = self.conn.recv()
                self.messageReceived.emit(msg)

# 图形化界面
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('聊天')
        self.setGeometry(100, 100, 500, 500)

        self.chatHistory = QTextEdit()
        self.chatHistory.setReadOnly(True)

        self.chatInput = QLineEdit()

        self.sendButton = QPushButton('发送')
        self.sendButton.clicked.connect(self.sendMessage)

        inputLayout = QHBoxLayout()
        inputLayout.addWidget(self.chatInput)
        inputLayout.addWidget(self.sendButton)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.chatHistory)
        mainLayout.addLayout(inputLayout)

        self.setLayout(mainLayout)

    def sendMessage(self):
        message = self.chatInput.text()
        self.chatInput.clear()
        self.chatHistory.append('Parent: {}'.format(message))
        self.conn.send(message)

    def receiveMessage(self, message):
        self.chatHistory.append('Child: {}'.format(message))

    def setConnection(self, conn):
        self.conn = conn
        self.receiver = Receiver(self.conn)
        self.receiver.messageReceived.connect(self.receiveMessage)
        self.receiver.start()

# 子进程
def child(conn):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setConnection(conn)
    window.show()
    app.exec_()
    conn.close()

# 父进程
def parent():
    parent_conn, child_conn = Pipe()
    child_process = Process(target=child, args=(child_conn, ))
    child_process.start()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setConnection(parent_conn)
    window.show()
    app.exec_()

    child_process.terminate()
    parent_conn.close()
    child_conn.close()

# 主程序
if __name__ == '__main__':
    parent()
