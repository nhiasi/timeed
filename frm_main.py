# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
        self.time_in = QLineEdit(self.page_2)
        self.time_in.setObjectName(u"time_in")
        self.time_in.setGeometry(QRect(220, 80, 161, 31))
        self.jetzt_b = QPushButton(self.page_2)
        self.jetzt_b.setObjectName(u"jetzt_b")
        self.jetzt_b.setGeometry(QRect(260, 130, 75, 24))
        self.zurueck_b = QPushButton(self.page_2)
        self.zurueck_b.setObjectName(u"zurueck_b")
        self.zurueck_b.setGeometry(QRect(30, 20, 75, 51))
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 310, 49, 16))
        self.stackedWidget.addWidget(self.page_2)
        frm_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 654, 33))
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
        self.jetzt_b.setText(QCoreApplication.translate("frm_main", u"Jetzt", None))
        self.zurueck_b.setText(QCoreApplication.translate("frm_main", u"Zur\u00fcck", None))
        self.label_2.setText(QCoreApplication.translate("frm_main", u"TextLabel", None))
    # retranslateUi

