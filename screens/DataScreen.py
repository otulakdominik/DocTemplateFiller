from PySide6.QtWidgets import (
    QTabWidget, QVBoxLayout, QPushButton, QWidget, QInputDialog, QHBoxLayout
)

from screens.DataForm import DataEntryTab

class DataScreen(QWidget):
    def __init__(self, get_selected_files):
        """Screen with add data."""
        super().__init__()
        self.get_selected_files = get_selected_files
        layout = QVBoxLayout(self)

        self.tab_widget = QTabWidget(self)
        layout.addWidget(self.tab_widget)

        buttons_layout = QHBoxLayout()

        add_tab_button = QPushButton("Add New Tab")
        add_tab_button.clicked.connect(self.add_new_tab)
        buttons_layout.addWidget(add_tab_button)

        remove_tab_button = QPushButton("Remove Selected Tab")
        remove_tab_button.clicked.connect(self.remove_selected_tab)
        buttons_layout.addWidget(remove_tab_button)

        layout.addLayout(buttons_layout)

        send_all_button = QPushButton("Send All Data")
        send_all_button.clicked.connect(self.send_all_data)
        layout.addWidget(send_all_button)

    def add_new_tab(self):
        """Add new tab named by user or named by system."""
        tab_name, ok = QInputDialog.getText(self, "New Tab", "Enter tab name:")
        if ok and tab_name.strip():
            new_tab = DataEntryTab(tab_name.strip())
            self.tab_widget.addTab(new_tab, tab_name.strip())
        elif ok:
            default_tab_name = f"Tab {self.tab_widget.count() + 1}"
            new_tab = DataEntryTab(default_tab_name)
            self.tab_widget.addTab(new_tab, default_tab_name)
        else:
            return

    def remove_selected_tab(self):
        """Delete active bar."""
        current_index = self.tab_widget.currentIndex()
        if current_index != -1:
            self.tab_widget.removeTab(current_index)

    def send_all_data(self):
        """collect and send all data."""
        collected_data = {}
        pliki = self.get_selected_files()
        for index in range(self.tab_widget.count()):
            tab = self.tab_widget.widget(index)
            if isinstance(tab, DataEntryTab):
                collected_data[tab.tab_name] = tab.get_data()

        print("Collected Data:")
        for tab_name, data in collected_data.items():
            print(f"{tab_name}: {data}")