from PySide6.QtWidgets import QApplication, QMainWindow
from frm_main import Ui_frm_main

class FrmMain(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stackedWidget.setCurrentWidget(self.page)

        self.zurueck_b.clicked.connect(self.go_main)
        self.plus.clicked.connect(self.go_new)

    def go_main(self):
        self.stackedWidget.setCurrentWidget(self.page)

    def go_new(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

app = QApplication()

frm_main = FrmMain()

frm_main.show()
app.exec()