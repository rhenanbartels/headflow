import os

import numpy
import pyqtgraph as pg
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QApplication, QFileDialog, QGroupBox, QMainWindow, QVBoxLayout

from toolbox import read_file


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.geometry()
        geo.moveCenter(center)
        self.setGeometry(geo)
        width, height = self.screen().size().toTuple()
        self.resize(width, height)

        app.setStyleSheet("QMainWindow{background-color: black;border: 1px solid black;}")

        self.setWindowTitle("Headflow")

        # Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")

        # Open file
        open_file_action = file_menu.addAction("Open")
        open_file_action.triggered.connect(self.open_file)
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(lambda: self.app.quit())

        # Init config variables
        self.dir = None

        # Main layout
        self.obj1 = pg.PlotWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.obj1)
        box = QGroupBox(self)
        box.setLayout(layout)
        self.setCentralWidget(box)

    def open_file(self):
        self.file_full_path, _ = QFileDialog.getOpenFileName(
            self, dir=self.dir or "", caption="Open file", filter="Text files (*.txt)"
        )
        if self.file_full_path:
            self.dir = os.path.dirname(self.file_full_path)
            self.file_name = os.path.basename(self.file_full_path)

            self.data = read_file(self.file_full_path)
            self.obj1.plot(numpy.cumsum(self.data), self.data, pen=pg.mkPen(color=(0, 255, 0)))
