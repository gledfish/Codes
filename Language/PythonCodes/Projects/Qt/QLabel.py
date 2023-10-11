import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QLabel')
        self.setGeometry(100, 100,320, 210)

        #创建一个Qlabel
        label = QLabel('This is a QLabel widget')

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        # 展示窗口
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建 主界面
    window = MainWindow()

    # 开始事件循环
    sys.exit(app.exec())

