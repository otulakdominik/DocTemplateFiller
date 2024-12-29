from PySide6.QtWidgets import (
    QVBoxLayout, QLineEdit, QWidget
)

class DataEntryTab(QWidget):
    def __init__(self, tab_name):
        """
        Subtab with form.
        :param tab_name: name of subtab.
        """
        super().__init__()
        self.tab_name = tab_name
        layout = QVBoxLayout(self)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter name")
        layout.addWidget(self.name_input)

    def get_data(self):
        """Return data from form."""
        return self.name_input.text()