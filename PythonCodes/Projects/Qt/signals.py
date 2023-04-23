import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QLabel
)

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 设置窗口标题
        self.setWindowTitle('signals & sLots')

        # 创建按钮
        button = QPushButton('Click me')
        button.clicked.connect(self.button_clicked)

        # 创建标签
        label = QLabel()
        line_edit = QLineEdit()
        line_edit.textChanged.connect(label.setText)
        # 使用垂直盒模型放置按钮
        layout = QVBoxLayout()

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)
        # 展示窗口
        self.show()

    def button_clicked(self):
        print('clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
        