from PyQt6.QtWidgets import QApplication, QWidget
import sys

# app = QApplication(sys.argv)

# window = QWidget(windowTitle='Hello World')
# window.show()

# sys.exit(app.exec_())

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Hello World')

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
