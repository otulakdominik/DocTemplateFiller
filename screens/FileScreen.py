import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QCheckBox, QPushButton, QMessageBox


class FileScreen(QWidget):
    def __init__(self, on_selection_changed):
        """
        :param on_selection_changed: function run when checbox change.
        """
        super().__init__()
        self.folder_path = 'doc_files'
        self.on_selection_changed = on_selection_changed
        self.selected_files = []

        layout = QVBoxLayout(self)

        self.file_list_widget = QListWidget(self)
        layout.addWidget(self.file_list_widget)

        self.load_files()

    def load_files(self):
        """Load files from dictionary and add them to list."""
        if not os.path.exists(self.folder_path):
            QMessageBox.critical(self, "Error", f"Folder '{self.folder_path}' does not exist.")
            return

        files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
        if not files:
            QMessageBox.information(self, "No Files", "The folder is empty.")
            return

        for file_name in files:
            item = QListWidgetItem(self.file_list_widget)
            checkbox = QCheckBox(file_name)
            checkbox.stateChanged.connect(self.update_selected_files)
            self.file_list_widget.setItemWidget(item, checkbox)

    def update_selected_files(self):
        """Update list of files."""
        self.selected_files = []
        for i in range(self.file_list_widget.count()):
            item = self.file_list_widget.item(i)
            widget = self.file_list_widget.itemWidget(item)
            if isinstance(widget, QCheckBox) and widget.isChecked():
                self.selected_files.append(widget.text())
        
        self.on_selection_changed(self.selected_files)
