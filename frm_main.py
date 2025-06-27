# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QWidget)

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(654, 565)
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 661, 511))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.plus = QPushButton(self.page)
        self.plus.setObjectName(u"plus")
        self.plus.setGeometry(QRect(550, 40, 75, 51))
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 150, 49, 16))
        self.lb_Timeed = QLabel(self.page)
        self.lb_Timeed.setObjectName(u"lb_Timeed")
        self.lb_Timeed.setGeometry(QRect(0, 0, 651, 41))
        self.lb_Timeed.setTextFormat(Qt.TextFormat.AutoText)
        self.lb_Timeed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.edit_day_createF = QLineEdit(self.page_2)
        self.edit_day_createF.setObjectName(u"edit_day_createF")
        self.edit_day_createF.setGeometry(QRect(200, 140, 41, 31))
        self.button_setjetzt_createF = QPushButton(self.page_2)
        self.button_setjetzt_createF.setObjectName(u"button_setjetzt_createF")
        self.button_setjetzt_createF.setGeometry(QRect(370, 300, 101, 41))
        self.zurueck_b = QPushButton(self.page_2)
        self.zurueck_b.setObjectName(u"zurueck_b")
        self.zurueck_b.setGeometry(QRect(30, 20, 75, 51))
        self.label_day_createF = QLabel(self.page_2)
        self.label_day_createF.setObjectName(u"label_day_createF")
        self.label_day_createF.setGeometry(QRect(140, 150, 49, 16))
        self.button_starten_crateF = QPushButton(self.page_2)
        self.button_starten_crateF.setObjectName(u"button_starten_crateF")
        self.button_starten_crateF.setGeometry(QRect(177, 420, 300, 70))
        self.label_month_createF = QLabel(self.page_2)
        self.label_month_createF.setObjectName(u"label_month_createF")
        self.label_month_createF.setGeometry(QRect(140, 190, 49, 16))
        self.edit_month_createF = QLineEdit(self.page_2)
        self.edit_month_createF.setObjectName(u"edit_month_createF")
        self.edit_month_createF.setGeometry(QRect(200, 180, 41, 31))
        self.label_year_createF = QLabel(self.page_2)
        self.label_year_createF.setObjectName(u"label_year_createF")
        self.label_year_createF.setGeometry(QRect(140, 230, 49, 16))
        self.edit_year_createF = QLineEdit(self.page_2)
        self.edit_year_createF.setObjectName(u"edit_year_createF")
        self.edit_year_createF.setGeometry(QRect(200, 230, 41, 31))
        self.label_second_createF = QLabel(self.page_2)
        self.label_second_createF.setObjectName(u"label_second_createF")
        self.label_second_createF.setGeometry(QRect(330, 150, 61, 16))
        self.edit_minute_createF = QLineEdit(self.page_2)
        self.edit_minute_createF.setObjectName(u"edit_minute_createF")
        self.edit_minute_createF.setGeometry(QRect(390, 180, 41, 31))
        self.label_minute_createF = QLabel(self.page_2)
        self.label_minute_createF.setObjectName(u"label_minute_createF")
        self.label_minute_createF.setGeometry(QRect(330, 190, 49, 16))
        self.edit_hour_createF = QLineEdit(self.page_2)
        self.edit_hour_createF.setObjectName(u"edit_hour_createF")
        self.edit_hour_createF.setGeometry(QRect(390, 230, 41, 31))
        self.edit_second_createF = QLineEdit(self.page_2)
        self.edit_second_createF.setObjectName(u"edit_second_createF")
        self.edit_second_createF.setGeometry(QRect(390, 140, 41, 31))
        self.label_hour_createF = QLabel(self.page_2)
        self.label_hour_createF.setObjectName(u"label_hour_createF")
        self.label_hour_createF.setGeometry(QRect(330, 230, 49, 16))
        self.button_setheute_createF = QPushButton(self.page_2)
        self.button_setheute_createF.setObjectName(u"button_setheute_createF")
        self.button_setheute_createF.setGeometry(QRect(180, 300, 101, 41))
        self.stackedWidget.addWidget(self.page_2)
        frm_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 654, 23))
        frm_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main)
        self.statusbar.setObjectName(u"statusbar")
        frm_main.setStatusBar(self.statusbar)

        self.retranslateUi(frm_main)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"MainWindow", None))
        self.plus.setText(QCoreApplication.translate("frm_main", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("frm_main", u"TextLabel", None))
        self.lb_Timeed.setText(QCoreApplication.translate("frm_main", u"Timeed", None))
        self.button_setjetzt_createF.setText(QCoreApplication.translate("frm_main", u"Jetzt", None))
        self.zurueck_b.setText(QCoreApplication.translate("frm_main", u"Zur\u00fcck", None))
        self.label_day_createF.setText(QCoreApplication.translate("frm_main", u"Tag:", None))
        self.button_starten_crateF.setText(QCoreApplication.translate("frm_main", u"Timer Starten", None))
        self.label_month_createF.setText(QCoreApplication.translate("frm_main", u"Monat:", None))
        self.label_year_createF.setText(QCoreApplication.translate("frm_main", u"Jahr:", None))
        self.label_second_createF.setText(QCoreApplication.translate("frm_main", u"Sekunde:", None))
        self.label_minute_createF.setText(QCoreApplication.translate("frm_main", u"Minute:", None))
        self.label_hour_createF.setText(QCoreApplication.translate("frm_main", u"Stunde:", None))
        self.button_setheute_createF.setText(QCoreApplication.translate("frm_main", u"Heute", None))
    # retranslateUi

