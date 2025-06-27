
#qt imports
from PySide6.QtWidgets import QApplication, QMainWindow
from frm_main import Ui_frm_main

#sys imports
from datetime import datetime


class FrmMain(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stackedWidget.setCurrentWidget(self.page)


        self.plus.clicked.connect(self.go_new)

        #new frame
        self.zurueck_b.clicked.connect(self.go_main)
        self.button_starten_crateF.clicked.connect(self.create_new)
        self.button_setjetzt_createF.clicked.connect(self.set_time_now)
        self.button_setheute_createF.clicked.connect(self.set_date_today)

    def go_main(self):
        self.stackedWidget.setCurrentWidget(self.page)

    def go_new(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

        #setzt timer automatisch
        self.set_time_now()
        self.set_date_today()

    def create_new(self):
        pass


    def set_time_now(self):

        aktuelle_zeit = str(datetime.now())
        aktuelle_sek = str(datetime.now().second)
        aktuelle_min = str(datetime.now().minute)
        aktuelle_hor = str(datetime.now().hour)

        self.edit_second_createF.setText(aktuelle_sek)
        self.edit_minute_createF.setText(aktuelle_min)
        self.edit_hour_createF.setText(aktuelle_hor)

        #self.time_in.setText(aktuelle_zeit)

    def set_date_today(self):
        aktuelles_datum = str(datetime.now().date())
        aktueller_tag = str(datetime.now().day)
        aktueller_montat= str(datetime.now().month)
        aktuelles_jahr = str(datetime.now().year)

        self.edit_day_createF.setText(aktueller_tag)
        self.edit_month_createF.setText(aktueller_montat)
        self.edit_year_createF.setText(aktuelles_jahr)

#TODO validierung für die eingabe hinzufügen; evtl so ne kleine shake animation wenn was nd passt und frabe oder so



app = QApplication()

frm_main = FrmMain()

frm_main.show()
app.exec()