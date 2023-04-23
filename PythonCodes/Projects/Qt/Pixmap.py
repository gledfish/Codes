import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        self.setGeometry(1000, 1000, 3200, 2100)

        label = QLabel()
        pixmap = QPixmap(
            'nahida-dendro-3-2-official-desktop-genshin-wallpaper.png'
        )
        label.setPixmap(pixmap)

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())