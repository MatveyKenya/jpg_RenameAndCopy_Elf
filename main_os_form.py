# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_os_form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(428, 397)
        self.path_glob = QAction(MainWindow)
        self.path_glob.setObjectName(u"path_glob")
        self.path_local = QAction(MainWindow)
        self.path_local.setObjectName(u"path_local")
        self.instruction_pr = QAction(MainWindow)
        self.instruction_pr.setObjectName(u"instruction_pr")
        self.about_pr = QAction(MainWindow)
        self.about_pr.setObjectName(u"about_pr")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushB_new = QPushButton(self.centralwidget)
        self.pushB_new.setObjectName(u"pushB_new")
        self.pushB_new.setGeometry(QRect(20, 140, 391, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 141, 20))
        self.dateE_dost = QDateEdit(self.centralwidget)
        self.dateE_dost.setObjectName(u"dateE_dost")
        self.dateE_dost.setGeometry(QRect(170, 20, 101, 22))
        self.dateE_dost.setCalendarPopup(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 151, 16))
        self.lineE_number = QLineEdit(self.centralwidget)
        self.lineE_number.setObjectName(u"lineE_number")
        self.lineE_number.setGeometry(QRect(170, 60, 101, 26))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineE_number.setFont(font)
        self.lineE_fio = QLineEdit(self.centralwidget)
        self.lineE_fio.setObjectName(u"lineE_fio")
        self.lineE_fio.setGeometry(QRect(110, 95, 161, 28))
        self.lineE_fio.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 100, 121, 16))
        self.pushB_rename = QPushButton(self.centralwidget)
        self.pushB_rename.setObjectName(u"pushB_rename")
        self.pushB_rename.setGeometry(QRect(20, 250, 201, 23))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 230, 47, 13))
        self.dateE_dost_new = QDateEdit(self.centralwidget)
        self.dateE_dost_new.setObjectName(u"dateE_dost_new")
        self.dateE_dost_new.setGeometry(QRect(110, 290, 110, 22))
        self.dateE_dost_new.setCalendarPopup(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 290, 71, 16))
        self.dateE_got = QDateEdit(self.centralwidget)
        self.dateE_got.setObjectName(u"dateE_got")
        self.dateE_got.setGeometry(QRect(310, 30, 101, 22))
        self.dateE_got.setCalendarPopup(True)
        self.checkB_got = QCheckBox(self.centralwidget)
        self.checkB_got.setObjectName(u"checkB_got")
        self.checkB_got.setGeometry(QRect(310, 10, 111, 17))
        self.checkB_north = QCheckBox(self.centralwidget)
        self.checkB_north.setObjectName(u"checkB_north")
        self.checkB_north.setGeometry(QRect(310, 60, 101, 17))
        self.pushB_close = QPushButton(self.centralwidget)
        self.pushB_close.setObjectName(u"pushB_close")
        self.pushB_close.setGeometry(QRect(270, 330, 141, 23))
        self.label_path_glob = QLabel(self.centralwidget)
        self.label_path_glob.setObjectName(u"label_path_glob")
        self.label_path_glob.setGeometry(QRect(20, 170, 391, 16))
        self.label_path_local = QLabel(self.centralwidget)
        self.label_path_local.setObjectName(u"label_path_local")
        self.label_path_local.setGeometry(QRect(20, 190, 391, 16))
        self.pushB_open_jpg = QPushButton(self.centralwidget)
        self.pushB_open_jpg.setObjectName(u"pushB_open_jpg")
        self.pushB_open_jpg.setGeometry(QRect(310, 92, 101, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 428, 21))
        self.menu_cfg = QMenu(self.menubar)
        self.menu_cfg.setObjectName(u"menu_cfg")
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_cfg.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_cfg.addAction(self.path_glob)
        self.menu_cfg.addAction(self.path_local)
        self.menu_about.addAction(self.instruction_pr)
        self.menu_about.addAction(self.about_pr)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 jpg", None))
        self.path_glob.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0421\u0435\u0440\u0432\u0435\u0440\u0443 \u0441\u043a\u0430\u043d\u043e\u0432", None))
        self.path_local.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u0430\u043f\u043a\u0435 \u0441\u043a\u0430\u043d\u043e\u0432", None))
        self.instruction_pr.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.about_pr.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0435", None))
        self.pushB_new.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b jpg \u0432 (\u0434\u0430\u0442\u0430 \u2116 \u0424\u0418\u041e-01)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u043a\u0430\u0437\u0430   (\u0445\u0445\u0445/\u0445)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438 (\u043e\u0442\u0433\u0440\u0443\u0437\u043a\u0438)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None))
        self.pushB_rename.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u0437\u0430\u043a\u0430\u0437", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041b\u0418", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0434\u0430\u0442\u0430", None))
        self.checkB_got.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0430\u0442\u0430 \u0433\u043e\u0442\u043e\u0432\u043d\u043e\u0441\u0442\u0438", None))
        self.checkB_north.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0432\u0435\u0440 (\u0421)", None))
        self.pushB_close.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label_path_glob.setText(QCoreApplication.translate("MainWindow", u"label_path_glob", None))
        self.label_path_local.setText(QCoreApplication.translate("MainWindow", u"label_path_local", None))
        self.pushB_open_jpg.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043a\u0440\u044b\u0442\u044c JPG", None))
        self.menu_cfg.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi
