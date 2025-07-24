
#from Cython.Build.Inline import strip_common_indent

#qt imports
from PySide6.QtWidgets import QApplication, QMainWindow
#from html5lib.constants import tagTokenTypes

from frm_main import Ui_frm_main

#sys imports
from datetime import datetime
import time
import threading
from time import sleep

#eigen imports
from validation import Validation


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


        ##update
        self.stop_run_update = False

    def go_main(self):
        self.stackedWidget.setCurrentWidget(self.page)

    def go_new(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

        #setzt timer automatisch
        self.set_time_now()
        self.set_date_today()

    def create_new(self):

        def false_input(list):
            #TODO mach ma das dann das entsprchende feld wackelt und rot wird oder so
            print("Falsche eingabe")


        in_sekunde = self.edit_second_createF.text()
        in_minute = self.edit_minute_createF.text()
        in_stunde = self.edit_hour_createF.text()
        in_tag = self.edit_day_createF.text()
        in_monat = self.edit_month_createF.text()
        in_jahr = self.edit_year_createF.text()

        date_validateion = Validation(in_jahr, in_monat, in_tag, in_stunde, in_minute, in_sekunde)

        if date_validateion.false_time_list:
            false_input(date_validateion.false_time_list)

        #TODO
        # timer erstellt datei und grafik
        # timer auf main frame anzeigen
        # zähler logig bauen





    def set_time_now(self):

        def update_timer():
            while True:

                new_sek = str(datetime.now().second)
                new_min = str(datetime.now().minute)
                self.edit_second_createF.setText(new_sek)
                self.edit_minute_createF.setText(new_min)
                sleep(1)
                if self.edit_minute_createF.text() != new_min or self.edit_second_createF.text() != new_sek:
                    break
                if self.stop_run_update:
                    break


        time_update_thread = threading.Thread(target=update_timer)
        time_update_thread.start()


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


if __name__ == "__main__":

    app = QApplication()
    frm_main = FrmMain()

    frm_main.show()
    app.exec()