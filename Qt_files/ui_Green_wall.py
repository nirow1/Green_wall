# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Green_wallfFFpLQ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1264, 897)
        MainWindow.setStyleSheet(u"border: 1px solid;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(180, 0))
        self.widget.setMaximumSize(QSize(180, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.logo_4j_lbl = QLabel(self.widget_3)
        self.logo_4j_lbl.setObjectName(u"logo_4j_lbl")
        self.logo_4j_lbl.setMaximumSize(QSize(150, 50))

        self.verticalLayout_2.addWidget(self.logo_4j_lbl)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.watering_page_btn = QPushButton(self.widget_4)
        self.watering_page_btn.setObjectName(u"watering_page_btn")
        self.watering_page_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.watering_page_btn)

        self.solutio_page_btn = QPushButton(self.widget_4)
        self.solutio_page_btn.setObjectName(u"solutio_page_btn")
        self.solutio_page_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.solutio_page_btn)

        self.cams_page_btn = QPushButton(self.widget_4)
        self.cams_page_btn.setObjectName(u"cams_page_btn")
        self.cams_page_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.cams_page_btn)

        self.chart_page_btn = QPushButton(self.widget_4)
        self.chart_page_btn.setObjectName(u"chart_page_btn")
        self.chart_page_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.chart_page_btn)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.watering_pg = QWidget()
        self.watering_pg.setObjectName(u"watering_pg")
        self.gridLayout = QGridLayout(self.watering_pg)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_26 = QWidget(self.watering_pg)
        self.widget_26.setObjectName(u"widget_26")

        self.gridLayout.addWidget(self.widget_26, 4, 1, 1, 1)

        self.widget_28 = QWidget(self.watering_pg)
        self.widget_28.setObjectName(u"widget_28")

        self.gridLayout.addWidget(self.widget_28, 6, 1, 1, 1)

        self.widget_21 = QWidget(self.watering_pg)
        self.widget_21.setObjectName(u"widget_21")

        self.gridLayout.addWidget(self.widget_21, 5, 0, 1, 1)

        self.widget_17 = QWidget(self.watering_pg)
        self.widget_17.setObjectName(u"widget_17")

        self.gridLayout.addWidget(self.widget_17, 2, 1, 1, 1)

        self.widget_31 = QWidget(self.watering_pg)
        self.widget_31.setObjectName(u"widget_31")

        self.gridLayout.addWidget(self.widget_31, 4, 2, 1, 1)

        self.widget_33 = QWidget(self.watering_pg)
        self.widget_33.setObjectName(u"widget_33")

        self.gridLayout.addWidget(self.widget_33, 6, 2, 1, 1)

        self.widget_24 = QWidget(self.watering_pg)
        self.widget_24.setObjectName(u"widget_24")

        self.gridLayout.addWidget(self.widget_24, 1, 2, 1, 1)

        self.widget_15 = QWidget(self.watering_pg)
        self.widget_15.setObjectName(u"widget_15")

        self.gridLayout.addWidget(self.widget_15, 2, 0, 1, 1)

        self.widget_22 = QWidget(self.watering_pg)
        self.widget_22.setObjectName(u"widget_22")

        self.gridLayout.addWidget(self.widget_22, 6, 0, 1, 1)

        self.widget_29 = QWidget(self.watering_pg)
        self.widget_29.setObjectName(u"widget_29")

        self.gridLayout.addWidget(self.widget_29, 7, 1, 1, 1)

        self.widget_18 = QWidget(self.watering_pg)
        self.widget_18.setObjectName(u"widget_18")

        self.gridLayout.addWidget(self.widget_18, 3, 1, 1, 1)

        self.widget_19 = QWidget(self.watering_pg)
        self.widget_19.setObjectName(u"widget_19")

        self.gridLayout.addWidget(self.widget_19, 3, 0, 1, 1)

        self.widget_27 = QWidget(self.watering_pg)
        self.widget_27.setObjectName(u"widget_27")

        self.gridLayout.addWidget(self.widget_27, 5, 1, 1, 1)

        self.widget_14 = QWidget(self.watering_pg)
        self.widget_14.setObjectName(u"widget_14")

        self.gridLayout.addWidget(self.widget_14, 1, 0, 1, 1)

        self.widget_30 = QWidget(self.watering_pg)
        self.widget_30.setObjectName(u"widget_30")

        self.gridLayout.addWidget(self.widget_30, 3, 2, 1, 1)

        self.widget_32 = QWidget(self.watering_pg)
        self.widget_32.setObjectName(u"widget_32")

        self.gridLayout.addWidget(self.widget_32, 5, 2, 1, 1)

        self.widget_23 = QWidget(self.watering_pg)
        self.widget_23.setObjectName(u"widget_23")

        self.gridLayout.addWidget(self.widget_23, 7, 0, 1, 1)

        self.widget_34 = QWidget(self.watering_pg)
        self.widget_34.setObjectName(u"widget_34")

        self.gridLayout.addWidget(self.widget_34, 7, 2, 1, 1)

        self.widget_25 = QWidget(self.watering_pg)
        self.widget_25.setObjectName(u"widget_25")

        self.gridLayout.addWidget(self.widget_25, 2, 2, 1, 1)

        self.widget_20 = QWidget(self.watering_pg)
        self.widget_20.setObjectName(u"widget_20")

        self.gridLayout.addWidget(self.widget_20, 4, 0, 1, 1)

        self.widget_16 = QWidget(self.watering_pg)
        self.widget_16.setObjectName(u"widget_16")

        self.gridLayout.addWidget(self.widget_16, 1, 1, 1, 1)

        self.widget_48 = QWidget(self.watering_pg)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(0, 35))
        self.widget_48.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.widget_48)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(200, 35))

        self.horizontalLayout_7.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_48)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(200, 35))

        self.horizontalLayout_7.addWidget(self.pushButton_10)


        self.gridLayout.addWidget(self.widget_48, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.watering_pg)
        self.solution_pg = QWidget()
        self.solution_pg.setObjectName(u"solution_pg")
        self.verticalLayout_8 = QVBoxLayout(self.solution_pg)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_10 = QWidget(self.solution_pg)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget_10)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(self.widget_10)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.solution_dir_btn = QPushButton(self.widget_10)
        self.solution_dir_btn.setObjectName(u"solution_dir_btn")
        self.solution_dir_btn.setMinimumSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.solution_dir_btn)

        self.pushButton_6 = QPushButton(self.widget_10)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(100, 35))

        self.horizontalLayout_4.addWidget(self.pushButton_6)


        self.verticalLayout_8.addWidget(self.widget_10)

        self.widget_35 = QWidget(self.solution_pg)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_38 = QWidget(self.widget_35)
        self.widget_38.setObjectName(u"widget_38")

        self.horizontalLayout_5.addWidget(self.widget_38)

        self.widget_39 = QWidget(self.widget_35)
        self.widget_39.setObjectName(u"widget_39")

        self.horizontalLayout_5.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.widget_35)
        self.widget_40.setObjectName(u"widget_40")

        self.horizontalLayout_5.addWidget(self.widget_40)


        self.verticalLayout_8.addWidget(self.widget_35)

        self.widget_12 = QWidget(self.solution_pg)
        self.widget_12.setObjectName(u"widget_12")

        self.verticalLayout_8.addWidget(self.widget_12)

        self.widget_36 = QWidget(self.solution_pg)
        self.widget_36.setObjectName(u"widget_36")

        self.verticalLayout_8.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.solution_pg)
        self.widget_37.setObjectName(u"widget_37")

        self.verticalLayout_8.addWidget(self.widget_37)

        self.stackedWidget.addWidget(self.solution_pg)
        self.chart_pg = QWidget()
        self.chart_pg.setObjectName(u"chart_pg")
        self.horizontalLayout_6 = QHBoxLayout(self.chart_pg)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_41 = QWidget(self.chart_pg)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_9 = QVBoxLayout(self.widget_41)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.widget_43 = QWidget(self.widget_41)
        self.widget_43.setObjectName(u"widget_43")

        self.verticalLayout_9.addWidget(self.widget_43)

        self.widget_44 = QWidget(self.widget_41)
        self.widget_44.setObjectName(u"widget_44")

        self.verticalLayout_9.addWidget(self.widget_44)


        self.horizontalLayout_6.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.chart_pg)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_10 = QVBoxLayout(self.widget_42)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.widget_45 = QWidget(self.widget_42)
        self.widget_45.setObjectName(u"widget_45")

        self.verticalLayout_10.addWidget(self.widget_45)

        self.widget_46 = QWidget(self.widget_42)
        self.widget_46.setObjectName(u"widget_46")

        self.verticalLayout_10.addWidget(self.widget_46)

        self.widget_47 = QWidget(self.widget_42)
        self.widget_47.setObjectName(u"widget_47")

        self.verticalLayout_10.addWidget(self.widget_47)


        self.horizontalLayout_6.addWidget(self.widget_42)

        self.stackedWidget.addWidget(self.chart_pg)
        self.camera_pg = QWidget()
        self.camera_pg.setObjectName(u"camera_pg")
        self.verticalLayout_5 = QVBoxLayout(self.camera_pg)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_6 = QWidget(self.camera_pg)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.cam_dir_btn = QPushButton(self.widget_6)
        self.cam_dir_btn.setObjectName(u"cam_dir_btn")
        self.cam_dir_btn.setMinimumSize(QSize(35, 35))

        self.horizontalLayout_3.addWidget(self.cam_dir_btn)

        self.pushButton_5 = QPushButton(self.widget_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 0))
        self.pushButton_5.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_5.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.camera_pg)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")

        self.verticalLayout_6.addWidget(self.widget_11)

        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_7 = QVBoxLayout(self.widget_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.verticalSpacer_3 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.widget_13 = QWidget(self.widget_9)
        self.widget_13.setObjectName(u"widget_13")

        self.verticalLayout_7.addWidget(self.widget_13)

        self.verticalSpacer_4 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.horizontalLayout_2.addWidget(self.widget_9)


        self.verticalLayout_5.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.camera_pg)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1264, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_4j_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.watering_page_btn.setText(QCoreApplication.translate("MainWindow", u"Zal\u00e9v\u00e1n\u00ed", None))
        self.solutio_page_btn.setText(QCoreApplication.translate("MainWindow", u"Nastaven\u00ed roztoku", None))
        self.cams_page_btn.setText(QCoreApplication.translate("MainWindow", u"Kamery", None))
        self.chart_page_btn.setText(QCoreApplication.translate("MainWindow", u"Grafy", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.solution_dir_btn.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit do csv", None))
        self.cam_dir_btn.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit sn\u00edmek", None))
    # retranslateUi

