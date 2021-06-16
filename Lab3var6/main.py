import logging
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from main_window import MainWindow


class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = MainWindow()
        self.ui.setup_ui(self)


def main():
    logging.getLogger().setLevel(logging.INFO)
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()