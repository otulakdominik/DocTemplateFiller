from PySide6.QtWidgets import QApplication, QWidget

import sys

from screens.main_window import MainWindow


app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()
