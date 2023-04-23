import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QPushButton Widget')
        self.setGeometry(100, 100, 320, 210)

        button = QPushButton('Delete')
        button.setIcon(QIcon('nahida-dendro-3-2-official-desktop-genshin-wallpaper.png'))
        button.clicked.connect(self.on_clicked)
        button.setFixedSize(QSize(100, 30))

        # 放置按钮
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

        # 展示界面
        self.show()

    def on_clicked(self):
        print('deleted')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建 main 窗口
    window = MainWindow()

    # 开始事件循环
    sys.exit(app.exec())
