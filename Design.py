# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 871, 655))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"background: #F9F9F9;\n"
"border: 1px solid #C4C4C3;\n"
"min-width: 20ex;\n"
"padding: 7px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: #F9F9F9;\n"
"}\n"
"QTabBar::tab:selected {\n"
"background: white;\n"
"border-bottom: 0px solid #C2C7CB;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 3px; /* make non-selected tabs look smaller */\n"
"border-left:0px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.img_diger_daire = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_daire.setGeometry(QtCore.QRect(20, 50, 241, 191))
        self.img_diger_daire.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_daire.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_daire.setObjectName("img_diger_daire")
        self.img_diger_rotate = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_rotate.setGeometry(QtCore.QRect(310, 50, 241, 191))
        self.img_diger_rotate.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_rotate.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_rotate.setObjectName("img_diger_rotate")
        self.img_diger_sekiller = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_sekiller.setGeometry(QtCore.QRect(600, 50, 241, 191))
        self.img_diger_sekiller.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_sekiller.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_sekiller.setObjectName("img_diger_sekiller")
        self.btn_diger_daire = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_daire.setGeometry(QtCore.QRect(20, 250, 241, 31))
        self.btn_diger_daire.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_daire.setObjectName("btn_diger_daire")
        self.btn_diger_rotate_sol = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_rotate_sol.setGeometry(QtCore.QRect(310, 250, 51, 31))
        self.btn_diger_rotate_sol.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_rotate_sol.setObjectName("btn_diger_rotate_sol")
        self.btn_diger_rotate_sag = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_rotate_sag.setGeometry(QtCore.QRect(360, 250, 51, 31))
        self.btn_diger_rotate_sag.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_rotate_sag.setObjectName("btn_diger_rotate_sag")
        self.btn_diger_rotate_yansima = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_rotate_yansima.setGeometry(QtCore.QRect(470, 250, 81, 31))
        self.btn_diger_rotate_yansima.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_rotate_yansima.setObjectName("btn_diger_rotate_yansima")
        self.btn_diger_rotate_ters = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_rotate_ters.setGeometry(QtCore.QRect(410, 250, 51, 31))
        self.btn_diger_rotate_ters.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_rotate_ters.setObjectName("btn_diger_rotate_ters")
        self.btn_diger_sekil_bul = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_sekil_bul.setGeometry(QtCore.QRect(700, 250, 141, 31))
        self.btn_diger_sekil_bul.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_sekil_bul.setObjectName("btn_diger_sekil_bul")
        self.img_diger_sekil_2 = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_sekil_2.setGeometry(QtCore.QRect(740, 140, 91, 71))
        self.img_diger_sekil_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_sekil_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_sekil_2.setObjectName("img_diger_sekil_2")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(740, 220, 91, 16))
        self.label.setStyleSheet("\n"
"border:1px solid gray;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btn_diger_sekiller_yukle = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_sekiller_yukle.setGeometry(QtCore.QRect(600, 250, 41, 31))
        self.btn_diger_sekiller_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_sekiller_yukle.setObjectName("btn_diger_sekiller_yukle")
        self.btn_diger_sekil_yukle = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_sekil_yukle.setGeometry(QtCore.QRect(650, 250, 41, 31))
        self.btn_diger_sekil_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_sekil_yukle.setObjectName("btn_diger_sekil_yukle")
        self.label_44 = QtWidgets.QLabel(self.tab_4)
        self.label_44.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.tab_4)
        self.label_45.setGeometry(QtCore.QRect(310, 20, 151, 16))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.tab_4)
        self.label_46.setGeometry(QtCore.QRect(600, 20, 101, 16))
        self.label_46.setObjectName("label_46")
        self.img_diger_resim_olustur = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_resim_olustur.setGeometry(QtCore.QRect(20, 350, 241, 161))
        self.img_diger_resim_olustur.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_resim_olustur.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_resim_olustur.setObjectName("img_diger_resim_olustur")
        self.btn_diger_resim_olustur = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_resim_olustur.setGeometry(QtCore.QRect(20, 520, 241, 31))
        self.btn_diger_resim_olustur.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_resim_olustur.setObjectName("btn_diger_resim_olustur")
        self.label_47 = QtWidgets.QLabel(self.tab_4)
        self.label_47.setGeometry(QtCore.QRect(20, 320, 101, 16))
        self.label_47.setObjectName("label_47")
        self.img_diger_tom_jery_1 = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_tom_jery_1.setGeometry(QtCore.QRect(310, 350, 241, 161))
        self.img_diger_tom_jery_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_tom_jery_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_tom_jery_1.setObjectName("img_diger_tom_jery_1")
        self.label_48 = QtWidgets.QLabel(self.tab_4)
        self.label_48.setGeometry(QtCore.QRect(310, 320, 161, 16))
        self.label_48.setObjectName("label_48")
        self.btn_diger_tom_jery_uygula = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_tom_jery_uygula.setGeometry(QtCore.QRect(310, 520, 241, 31))
        self.btn_diger_tom_jery_uygula.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_tom_jery_uygula.setObjectName("btn_diger_tom_jery_uygula")
        self.img_diger_tom = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_tom.setGeometry(QtCore.QRect(310, 450, 101, 61))
        self.img_diger_tom.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_tom.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_tom.setObjectName("img_diger_tom")
        self.img_diger_jery = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_jery.setGeometry(QtCore.QRect(450, 450, 101, 61))
        self.img_diger_jery.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_jery.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_jery.setObjectName("img_diger_jery")
        self.btn_diger_tom_yukle = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_tom_yukle.setGeometry(QtCore.QRect(390, 490, 21, 21))
        self.btn_diger_tom_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_tom_yukle.setObjectName("btn_diger_tom_yukle")
        self.btn_diger_jery_yukle = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_jery_yukle.setGeometry(QtCore.QRect(530, 490, 21, 21))
        self.btn_diger_jery_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_jery_yukle.setObjectName("btn_diger_jery_yukle")
        self.label_97 = QtWidgets.QLabel(self.tab_4)
        self.label_97.setGeometry(QtCore.QRect(600, 320, 161, 16))
        self.label_97.setObjectName("label_97")
        self.img_diger_tom_jery_arkaplan = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_tom_jery_arkaplan.setGeometry(QtCore.QRect(600, 350, 121, 81))
        self.img_diger_tom_jery_arkaplan.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_tom_jery_arkaplan.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_tom_jery_arkaplan.setObjectName("img_diger_tom_jery_arkaplan")
        self.btn_diger_arkaplan_tom_jery_uygula = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_arkaplan_tom_jery_uygula.setGeometry(QtCore.QRect(600, 520, 241, 31))
        self.btn_diger_arkaplan_tom_jery_uygula.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_arkaplan_tom_jery_uygula.setObjectName("btn_diger_arkaplan_tom_jery_uygula")
        self.img_diger_tom_jery_arkaplan_sonuc = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_tom_jery_arkaplan_sonuc.setGeometry(QtCore.QRect(600, 430, 241, 81))
        self.img_diger_tom_jery_arkaplan_sonuc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_tom_jery_arkaplan_sonuc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_tom_jery_arkaplan_sonuc.setObjectName("img_diger_tom_jery_arkaplan_sonuc")
        self.btn_diger_tom_jery_arkaplan_yukle_1 = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_tom_jery_arkaplan_yukle_1.setGeometry(QtCore.QRect(690, 400, 31, 31))
        self.btn_diger_tom_jery_arkaplan_yukle_1.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_tom_jery_arkaplan_yukle_1.setObjectName("btn_diger_tom_jery_arkaplan_yukle_1")
        self.img_diger_tom_jery_3 = QtWidgets.QGraphicsView(self.tab_4)
        self.img_diger_tom_jery_3.setGeometry(QtCore.QRect(720, 350, 121, 81))
        self.img_diger_tom_jery_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_tom_jery_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_tom_jery_3.setObjectName("img_diger_tom_jery_3")
        self.btn_diger_tom_jery_arkaplan_yukle_2 = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_tom_jery_arkaplan_yukle_2.setGeometry(QtCore.QRect(810, 400, 31, 31))
        self.btn_diger_tom_jery_arkaplan_yukle_2.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_tom_jery_arkaplan_yukle_2.setObjectName("btn_diger_tom_jery_arkaplan_yukle_2")
        self.btn_diger_rotate_yukle = QtWidgets.QPushButton(self.tab_4)
        self.btn_diger_rotate_yukle.setGeometry(QtCore.QRect(520, 210, 31, 31))
        self.btn_diger_rotate_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_diger_rotate_yukle.setObjectName("btn_diger_rotate_yukle")
        self.lbl_circle_coordinate = QtWidgets.QLabel(self.tab_4)
        self.lbl_circle_coordinate.setGeometry(QtCore.QRect(30, 60, 211, 51))
        self.lbl_circle_coordinate.setStyleSheet("color: rgb(0, 255, 127);")
        self.lbl_circle_coordinate.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_circle_coordinate.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_circle_coordinate.setLineWidth(4)
        self.lbl_circle_coordinate.setMidLineWidth(0)
        self.lbl_circle_coordinate.setText("")
        self.lbl_circle_coordinate.setWordWrap(True)
        self.lbl_circle_coordinate.setObjectName("lbl_circle_coordinate")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_load = QtWidgets.QWidget()
        self.tab_load.setObjectName("tab_load")
        self.label_4 = QtWidgets.QLabel(self.tab_load)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label_4.setObjectName("label_4")
        self.img_temel_orjinal = QtWidgets.QGraphicsView(self.tab_load)
        self.img_temel_orjinal.setGeometry(QtCore.QRect(20, 50, 411, 391))
        self.img_temel_orjinal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_orjinal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_orjinal.setObjectName("img_temel_orjinal")
        self.img_temel_sonuc = QtWidgets.QGraphicsView(self.tab_load)
        self.img_temel_sonuc.setGeometry(QtCore.QRect(450, 50, 391, 391))
        self.img_temel_sonuc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_sonuc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_sonuc.setObjectName("img_temel_sonuc")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_load)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 450, 821, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_temel_gri_cevir = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_temel_gri_cevir.setGeometry(QtCore.QRect(50, 30, 61, 31))
        self.btn_temel_gri_cevir.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_temel_gri_cevir.setObjectName("btn_temel_gri_cevir")
        self.btn_temel_sobel = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_temel_sobel.setGeometry(QtCore.QRect(210, 30, 71, 31))
        self.btn_temel_sobel.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_temel_sobel.setObjectName("btn_temel_sobel")
        self.btn_temel_hist_esitle = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_temel_hist_esitle.setGeometry(QtCore.QRect(270, 70, 141, 31))
        self.btn_temel_hist_esitle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_temel_hist_esitle.setObjectName("btn_temel_hist_esitle")
        self.btn_temel_binary_cevir = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_temel_binary_cevir.setGeometry(QtCore.QRect(120, 30, 81, 31))
        self.btn_temel_binary_cevir.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_temel_binary_cevir.setObjectName("btn_temel_binary_cevir")
        self.btn_temel_boyutlandir = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_temel_boyutlandir.setGeometry(QtCore.QRect(680, 30, 121, 31))
        self.btn_temel_boyutlandir.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_temel_boyutlandir.setObjectName("btn_temel_boyutlandir")
        self.img_temel_yukseklik = QtWidgets.QLineEdit(self.groupBox_2)
        self.img_temel_yukseklik.setGeometry(QtCore.QRect(650, 30, 31, 31))
        self.img_temel_yukseklik.setStyleSheet("padding-left:3px;")
        self.img_temel_yukseklik.setObjectName("img_temel_yukseklik")
        self.img_temel_genislik = QtWidgets.QLineEdit(self.groupBox_2)
        self.img_temel_genislik.setGeometry(QtCore.QRect(620, 30, 31, 31))
        self.img_temel_genislik.setStyleSheet("padding-left:3px;")
        self.img_temel_genislik.setObjectName("img_temel_genislik")
        self.btn_temel_yukle = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_temel_yukle.setGeometry(QtCore.QRect(10, 30, 31, 31))
        self.btn_temel_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_temel_yukle.setObjectName("btn_temel_yukle")
        self.btn_temel_treshold = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_temel_treshold.setGeometry(QtCore.QRect(50, 70, 111, 31))
        self.btn_temel_treshold.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_temel_treshold.setObjectName("btn_temel_treshold")
        self.btn_temel_canny = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_temel_canny.setGeometry(QtCore.QRect(170, 70, 91, 31))
        self.btn_temel_canny.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_temel_canny.setObjectName("btn_temel_canny")
        self.btn_temel_skeletonize = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_temel_skeletonize.setGeometry(QtCore.QRect(290, 30, 121, 31))
        self.btn_temel_skeletonize.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_temel_skeletonize.setObjectName("btn_temel_skeletonize")
        self.label_5 = QtWidgets.QLabel(self.tab_load)
        self.label_5.setGeometry(QtCore.QRect(450, 20, 101, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_load)
        self.groupBox_3.setGeometry(QtCore.QRect(460, 270, 371, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.img_temel_hist_once = QtWidgets.QGraphicsView(self.groupBox_3)
        self.img_temel_hist_once.setGeometry(QtCore.QRect(10, 20, 171, 131))
        self.img_temel_hist_once.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_hist_once.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_hist_once.setObjectName("img_temel_hist_once")
        self.img_temel_hist_sonra = QtWidgets.QGraphicsView(self.groupBox_3)
        self.img_temel_hist_sonra.setGeometry(QtCore.QRect(190, 20, 171, 131))
        self.img_temel_hist_sonra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_hist_sonra.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_hist_sonra.setObjectName("img_temel_hist_sonra")
        self.tabWidget.addTab(self.tab_load, "")
        self.tab_classes = QtWidgets.QWidget()
        self.tab_classes.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"border-top: 2px solid #C2C7CB;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"left: 5px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"border: 2px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 8ex;\n"
"padding: 2px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"QTabBar::tab:selected {\n"
"border-color: #9B9B9B;\n"
"border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.tab_classes.setObjectName("tab_classes")
        self.label_6 = QtWidgets.QLabel(self.tab_classes)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.label_6.setObjectName("label_6")
        self.img_mantiksal_a = QtWidgets.QGraphicsView(self.tab_classes)
        self.img_mantiksal_a.setGeometry(QtCore.QRect(20, 60, 261, 281))
        self.img_mantiksal_a.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_mantiksal_a.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_mantiksal_a.setObjectName("img_mantiksal_a")
        self.label_7 = QtWidgets.QLabel(self.tab_classes)
        self.label_7.setGeometry(QtCore.QRect(300, 30, 101, 16))
        self.label_7.setObjectName("label_7")
        self.btn_mantiksal_a_yukle = QtWidgets.QPushButton(self.tab_classes)
        self.btn_mantiksal_a_yukle.setGeometry(QtCore.QRect(250, 310, 31, 31))
        self.btn_mantiksal_a_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_mantiksal_a_yukle.setObjectName("btn_mantiksal_a_yukle")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_classes)
        self.groupBox_4.setGeometry(QtCore.QRect(580, 380, 261, 161))
        self.groupBox_4.setObjectName("groupBox_4")
        self.cmb_mantiksal_islemler = QtWidgets.QComboBox(self.groupBox_4)
        self.cmb_mantiksal_islemler.setGeometry(QtCore.QRect(20, 60, 221, 31))
        self.cmb_mantiksal_islemler.setStyleSheet("border:1px solid black;")
        self.cmb_mantiksal_islemler.setObjectName("cmb_mantiksal_islemler")
        self.cmb_mantiksal_islemler.addItem("")
        self.cmb_mantiksal_islemler.addItem("")
        self.cmb_mantiksal_islemler.addItem("")
        self.cmb_mantiksal_islemler.addItem("")
        self.cmb_mantiksal_islemler.addItem("")
        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setGeometry(QtCore.QRect(20, 20, 191, 31))
        self.label_36.setObjectName("label_36")
        self.btn_mantiksal_uygula = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_mantiksal_uygula.setGeometry(QtCore.QRect(20, 100, 221, 41))
        self.btn_mantiksal_uygula.setStyleSheet("border: 1px solid red;\n"
"color:red;\n"
"")
        self.btn_mantiksal_uygula.setObjectName("btn_mantiksal_uygula")
        self.btn_classes_apply_9 = QtWidgets.QPushButton(self.tab_classes)
        self.btn_classes_apply_9.setGeometry(QtCore.QRect(530, 280, 31, 31))
        self.btn_classes_apply_9.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_classes_apply_9.setObjectName("btn_classes_apply_9")
        self.img_mantiksal_b = QtWidgets.QGraphicsView(self.tab_classes)
        self.img_mantiksal_b.setGeometry(QtCore.QRect(300, 60, 261, 281))
        self.img_mantiksal_b.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_mantiksal_b.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_mantiksal_b.setObjectName("img_mantiksal_b")
        self.btn_mantiksal_b_yukle = QtWidgets.QPushButton(self.tab_classes)
        self.btn_mantiksal_b_yukle.setGeometry(QtCore.QRect(530, 310, 31, 31))
        self.btn_mantiksal_b_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_mantiksal_b_yukle.setObjectName("btn_mantiksal_b_yukle")
        self.btn_classes_apply_11 = QtWidgets.QPushButton(self.tab_classes)
        self.btn_classes_apply_11.setGeometry(QtCore.QRect(810, 280, 31, 31))
        self.btn_classes_apply_11.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_classes_apply_11.setObjectName("btn_classes_apply_11")
        self.label_8 = QtWidgets.QLabel(self.tab_classes)
        self.label_8.setGeometry(QtCore.QRect(580, 30, 101, 16))
        self.label_8.setObjectName("label_8")
        self.img_mantiksal_sonuc = QtWidgets.QGraphicsView(self.tab_classes)
        self.img_mantiksal_sonuc.setGeometry(QtCore.QRect(580, 60, 261, 281))
        self.img_mantiksal_sonuc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_mantiksal_sonuc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_mantiksal_sonuc.setObjectName("img_mantiksal_sonuc")
        self.tabWidget.addTab(self.tab_classes, "")
        self.tab_split = QtWidgets.QWidget()
        self.tab_split.setObjectName("tab_split")
        self.label_10 = QtWidgets.QLabel(self.tab_split)
        self.label_10.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.label_10.setObjectName("label_10")
        self.img_label_orjinal = QtWidgets.QGraphicsView(self.tab_split)
        self.img_label_orjinal.setGeometry(QtCore.QRect(20, 60, 411, 391))
        self.img_label_orjinal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_label_orjinal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_label_orjinal.setObjectName("img_label_orjinal")
        self.btn_labeling_yukle = QtWidgets.QPushButton(self.tab_split)
        self.btn_labeling_yukle.setGeometry(QtCore.QRect(400, 420, 31, 31))
        self.btn_labeling_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_labeling_yukle.setObjectName("btn_labeling_yukle")
        self.label_11 = QtWidgets.QLabel(self.tab_split)
        self.label_11.setGeometry(QtCore.QRect(440, 30, 101, 16))
        self.label_11.setObjectName("label_11")
        self.img_label_sonuc = QtWidgets.QGraphicsView(self.tab_split)
        self.img_label_sonuc.setGeometry(QtCore.QRect(440, 60, 411, 391))
        self.img_label_sonuc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_label_sonuc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_label_sonuc.setObjectName("img_label_sonuc")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_split)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 470, 831, 81))
        self.groupBox_5.setObjectName("groupBox_5")
        self.btn_labeling_uygula = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_labeling_uygula.setGeometry(QtCore.QRect(20, 30, 141, 31))
        self.btn_labeling_uygula.setStyleSheet("QPushButton\n"
"{\n"
"border: 1px solid red;\n"
"color:red;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_labeling_uygula.setObjectName("btn_labeling_uygula")
        self.label_37 = QtWidgets.QLabel(self.groupBox_5)
        self.label_37.setGeometry(QtCore.QRect(460, 30, 131, 31))
        self.label_37.setObjectName("label_37")
        self.cmb_label_sekiller = QtWidgets.QComboBox(self.groupBox_5)
        self.cmb_label_sekiller.setGeometry(QtCore.QRect(590, 30, 221, 31))
        self.cmb_label_sekiller.setStyleSheet("border:1px solid black;")
        self.cmb_label_sekiller.setObjectName("cmb_label_sekiller")
        self.btn_labeling_vurgula = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_labeling_vurgula.setGeometry(QtCore.QRect(180, 30, 141, 31))
        self.btn_labeling_vurgula.setStyleSheet("QPushButton\n"
"{\n"
"border: 1px solid red;\n"
"color:red;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_labeling_vurgula.setObjectName("btn_labeling_vurgula")
        self.tabWidget.addTab(self.tab_split, "")
        self.tab_performence = QtWidgets.QWidget()
        self.tab_performence.setObjectName("tab_performence")
        self.img_gurultu_sonuc = QtWidgets.QGraphicsView(self.tab_performence)
        self.img_gurultu_sonuc.setGeometry(QtCore.QRect(440, 60, 401, 391))
        self.img_gurultu_sonuc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_gurultu_sonuc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_gurultu_sonuc.setObjectName("img_gurultu_sonuc")
        self.label_12 = QtWidgets.QLabel(self.tab_performence)
        self.label_12.setGeometry(QtCore.QRect(440, 30, 101, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_performence)
        self.label_13.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.label_13.setObjectName("label_13")
        self.img_gurultu_orjinal = QtWidgets.QGraphicsView(self.tab_performence)
        self.img_gurultu_orjinal.setGeometry(QtCore.QRect(20, 60, 411, 391))
        self.img_gurultu_orjinal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_gurultu_orjinal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_gurultu_orjinal.setObjectName("img_gurultu_orjinal")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_performence)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 470, 821, 81))
        self.groupBox_6.setObjectName("groupBox_6")
        self.btn_gurultu_olustur = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_gurultu_olustur.setGeometry(QtCore.QRect(600, 30, 201, 31))
        self.btn_gurultu_olustur.setStyleSheet("QPushButton\n"
"{\n"
"border: 1px solid red;\n"
"color:red;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_gurultu_olustur.setObjectName("btn_gurultu_olustur")
        self.label_39 = QtWidgets.QLabel(self.groupBox_6)
        self.label_39.setGeometry(QtCore.QRect(10, 30, 71, 31))
        self.label_39.setObjectName("label_39")
        self.trackBar_gurultu = QtWidgets.QSlider(self.groupBox_6)
        self.trackBar_gurultu.setGeometry(QtCore.QRect(90, 30, 191, 31))
        self.trackBar_gurultu.setMaximum(100)
        self.trackBar_gurultu.setOrientation(QtCore.Qt.Horizontal)
        self.trackBar_gurultu.setObjectName("trackBar_gurultu")
        self.lbl_gurultu_oran = QtWidgets.QLabel(self.groupBox_6)
        self.lbl_gurultu_oran.setGeometry(QtCore.QRect(300, 34, 71, 21))
        self.lbl_gurultu_oran.setObjectName("lbl_gurultu_oran")
        self.btn_gurultu_yukle = QtWidgets.QPushButton(self.tab_performence)
        self.btn_gurultu_yukle.setGeometry(QtCore.QRect(400, 420, 31, 31))
        self.btn_gurultu_yukle.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_gurultu_yukle.setObjectName("btn_gurultu_yukle")
        self.tabWidget.addTab(self.tab_performence, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 20, 851, 541))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphicsView_12 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_12.setGeometry(QtCore.QRect(420, 40, 401, 361))
        self.graphicsView_12.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_12.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_12.setObjectName("graphicsView_12")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(420, 10, 101, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_15.setObjectName("label_15")
        self.graphicsView_13 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_13.setGeometry(QtCore.QRect(10, 40, 391, 361))
        self.graphicsView_13.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_13.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_13.setObjectName("graphicsView_13")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 410, 811, 81))
        self.groupBox_7.setObjectName("groupBox_7")
        self.btn_split_next_5 = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_split_next_5.setGeometry(QtCore.QRect(20, 30, 201, 31))
        self.btn_split_next_5.setStyleSheet("QPushButton\n"
"{\n"
"border: 1px solid red;\n"
"color:red;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_split_next_5.setObjectName("btn_split_next_5")
        self.label_42 = QtWidgets.QLabel(self.groupBox_7)
        self.label_42.setGeometry(QtCore.QRect(290, 30, 131, 31))
        self.label_42.setObjectName("label_42")
        self.cmb_classes_5 = QtWidgets.QComboBox(self.groupBox_7)
        self.cmb_classes_5.setGeometry(QtCore.QRect(420, 30, 201, 31))
        self.cmb_classes_5.setStyleSheet("border:1px solid black;")
        self.cmb_classes_5.setObjectName("cmb_classes_5")
        self.btn_split_next_6 = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_split_next_6.setGeometry(QtCore.QRect(640, 30, 151, 31))
        self.btn_split_next_6.setStyleSheet("QPushButton\n"
"{\n"
"border: 1px solid red;\n"
"color:red;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_split_next_6.setObjectName("btn_split_next_6")
        self.btn_classes_apply_14 = QtWidgets.QPushButton(self.tab_2)
        self.btn_classes_apply_14.setGeometry(QtCore.QRect(370, 370, 31, 31))
        self.btn_classes_apply_14.setStyleSheet("QPushButton\n"
"{\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(250, 250, 250);\n"
"}")
        self.btn_classes_apply_14.setObjectName("btn_classes_apply_14")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(-1, -1, 851, 507))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.scrollArea.setFont(font)
        self.scrollArea.setMouseTracking(False)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 832, 1700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setMouseTracking(False)
        self.scrollAreaWidgetContents.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollAreaWidgetContents.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.scrollAreaWidgetContents.setAcceptDrops(False)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_17.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.graphicsView_17 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_17.setGeometry(QtCore.QRect(580, 60, 181, 141))
        self.graphicsView_17.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_17.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_17.setObjectName("graphicsView_17")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(780, 90, 47, 21))
        self.label_3.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_3.setObjectName("label_3")
        self.graphicsView_16 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_16.setGeometry(QtCore.QRect(400, 60, 181, 141))
        self.graphicsView_16.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_16.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_16.setObjectName("graphicsView_16")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setGeometry(QtCore.QRect(580, 30, 181, 16))
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setGeometry(QtCore.QRect(780, 150, 47, 21))
        self.label_21.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_21.setObjectName("label_21")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setGeometry(QtCore.QRect(190, 30, 181, 16))
        self.label_18.setObjectName("label_18")
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setGeometry(QtCore.QRect(780, 130, 47, 13))
        self.label_22.setObjectName("label_22")
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setGeometry(QtCore.QRect(400, 30, 171, 16))
        self.label_20.setObjectName("label_20")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label_16.setObjectName("label_16")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(780, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.graphicsView_14 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_14.setGeometry(QtCore.QRect(10, 60, 181, 141))
        self.graphicsView_14.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_14.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_14.setObjectName("graphicsView_14")
        self.graphicsView_15 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_15.setGeometry(QtCore.QRect(190, 60, 181, 141))
        self.graphicsView_15.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_15.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_15.setObjectName("graphicsView_15")
        self.graphicsView_18 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_18.setGeometry(QtCore.QRect(580, 270, 181, 141))
        self.graphicsView_18.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_18.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_18.setObjectName("graphicsView_18")
        self.graphicsView_19 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_19.setGeometry(QtCore.QRect(190, 270, 181, 141))
        self.graphicsView_19.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_19.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_19.setObjectName("graphicsView_19")
        self.graphicsView_20 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_20.setGeometry(QtCore.QRect(400, 270, 181, 141))
        self.graphicsView_20.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_20.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_20.setObjectName("graphicsView_20")
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setGeometry(QtCore.QRect(10, 240, 181, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setGeometry(QtCore.QRect(580, 240, 181, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setGeometry(QtCore.QRect(10, 220, 211, 16))
        self.label_25.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setGeometry(QtCore.QRect(780, 360, 47, 21))
        self.label_26.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setGeometry(QtCore.QRect(780, 340, 47, 13))
        self.label_27.setObjectName("label_27")
        self.graphicsView_21 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_21.setGeometry(QtCore.QRect(10, 270, 181, 141))
        self.graphicsView_21.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_21.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_21.setObjectName("graphicsView_21")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(780, 300, 47, 21))
        self.label_9.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_9.setObjectName("label_9")
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setGeometry(QtCore.QRect(190, 240, 181, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setGeometry(QtCore.QRect(400, 240, 171, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setGeometry(QtCore.QRect(780, 280, 47, 13))
        self.label_30.setObjectName("label_30")
        self.graphicsView_22 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_22.setGeometry(QtCore.QRect(580, 480, 181, 141))
        self.graphicsView_22.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_22.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_22.setObjectName("graphicsView_22")
        self.graphicsView_23 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_23.setGeometry(QtCore.QRect(190, 480, 181, 141))
        self.graphicsView_23.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_23.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_23.setObjectName("graphicsView_23")
        self.graphicsView_24 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_24.setGeometry(QtCore.QRect(400, 480, 181, 141))
        self.graphicsView_24.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_24.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_24.setObjectName("graphicsView_24")
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setGeometry(QtCore.QRect(10, 450, 181, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setGeometry(QtCore.QRect(580, 450, 181, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_33.setGeometry(QtCore.QRect(10, 430, 101, 16))
        self.label_33.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setGeometry(QtCore.QRect(780, 570, 47, 21))
        self.label_34.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_35.setGeometry(QtCore.QRect(780, 550, 47, 13))
        self.label_35.setObjectName("label_35")
        self.graphicsView_25 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_25.setGeometry(QtCore.QRect(10, 480, 181, 141))
        self.graphicsView_25.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_25.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_25.setObjectName("graphicsView_25")
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setGeometry(QtCore.QRect(780, 510, 47, 21))
        self.label_38.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_38.setObjectName("label_38")
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_40.setGeometry(QtCore.QRect(190, 450, 181, 16))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_41.setGeometry(QtCore.QRect(400, 450, 171, 16))
        self.label_41.setObjectName("label_41")
        self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_43.setGeometry(QtCore.QRect(780, 490, 47, 13))
        self.label_43.setObjectName("label_43")
        self.graphicsView_26 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_26.setGeometry(QtCore.QRect(190, 690, 181, 141))
        self.graphicsView_26.setObjectName("graphicsView_26")
        self.label_49 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_49.setGeometry(QtCore.QRect(400, 660, 171, 16))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_50.setGeometry(QtCore.QRect(780, 760, 47, 13))
        self.label_50.setObjectName("label_50")
        self.graphicsView_27 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_27.setGeometry(QtCore.QRect(580, 690, 181, 141))
        self.graphicsView_27.setObjectName("graphicsView_27")
        self.label_51 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_51.setGeometry(QtCore.QRect(10, 640, 121, 16))
        self.label_51.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_51.setObjectName("label_51")
        self.graphicsView_28 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_28.setGeometry(QtCore.QRect(10, 690, 181, 141))
        self.graphicsView_28.setObjectName("graphicsView_28")
        self.label_52 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_52.setGeometry(QtCore.QRect(10, 660, 181, 16))
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_53.setGeometry(QtCore.QRect(780, 780, 47, 21))
        self.label_53.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_54.setGeometry(QtCore.QRect(780, 700, 47, 13))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_55.setGeometry(QtCore.QRect(580, 660, 181, 16))
        self.label_55.setObjectName("label_55")
        self.graphicsView_29 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_29.setGeometry(QtCore.QRect(400, 690, 181, 141))
        self.graphicsView_29.setObjectName("graphicsView_29")
        self.label_56 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_56.setGeometry(QtCore.QRect(780, 720, 47, 21))
        self.label_56.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_57.setGeometry(QtCore.QRect(190, 660, 181, 16))
        self.label_57.setObjectName("label_57")
        self.graphicsView_30 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_30.setGeometry(QtCore.QRect(190, 900, 181, 141))
        self.graphicsView_30.setObjectName("graphicsView_30")
        self.label_58 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_58.setGeometry(QtCore.QRect(400, 870, 171, 16))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_59.setGeometry(QtCore.QRect(780, 970, 47, 13))
        self.label_59.setObjectName("label_59")
        self.graphicsView_31 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_31.setGeometry(QtCore.QRect(580, 900, 181, 141))
        self.graphicsView_31.setObjectName("graphicsView_31")
        self.label_60 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_60.setGeometry(QtCore.QRect(10, 850, 221, 16))
        self.label_60.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_60.setObjectName("label_60")
        self.graphicsView_32 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_32.setGeometry(QtCore.QRect(10, 900, 181, 141))
        self.graphicsView_32.setObjectName("graphicsView_32")
        self.label_61 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_61.setGeometry(QtCore.QRect(10, 870, 181, 16))
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_62.setGeometry(QtCore.QRect(780, 990, 47, 21))
        self.label_62.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_63.setGeometry(QtCore.QRect(780, 910, 47, 13))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_64.setGeometry(QtCore.QRect(580, 870, 181, 16))
        self.label_64.setObjectName("label_64")
        self.graphicsView_33 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_33.setGeometry(QtCore.QRect(400, 900, 181, 141))
        self.graphicsView_33.setObjectName("graphicsView_33")
        self.label_65 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_65.setGeometry(QtCore.QRect(780, 930, 47, 21))
        self.label_65.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_66.setGeometry(QtCore.QRect(190, 870, 181, 16))
        self.label_66.setObjectName("label_66")
        self.graphicsView_34 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_34.setGeometry(QtCore.QRect(190, 1120, 181, 141))
        self.graphicsView_34.setObjectName("graphicsView_34")
        self.label_67 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_67.setGeometry(QtCore.QRect(400, 1090, 171, 16))
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_68.setGeometry(QtCore.QRect(780, 1190, 47, 13))
        self.label_68.setObjectName("label_68")
        self.graphicsView_35 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_35.setGeometry(QtCore.QRect(580, 1120, 181, 141))
        self.graphicsView_35.setObjectName("graphicsView_35")
        self.label_69 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_69.setGeometry(QtCore.QRect(10, 1070, 161, 16))
        self.label_69.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_69.setObjectName("label_69")
        self.graphicsView_36 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_36.setGeometry(QtCore.QRect(10, 1120, 181, 141))
        self.graphicsView_36.setObjectName("graphicsView_36")
        self.label_70 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_70.setGeometry(QtCore.QRect(10, 1090, 181, 16))
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_71.setGeometry(QtCore.QRect(780, 1210, 47, 21))
        self.label_71.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_72.setGeometry(QtCore.QRect(780, 1130, 47, 13))
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_73.setGeometry(QtCore.QRect(580, 1090, 181, 16))
        self.label_73.setObjectName("label_73")
        self.graphicsView_37 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_37.setGeometry(QtCore.QRect(400, 1120, 181, 141))
        self.graphicsView_37.setObjectName("graphicsView_37")
        self.label_74 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_74.setGeometry(QtCore.QRect(780, 1150, 47, 21))
        self.label_74.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_75.setGeometry(QtCore.QRect(190, 1090, 181, 16))
        self.label_75.setObjectName("label_75")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_diger_daire.setText(_translate("MainWindow", "D A İ R E  Ç İ Z"))
        self.btn_diger_rotate_sol.setText(_translate("MainWindow", "S O L"))
        self.btn_diger_rotate_sag.setText(_translate("MainWindow", "S A Ğ"))
        self.btn_diger_rotate_yansima.setText(_translate("MainWindow", "Y A N S I M A"))
        self.btn_diger_rotate_ters.setText(_translate("MainWindow", "T E R S"))
        self.btn_diger_sekil_bul.setText(_translate("MainWindow", "Ş E K İ L  B İ L G İ S İ"))
        self.btn_diger_sekiller_yukle.setText(_translate("MainWindow", "^"))
        self.btn_diger_sekil_yukle.setText(_translate("MainWindow", "^"))
        self.label_44.setText(_translate("MainWindow", "D a i r e  Ç i z i m i"))
        self.label_45.setText(_translate("MainWindow", "D ö n d ü r m e  İ ş l e m l e r i"))
        self.label_46.setText(_translate("MainWindow", "Ş e k i l  B u l m a"))
        self.btn_diger_resim_olustur.setText(_translate("MainWindow", "O L U Ş T U R"))
        self.label_47.setText(_translate("MainWindow", "R e s i m  O l u ş t u r"))
        self.label_48.setText(_translate("MainWindow", "T o m  v e  J e r y  B i r l e ş t i r"))
        self.btn_diger_tom_jery_uygula.setText(_translate("MainWindow", "U Y G U L A"))
        self.btn_diger_tom_yukle.setText(_translate("MainWindow", "↓"))
        self.btn_diger_jery_yukle.setText(_translate("MainWindow", "↓"))
        self.label_97.setText(_translate("MainWindow", "T o m  v e  J e r y  A r k a p l a n"))
        self.btn_diger_arkaplan_tom_jery_uygula.setText(_translate("MainWindow", "U Y G U L A"))
        self.btn_diger_tom_jery_arkaplan_yukle_1.setText(_translate("MainWindow", "↓"))
        self.btn_diger_tom_jery_arkaplan_yukle_2.setText(_translate("MainWindow", "↓"))
        self.btn_diger_rotate_yukle.setText(_translate("MainWindow", "↓"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Ö D E V L E R"))
        self.label_4.setText(_translate("MainWindow", "Orjinal Resim :"))
        self.groupBox_2.setTitle(_translate("MainWindow", "İ ş l e m l e r"))
        self.btn_temel_gri_cevir.setText(_translate("MainWindow", "G R I"))
        self.btn_temel_sobel.setText(_translate("MainWindow", "S O B E L"))
        self.btn_temel_hist_esitle.setText(_translate("MainWindow", "H I S T.  E Ş İ T L E"))
        self.btn_temel_binary_cevir.setText(_translate("MainWindow", "B I N A R Y"))
        self.btn_temel_boyutlandir.setText(_translate("MainWindow", "B O Y U T L A N D I R"))
        self.img_temel_yukseklik.setText(_translate("MainWindow", "10"))
        self.img_temel_genislik.setText(_translate("MainWindow", "10"))
        self.btn_temel_yukle.setText(_translate("MainWindow", "↓"))
        self.btn_temel_treshold.setText(_translate("MainWindow", "T R E S H O L D"))
        self.btn_temel_canny.setText(_translate("MainWindow", "C A N N Y"))
        self.btn_temel_skeletonize.setText(_translate("MainWindow", "S K E L E T O N I Z E"))
        self.label_5.setText(_translate("MainWindow", "İşlemler (resim) :"))
        self.groupBox_3.setTitle(_translate("MainWindow", "H i s t o g r a m - Ö n c e / S o n r a"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_load), _translate("MainWindow", "T E M E L"))
        self.label_6.setText(_translate("MainWindow", "Resim (a)"))
        self.label_7.setText(_translate("MainWindow", "Resim (b)"))
        self.btn_mantiksal_a_yukle.setText(_translate("MainWindow", "↓"))
        self.groupBox_4.setTitle(_translate("MainWindow", "İ ş l e m l e r"))
        self.cmb_mantiksal_islemler.setItemText(0, _translate("MainWindow", "NOT"))
        self.cmb_mantiksal_islemler.setItemText(1, _translate("MainWindow", "OR"))
        self.cmb_mantiksal_islemler.setItemText(2, _translate("MainWindow", "AND"))
        self.cmb_mantiksal_islemler.setItemText(3, _translate("MainWindow", "XOR"))
        self.cmb_mantiksal_islemler.setItemText(4, _translate("MainWindow", "AND NOT"))
        self.label_36.setText(_translate("MainWindow", "M a n t ı k s a l  İ ş l e m  S e ç i n i z :"))
        self.btn_mantiksal_uygula.setText(_translate("MainWindow", "U Y G U L A"))
        self.btn_classes_apply_9.setText(_translate("MainWindow", "^"))
        self.btn_mantiksal_b_yukle.setText(_translate("MainWindow", "↓"))
        self.btn_classes_apply_11.setText(_translate("MainWindow", "^"))
        self.label_8.setText(_translate("MainWindow", "Resim (sonuç)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_classes), _translate("MainWindow", "M A N T I K S A L"))
        self.label_10.setText(_translate("MainWindow", "R e s i m"))
        self.btn_labeling_yukle.setText(_translate("MainWindow", "↓"))
        self.label_11.setText(_translate("MainWindow", "Ş e k i l"))
        self.groupBox_5.setTitle(_translate("MainWindow", "İ ş l e m l e r"))
        self.btn_labeling_uygula.setText(_translate("MainWindow", "L A B E L I N G"))
        self.label_37.setText(_translate("MainWindow", "O l u ş a n  Ş e k i l l e r :"))
        self.btn_labeling_vurgula.setText(_translate("MainWindow", "V U R G U L A"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_split), _translate("MainWindow", "L A B E L I N G"))
        self.label_12.setText(_translate("MainWindow", "Ş e k i l"))
        self.label_13.setText(_translate("MainWindow", "R e s i m"))
        self.groupBox_6.setTitle(_translate("MainWindow", "İ ş l e m l e r"))
        self.btn_gurultu_olustur.setText(_translate("MainWindow", "G Ü R Ü L T Ü  O L U Ş T U R"))
        self.label_39.setText(_translate("MainWindow", "G ü r ü l t ü :"))
        self.lbl_gurultu_oran.setText(_translate("MainWindow", "0"))
        self.btn_gurultu_yukle.setText(_translate("MainWindow", "↓"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_performence), _translate("MainWindow", "G Ü R Ü L T Ü"))
        self.label_14.setText(_translate("MainWindow", "Ş e k i l"))
        self.label_15.setText(_translate("MainWindow", "R e s i m"))
        self.groupBox_7.setTitle(_translate("MainWindow", "İ ş l e m l e r"))
        self.btn_split_next_5.setText(_translate("MainWindow", "L A B E L I N G"))
        self.label_42.setText(_translate("MainWindow", "O l u ş a n  Ş e k i l l e r :"))
        self.btn_split_next_6.setText(_translate("MainWindow", "T E M P L A T E  M A T C H"))
        self.btn_classes_apply_14.setText(_translate("MainWindow", "↓"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "i ş l e m l e r"))
        self.label_17.setText(_translate("MainWindow", "C C O E F F"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "Bulunan Parça :"))
        self.label_21.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "Algılanan Nokta (Detected Point) :"))
        self.label_22.setText(_translate("MainWindow", "SSIM"))
        self.label_20.setText(_translate("MainWindow", "Aranan Parça :"))
        self.label_16.setText(_translate("MainWindow", "Eşleşen Sonuç (Matching Result) :"))
        self.label_2.setText(_translate("MainWindow", "MSE"))
        self.label_23.setText(_translate("MainWindow", "Eşleşen Sonuç (Matching Result) :"))
        self.label_24.setText(_translate("MainWindow", "Bulunan Parça :"))
        self.label_25.setText(_translate("MainWindow", "C C O E F F  N O R M E D"))
        self.label_26.setText(_translate("MainWindow", "0"))
        self.label_27.setText(_translate("MainWindow", "SSIM"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.label_28.setText(_translate("MainWindow", "Algılanan Nokta (Detected Point) :"))
        self.label_29.setText(_translate("MainWindow", "Aranan Parça :"))
        self.label_30.setText(_translate("MainWindow", "MSE"))
        self.label_31.setText(_translate("MainWindow", "Eşleşen Sonuç (Matching Result) :"))
        self.label_32.setText(_translate("MainWindow", "Bulunan Parça :"))
        self.label_33.setText(_translate("MainWindow", "C C O R R"))
        self.label_34.setText(_translate("MainWindow", "0"))
        self.label_35.setText(_translate("MainWindow", "SSIM"))
        self.label_38.setText(_translate("MainWindow", "0"))
        self.label_40.setText(_translate("MainWindow", "Algılanan Nokta (Detected Point) :"))
        self.label_41.setText(_translate("MainWindow", "Aranan Parça :"))
        self.label_43.setText(_translate("MainWindow", "MSE"))
        self.label_49.setText(_translate("MainWindow", "Aranan Parça :"))
        self.label_50.setText(_translate("MainWindow", "SSIM"))
        self.label_51.setText(_translate("MainWindow", "T M  C C O R R  N O R M E D"))
        self.label_52.setText(_translate("MainWindow", "Eşleşen Sonuç (Matching Result) :"))
        self.label_53.setText(_translate("MainWindow", "0"))
        self.label_54.setText(_translate("MainWindow", "MSE"))
        self.label_55.setText(_translate("MainWindow", "Bulunan Parça :"))
        self.label_56.setText(_translate("MainWindow", "0"))
        self.label_57.setText(_translate("MainWindow", "Algılanan Nokta (Detected Point) :"))
        self.label_58.setText(_translate("MainWindow", "Aranan Parça :"))
        self.label_59.setText(_translate("MainWindow", "SSIM"))
        self.label_60.setText(_translate("MainWindow", "T M  S Q D I F F"))
        self.label_61.setText(_translate("MainWindow", "Eşleşen Sonuç (Matching Result) :"))
        self.label_62.setText(_translate("MainWindow", "0"))
        self.label_63.setText(_translate("MainWindow", "MSE"))
        self.label_64.setText(_translate("MainWindow", "Bulunan Parça :"))
        self.label_65.setText(_translate("MainWindow", "0"))
        self.label_66.setText(_translate("MainWindow", "Algılanan Nokta (Detected Point) :"))
        self.label_67.setText(_translate("MainWindow", "Aranan Parça :"))
        self.label_68.setText(_translate("MainWindow", "SSIM"))
        self.label_69.setText(_translate("MainWindow", "T M  S Q D I F F  N O R M E D"))
        self.label_70.setText(_translate("MainWindow", "Eşleşen Sonuç (Matching Result) :"))
        self.label_71.setText(_translate("MainWindow", "0"))
        self.label_72.setText(_translate("MainWindow", "MSE"))
        self.label_73.setText(_translate("MainWindow", "Bulunan Parça :"))
        self.label_74.setText(_translate("MainWindow", "0"))
        self.label_75.setText(_translate("MainWindow", "Algılanan Nokta (Detected Point) :"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "s o n u ç l a r"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "T E M P L A T E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

