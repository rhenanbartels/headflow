import os

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

from toolbox import read_file


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setWindowTitle("Headflow")

        # Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")

        # Open file
        open_file_action = file_menu.addAction("Open")
        open_file_action.triggered.connect(self.open_file)

        # Init config variables
        self.dir = None

    def open_file(self):
        self.file_full_path, _ = QFileDialog.getOpenFileName(
            self,
            dir=self.dir or "",
            caption="Open file",
            filter="Text files (*.txt)"
        )
        if self.file_full_path:
            self.dir = os.path.dirname(self.file_full_path)
            self.file_name = os.path.basename(self.file_full_path)
            self.data = read_file(self.file_full_path)
            print(self.data)
