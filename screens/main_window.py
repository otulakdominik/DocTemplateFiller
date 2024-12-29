from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QMainWindow, QToolBar, QTabWidget

from screens.DataScreen import DataScreen
from screens.FileScreen import FileScreen


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.selected_files = []
        self.setWindowTitle("DocTemplateFiller")

        self.tab_widget = QTabWidget(self)
        self.tab_widget.addTab(DataScreen(self.get_selected_files), 'Dane')
        self.tab_widget.addTab(FileScreen(self.set_selected_files), 'Pliki')
        self.setCentralWidget(self.tab_widget)

    def set_selected_files(self, files):
        """Set files to list."""
        self.selected_files = files

    def get_selected_files(self):
        """Get files form list."""
        return self.selected_files