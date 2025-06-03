from PySide6.QtWidgets import QApplication, QMainWindow
from frm_main import Ui_frm_main

class FrmMain(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication()

frm_main = FrmMain()

frm_main.show()
app.exec()