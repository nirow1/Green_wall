# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Green_walllNHiEm.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1264, 888)
        MainWindow.setStyleSheet(u"border: 1px solid;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(180, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.logo_4j_btn = QPushButton(self.widget_3)
        self.logo_4j_btn.setObjectName(u"logo_4j_btn")
        self.logo_4j_btn.setMinimumSize(QSize(150, 50))
        self.logo_4j_btn.setMaximumSize(QSize(150, 50))
        self.logo_4j_btn.setIconSize(QSize(150, 50))

        self.verticalLayout_2.addWidget(self.logo_4j_btn)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.watering_page_btn = QPushButton(self.widget_4)
        self.watering_page_btn.setObjectName(u"watering_page_btn")
        self.watering_page_btn.setMinimumSize(QSize(0, 0))
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

        self.expand_wgt = QWidget(self.centralwidget)
        self.expand_wgt.setObjectName(u"expand_wgt")
        self.expand_wgt.setMinimumSize(QSize(40, 0))
        self.expand_wgt.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout_17 = QVBoxLayout(self.expand_wgt)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 24, 0, 0)
        self.expand_menu_btn = QPushButton(self.expand_wgt)
        self.expand_menu_btn.setObjectName(u"expand_menu_btn")
        self.expand_menu_btn.setMaximumSize(QSize(40, 40))
        self.expand_menu_btn.setIconSize(QSize(40, 40))

        self.verticalLayout_17.addWidget(self.expand_menu_btn)

        self.widget_17 = QWidget(self.expand_wgt)
        self.widget_17.setObjectName(u"widget_17")

        self.verticalLayout_17.addWidget(self.widget_17)


        self.horizontalLayout.addWidget(self.expand_wgt)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_16 = QVBoxLayout(self.page_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.stackedWidget.addWidget(self.page_2)
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

        self.solution_dir_le = QLineEdit(self.widget_10)
        self.solution_dir_le.setObjectName(u"solution_dir_le")
        self.solution_dir_le.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_4.addWidget(self.solution_dir_le)

        self.solution_dir_btn = QPushButton(self.widget_10)
        self.solution_dir_btn.setObjectName(u"solution_dir_btn")
        self.solution_dir_btn.setMinimumSize(QSize(40, 35))
        self.solution_dir_btn.setIconSize(QSize(52, 35))

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
        self.horizontalLayout_118 = QHBoxLayout(self.chart_pg)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.widget_15 = QWidget(self.chart_pg)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_117 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(1, 1, 1, 1)
        self.widget_41 = QWidget(self.widget_15)
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


        self.horizontalLayout_117.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.widget_15)
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


        self.horizontalLayout_117.addWidget(self.widget_42)


        self.horizontalLayout_118.addWidget(self.widget_15)

        self.stackedWidget.addWidget(self.chart_pg)
        self.watering_pg = QWidget()
        self.watering_pg.setObjectName(u"watering_pg")
        self.verticalLayout_11 = QVBoxLayout(self.watering_pg)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_49 = QWidget(self.watering_pg)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.widget_14 = QWidget(self.widget_49)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.widget_14)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 40))
        self.pushButton_8.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_8)

        self.pushButton_4 = QPushButton(self.widget_14)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 40))
        self.pushButton_4.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_4)

        self.water_all_btn = QPushButton(self.widget_14)
        self.water_all_btn.setObjectName(u"water_all_btn")
        self.water_all_btn.setMinimumSize(QSize(0, 40))
        self.water_all_btn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.water_all_btn)


        self.horizontalLayout_8.addWidget(self.widget_14)


        self.verticalLayout_11.addWidget(self.widget_49)

        self.scrollArea = QScrollArea(self.watering_pg)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setBaseSize(QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 957, 1596))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_77 = QWidget(self.scrollAreaWidgetContents)
        self.widget_77.setObjectName(u"widget_77")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_77)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.label_2 = QLabel(self.widget_77)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_10.addWidget(self.label_2)

        self.water_col_btn_1 = QPushButton(self.widget_77)
        self.water_col_btn_1.setObjectName(u"water_col_btn_1")
        self.water_col_btn_1.setMinimumSize(QSize(0, 40))
        self.water_col_btn_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.water_col_btn_1)

        self.fill_column_btn_1 = QPushButton(self.widget_77)
        self.fill_column_btn_1.setObjectName(u"fill_column_btn_1")
        self.fill_column_btn_1.setMinimumSize(QSize(0, 40))
        self.fill_column_btn_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.fill_column_btn_1)


        self.verticalLayout_12.addWidget(self.widget_77)

        self.col_wg_1 = QWidget(self.scrollAreaWidgetContents)
        self.col_wg_1.setObjectName(u"col_wg_1")
        self.col_wg_1.setMinimumSize(QSize(0, 474))
        self.col_wg_1.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_13 = QVBoxLayout(self.col_wg_1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.widget_53 = QWidget(self.col_wg_1)
        self.widget_53.setObjectName(u"widget_53")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.water_btn_1 = QPushButton(self.widget_53)
        self.water_btn_1.setObjectName(u"water_btn_1")
        self.water_btn_1.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_9.addWidget(self.water_btn_1)

        self.widget_80 = QWidget(self.widget_53)
        self.widget_80.setObjectName(u"widget_80")
        self.widget_80.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_80)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.label_9 = QLabel(self.widget_80)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_13.addWidget(self.label_9)

        self.water_start_le_1 = QLineEdit(self.widget_80)
        self.water_start_le_1.setObjectName(u"water_start_le_1")
        self.water_start_le_1.setMinimumSize(QSize(0, 35))
        self.water_start_le_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_13.addWidget(self.water_start_le_1)

        self.label_15 = QLabel(self.widget_80)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)


        self.horizontalLayout_9.addWidget(self.widget_80)

        self.widget_81 = QWidget(self.widget_53)
        self.widget_81.setObjectName(u"widget_81")
        self.widget_81.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_81)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.label_10 = QLabel(self.widget_81)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_14.addWidget(self.label_10)

        self.water_dur_le_1 = QLineEdit(self.widget_81)
        self.water_dur_le_1.setObjectName(u"water_dur_le_1")
        self.water_dur_le_1.setMinimumSize(QSize(0, 35))
        self.water_dur_le_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_14.addWidget(self.water_dur_le_1)

        self.label_4 = QLabel(self.widget_81)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_14.addWidget(self.label_4)


        self.horizontalLayout_9.addWidget(self.widget_81)

        self.widget_82 = QWidget(self.widget_53)
        self.widget_82.setObjectName(u"widget_82")
        self.widget_82.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_82)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.label_11 = QLabel(self.widget_82)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_15.addWidget(self.label_11)

        self.water_interval_le_1 = QLineEdit(self.widget_82)
        self.water_interval_le_1.setObjectName(u"water_interval_le_1")
        self.water_interval_le_1.setMinimumSize(QSize(0, 35))
        self.water_interval_le_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_15.addWidget(self.water_interval_le_1)

        self.label_14 = QLabel(self.widget_82)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_15.addWidget(self.label_14)


        self.horizontalLayout_9.addWidget(self.widget_82)

        self.widget_83 = QWidget(self.widget_53)
        self.widget_83.setObjectName(u"widget_83")
        self.widget_83.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_83)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.label_12 = QLabel(self.widget_83)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_16.addWidget(self.label_12)

        self.water_end_le_1 = QLineEdit(self.widget_83)
        self.water_end_le_1.setObjectName(u"water_end_le_1")
        self.water_end_le_1.setMinimumSize(QSize(0, 35))
        self.water_end_le_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_16.addWidget(self.water_end_le_1)

        self.label_16 = QLabel(self.widget_83)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)


        self.horizontalLayout_9.addWidget(self.widget_83)


        self.verticalLayout_13.addWidget(self.widget_53)

        self.widget_54 = QWidget(self.col_wg_1)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.water_btn_2 = QPushButton(self.widget_54)
        self.water_btn_2.setObjectName(u"water_btn_2")
        self.water_btn_2.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_21.addWidget(self.water_btn_2)

        self.widget_85 = QWidget(self.widget_54)
        self.widget_85.setObjectName(u"widget_85")
        self.widget_85.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_85)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(2, 2, 2, 2)
        self.label_19 = QLabel(self.widget_85)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.label_19)

        self.water_start_le_2 = QLineEdit(self.widget_85)
        self.water_start_le_2.setObjectName(u"water_start_le_2")
        self.water_start_le_2.setMinimumSize(QSize(0, 35))
        self.water_start_le_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_18.addWidget(self.water_start_le_2)

        self.label_20 = QLabel(self.widget_85)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_18.addWidget(self.label_20)


        self.horizontalLayout_21.addWidget(self.widget_85)

        self.widget_87 = QWidget(self.widget_54)
        self.widget_87.setObjectName(u"widget_87")
        self.widget_87.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_87)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(2, 2, 2, 2)
        self.label_23 = QLabel(self.widget_87)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_20.addWidget(self.label_23)

        self.water_dur_le_2 = QLineEdit(self.widget_87)
        self.water_dur_le_2.setObjectName(u"water_dur_le_2")
        self.water_dur_le_2.setMinimumSize(QSize(0, 35))
        self.water_dur_le_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_20.addWidget(self.water_dur_le_2)

        self.label_24 = QLabel(self.widget_87)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_20.addWidget(self.label_24)


        self.horizontalLayout_21.addWidget(self.widget_87)

        self.widget_84 = QWidget(self.widget_54)
        self.widget_84.setObjectName(u"widget_84")
        self.widget_84.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_84)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.label_17 = QLabel(self.widget_84)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_17.addWidget(self.label_17)

        self.water_interval_le_2 = QLineEdit(self.widget_84)
        self.water_interval_le_2.setObjectName(u"water_interval_le_2")
        self.water_interval_le_2.setMinimumSize(QSize(0, 35))
        self.water_interval_le_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_17.addWidget(self.water_interval_le_2)

        self.label_18 = QLabel(self.widget_84)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_17.addWidget(self.label_18)


        self.horizontalLayout_21.addWidget(self.widget_84)

        self.widget_86 = QWidget(self.widget_54)
        self.widget_86.setObjectName(u"widget_86")
        self.widget_86.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_86)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.label_21 = QLabel(self.widget_86)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_19.addWidget(self.label_21)

        self.water_end_le_2 = QLineEdit(self.widget_86)
        self.water_end_le_2.setObjectName(u"water_end_le_2")
        self.water_end_le_2.setMinimumSize(QSize(0, 35))
        self.water_end_le_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_19.addWidget(self.water_end_le_2)

        self.label_22 = QLabel(self.widget_86)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_19.addWidget(self.label_22)


        self.horizontalLayout_21.addWidget(self.widget_86)


        self.verticalLayout_13.addWidget(self.widget_54)

        self.widget_55 = QWidget(self.col_wg_1)
        self.widget_55.setObjectName(u"widget_55")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(1, 1, 1, 1)
        self.water_btn_3 = QPushButton(self.widget_55)
        self.water_btn_3.setObjectName(u"water_btn_3")
        self.water_btn_3.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_26.addWidget(self.water_btn_3)

        self.widget_90 = QWidget(self.widget_55)
        self.widget_90.setObjectName(u"widget_90")
        self.widget_90.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_90)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(2, 2, 2, 2)
        self.label_29 = QLabel(self.widget_90)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_24.addWidget(self.label_29)

        self.water_start_le_3 = QLineEdit(self.widget_90)
        self.water_start_le_3.setObjectName(u"water_start_le_3")
        self.water_start_le_3.setMinimumSize(QSize(0, 35))
        self.water_start_le_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_24.addWidget(self.water_start_le_3)

        self.label_30 = QLabel(self.widget_90)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_24.addWidget(self.label_30)


        self.horizontalLayout_26.addWidget(self.widget_90)

        self.widget_88 = QWidget(self.widget_55)
        self.widget_88.setObjectName(u"widget_88")
        self.widget_88.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_88)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(2, 2, 2, 2)
        self.label_25 = QLabel(self.widget_88)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_22.addWidget(self.label_25)

        self.water_dur_le_3 = QLineEdit(self.widget_88)
        self.water_dur_le_3.setObjectName(u"water_dur_le_3")
        self.water_dur_le_3.setMinimumSize(QSize(0, 35))
        self.water_dur_le_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_22.addWidget(self.water_dur_le_3)

        self.label_26 = QLabel(self.widget_88)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_22.addWidget(self.label_26)


        self.horizontalLayout_26.addWidget(self.widget_88)

        self.widget_89 = QWidget(self.widget_55)
        self.widget_89.setObjectName(u"widget_89")
        self.widget_89.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_89)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(2, 2, 2, 2)
        self.label_27 = QLabel(self.widget_89)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_23.addWidget(self.label_27)

        self.water_interval_le_3 = QLineEdit(self.widget_89)
        self.water_interval_le_3.setObjectName(u"water_interval_le_3")
        self.water_interval_le_3.setMinimumSize(QSize(0, 35))
        self.water_interval_le_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_23.addWidget(self.water_interval_le_3)

        self.label_28 = QLabel(self.widget_89)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_23.addWidget(self.label_28)


        self.horizontalLayout_26.addWidget(self.widget_89)

        self.widget_91 = QWidget(self.widget_55)
        self.widget_91.setObjectName(u"widget_91")
        self.widget_91.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_91)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(2, 2, 2, 2)
        self.label_31 = QLabel(self.widget_91)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_25.addWidget(self.label_31)

        self.water_end_le_3 = QLineEdit(self.widget_91)
        self.water_end_le_3.setObjectName(u"water_end_le_3")
        self.water_end_le_3.setMinimumSize(QSize(0, 35))
        self.water_end_le_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_25.addWidget(self.water_end_le_3)

        self.label_32 = QLabel(self.widget_91)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_25.addWidget(self.label_32)


        self.horizontalLayout_26.addWidget(self.widget_91)


        self.verticalLayout_13.addWidget(self.widget_55)

        self.widget_56 = QWidget(self.col_wg_1)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_31.setSpacing(5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(1, 1, 1, 1)
        self.water_btn_4 = QPushButton(self.widget_56)
        self.water_btn_4.setObjectName(u"water_btn_4")
        self.water_btn_4.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_31.addWidget(self.water_btn_4)

        self.widget_94 = QWidget(self.widget_56)
        self.widget_94.setObjectName(u"widget_94")
        self.widget_94.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_29 = QHBoxLayout(self.widget_94)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(2, 2, 2, 2)
        self.label_37 = QLabel(self.widget_94)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_29.addWidget(self.label_37)

        self.water_start_le_4 = QLineEdit(self.widget_94)
        self.water_start_le_4.setObjectName(u"water_start_le_4")
        self.water_start_le_4.setMinimumSize(QSize(0, 35))
        self.water_start_le_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_29.addWidget(self.water_start_le_4)

        self.label_38 = QLabel(self.widget_94)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_29.addWidget(self.label_38)


        self.horizontalLayout_31.addWidget(self.widget_94)

        self.widget_92 = QWidget(self.widget_56)
        self.widget_92.setObjectName(u"widget_92")
        self.widget_92.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_92)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(2, 2, 2, 2)
        self.label_33 = QLabel(self.widget_92)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_27.addWidget(self.label_33)

        self.water_dur_le_4 = QLineEdit(self.widget_92)
        self.water_dur_le_4.setObjectName(u"water_dur_le_4")
        self.water_dur_le_4.setMinimumSize(QSize(0, 35))
        self.water_dur_le_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_27.addWidget(self.water_dur_le_4)

        self.label_34 = QLabel(self.widget_92)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_27.addWidget(self.label_34)


        self.horizontalLayout_31.addWidget(self.widget_92)

        self.widget_93 = QWidget(self.widget_56)
        self.widget_93.setObjectName(u"widget_93")
        self.widget_93.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_93)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(2, 2, 2, 2)
        self.label_35 = QLabel(self.widget_93)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_28.addWidget(self.label_35)

        self.water_interval_le_4 = QLineEdit(self.widget_93)
        self.water_interval_le_4.setObjectName(u"water_interval_le_4")
        self.water_interval_le_4.setMinimumSize(QSize(0, 35))
        self.water_interval_le_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_28.addWidget(self.water_interval_le_4)

        self.label_36 = QLabel(self.widget_93)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_28.addWidget(self.label_36)


        self.horizontalLayout_31.addWidget(self.widget_93)

        self.widget_95 = QWidget(self.widget_56)
        self.widget_95.setObjectName(u"widget_95")
        self.widget_95.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_30 = QHBoxLayout(self.widget_95)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(2, 2, 2, 2)
        self.label_39 = QLabel(self.widget_95)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_30.addWidget(self.label_39)

        self.water_end_le_4 = QLineEdit(self.widget_95)
        self.water_end_le_4.setObjectName(u"water_end_le_4")
        self.water_end_le_4.setMinimumSize(QSize(0, 35))
        self.water_end_le_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_30.addWidget(self.water_end_le_4)

        self.label_40 = QLabel(self.widget_95)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_30.addWidget(self.label_40)


        self.horizontalLayout_31.addWidget(self.widget_95)


        self.verticalLayout_13.addWidget(self.widget_56)

        self.widget_57 = QWidget(self.col_wg_1)
        self.widget_57.setObjectName(u"widget_57")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_36.setSpacing(5)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(1, 1, 1, 1)
        self.water_btn_5 = QPushButton(self.widget_57)
        self.water_btn_5.setObjectName(u"water_btn_5")
        self.water_btn_5.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_36.addWidget(self.water_btn_5)

        self.widget_98 = QWidget(self.widget_57)
        self.widget_98.setObjectName(u"widget_98")
        self.widget_98.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_34 = QHBoxLayout(self.widget_98)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(2, 2, 2, 2)
        self.label_45 = QLabel(self.widget_98)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_34.addWidget(self.label_45)

        self.water_start_le_5 = QLineEdit(self.widget_98)
        self.water_start_le_5.setObjectName(u"water_start_le_5")
        self.water_start_le_5.setMinimumSize(QSize(0, 35))
        self.water_start_le_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_34.addWidget(self.water_start_le_5)

        self.label_46 = QLabel(self.widget_98)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_34.addWidget(self.label_46)


        self.horizontalLayout_36.addWidget(self.widget_98)

        self.widget_96 = QWidget(self.widget_57)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_32 = QHBoxLayout(self.widget_96)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(2, 2, 2, 2)
        self.label_41 = QLabel(self.widget_96)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_32.addWidget(self.label_41)

        self.water_dur_le_5 = QLineEdit(self.widget_96)
        self.water_dur_le_5.setObjectName(u"water_dur_le_5")
        self.water_dur_le_5.setMinimumSize(QSize(0, 35))
        self.water_dur_le_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_32.addWidget(self.water_dur_le_5)

        self.label_42 = QLabel(self.widget_96)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_32.addWidget(self.label_42)


        self.horizontalLayout_36.addWidget(self.widget_96)

        self.widget_97 = QWidget(self.widget_57)
        self.widget_97.setObjectName(u"widget_97")
        self.widget_97.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_33 = QHBoxLayout(self.widget_97)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(2, 2, 2, 2)
        self.label_43 = QLabel(self.widget_97)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_33.addWidget(self.label_43)

        self.water_interval_le_5 = QLineEdit(self.widget_97)
        self.water_interval_le_5.setObjectName(u"water_interval_le_5")
        self.water_interval_le_5.setMinimumSize(QSize(0, 35))
        self.water_interval_le_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_33.addWidget(self.water_interval_le_5)

        self.label_44 = QLabel(self.widget_97)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_33.addWidget(self.label_44)


        self.horizontalLayout_36.addWidget(self.widget_97)

        self.widget_99 = QWidget(self.widget_57)
        self.widget_99.setObjectName(u"widget_99")
        self.widget_99.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_99)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(2, 2, 2, 2)
        self.label_47 = QLabel(self.widget_99)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_35.addWidget(self.label_47)

        self.water_end_le_5 = QLineEdit(self.widget_99)
        self.water_end_le_5.setObjectName(u"water_end_le_5")
        self.water_end_le_5.setMinimumSize(QSize(0, 35))
        self.water_end_le_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_35.addWidget(self.water_end_le_5)

        self.label_48 = QLabel(self.widget_99)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_35.addWidget(self.label_48)


        self.horizontalLayout_36.addWidget(self.widget_99)


        self.verticalLayout_13.addWidget(self.widget_57)

        self.widget_58 = QWidget(self.col_wg_1)
        self.widget_58.setObjectName(u"widget_58")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_41.setSpacing(5)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(1, 1, 1, 1)
        self.water_btn_6 = QPushButton(self.widget_58)
        self.water_btn_6.setObjectName(u"water_btn_6")
        self.water_btn_6.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_41.addWidget(self.water_btn_6)

        self.widget_102 = QWidget(self.widget_58)
        self.widget_102.setObjectName(u"widget_102")
        self.widget_102.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_39 = QHBoxLayout(self.widget_102)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(2, 2, 2, 2)
        self.label_53 = QLabel(self.widget_102)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_39.addWidget(self.label_53)

        self.water_start_le_6 = QLineEdit(self.widget_102)
        self.water_start_le_6.setObjectName(u"water_start_le_6")
        self.water_start_le_6.setMinimumSize(QSize(0, 35))
        self.water_start_le_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_39.addWidget(self.water_start_le_6)

        self.label_54 = QLabel(self.widget_102)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_39.addWidget(self.label_54)


        self.horizontalLayout_41.addWidget(self.widget_102)

        self.widget_100 = QWidget(self.widget_58)
        self.widget_100.setObjectName(u"widget_100")
        self.widget_100.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_100)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(2, 2, 2, 2)
        self.label_49 = QLabel(self.widget_100)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_37.addWidget(self.label_49)

        self.water_dur_le_6 = QLineEdit(self.widget_100)
        self.water_dur_le_6.setObjectName(u"water_dur_le_6")
        self.water_dur_le_6.setMinimumSize(QSize(0, 35))
        self.water_dur_le_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_37.addWidget(self.water_dur_le_6)

        self.label_50 = QLabel(self.widget_100)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_37.addWidget(self.label_50)


        self.horizontalLayout_41.addWidget(self.widget_100)

        self.widget_101 = QWidget(self.widget_58)
        self.widget_101.setObjectName(u"widget_101")
        self.widget_101.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_38 = QHBoxLayout(self.widget_101)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(2, 2, 2, 2)
        self.label_51 = QLabel(self.widget_101)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_38.addWidget(self.label_51)

        self.water_interval_le_6 = QLineEdit(self.widget_101)
        self.water_interval_le_6.setObjectName(u"water_interval_le_6")
        self.water_interval_le_6.setMinimumSize(QSize(0, 35))
        self.water_interval_le_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_38.addWidget(self.water_interval_le_6)

        self.label_52 = QLabel(self.widget_101)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_38.addWidget(self.label_52)


        self.horizontalLayout_41.addWidget(self.widget_101)

        self.widget_103 = QWidget(self.widget_58)
        self.widget_103.setObjectName(u"widget_103")
        self.widget_103.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_40 = QHBoxLayout(self.widget_103)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(2, 2, 2, 2)
        self.label_55 = QLabel(self.widget_103)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_40.addWidget(self.label_55)

        self.water_end_le_6 = QLineEdit(self.widget_103)
        self.water_end_le_6.setObjectName(u"water_end_le_6")
        self.water_end_le_6.setMinimumSize(QSize(0, 35))
        self.water_end_le_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_40.addWidget(self.water_end_le_6)

        self.label_56 = QLabel(self.widget_103)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_40.addWidget(self.label_56)


        self.horizontalLayout_41.addWidget(self.widget_103)


        self.verticalLayout_13.addWidget(self.widget_58)

        self.widget_59 = QWidget(self.col_wg_1)
        self.widget_59.setObjectName(u"widget_59")
        self.horizontalLayout_46 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_46.setSpacing(5)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(1, 1, 1, 1)
        self.water_btn_7 = QPushButton(self.widget_59)
        self.water_btn_7.setObjectName(u"water_btn_7")
        self.water_btn_7.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_46.addWidget(self.water_btn_7)

        self.widget_106 = QWidget(self.widget_59)
        self.widget_106.setObjectName(u"widget_106")
        self.widget_106.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_44 = QHBoxLayout(self.widget_106)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(2, 2, 2, 2)
        self.label_61 = QLabel(self.widget_106)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_44.addWidget(self.label_61)

        self.water_start_le_7 = QLineEdit(self.widget_106)
        self.water_start_le_7.setObjectName(u"water_start_le_7")
        self.water_start_le_7.setMinimumSize(QSize(0, 35))
        self.water_start_le_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_44.addWidget(self.water_start_le_7)

        self.label_62 = QLabel(self.widget_106)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_44.addWidget(self.label_62)


        self.horizontalLayout_46.addWidget(self.widget_106)

        self.widget_104 = QWidget(self.widget_59)
        self.widget_104.setObjectName(u"widget_104")
        self.widget_104.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_42 = QHBoxLayout(self.widget_104)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(2, 2, 2, 2)
        self.label_57 = QLabel(self.widget_104)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_42.addWidget(self.label_57)

        self.water_dur_le_7 = QLineEdit(self.widget_104)
        self.water_dur_le_7.setObjectName(u"water_dur_le_7")
        self.water_dur_le_7.setMinimumSize(QSize(0, 35))
        self.water_dur_le_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_42.addWidget(self.water_dur_le_7)

        self.label_58 = QLabel(self.widget_104)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_42.addWidget(self.label_58)


        self.horizontalLayout_46.addWidget(self.widget_104)

        self.widget_105 = QWidget(self.widget_59)
        self.widget_105.setObjectName(u"widget_105")
        self.widget_105.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_43 = QHBoxLayout(self.widget_105)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(2, 2, 2, 2)
        self.label_59 = QLabel(self.widget_105)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_43.addWidget(self.label_59)

        self.water_interval_le_7 = QLineEdit(self.widget_105)
        self.water_interval_le_7.setObjectName(u"water_interval_le_7")
        self.water_interval_le_7.setMinimumSize(QSize(0, 35))
        self.water_interval_le_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_43.addWidget(self.water_interval_le_7)

        self.label_60 = QLabel(self.widget_105)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_43.addWidget(self.label_60)


        self.horizontalLayout_46.addWidget(self.widget_105)

        self.widget_107 = QWidget(self.widget_59)
        self.widget_107.setObjectName(u"widget_107")
        self.widget_107.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_45 = QHBoxLayout(self.widget_107)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(2, 2, 2, 2)
        self.label_63 = QLabel(self.widget_107)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_45.addWidget(self.label_63)

        self.water_end_le_7 = QLineEdit(self.widget_107)
        self.water_end_le_7.setObjectName(u"water_end_le_7")
        self.water_end_le_7.setMinimumSize(QSize(0, 35))
        self.water_end_le_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_45.addWidget(self.water_end_le_7)

        self.label_64 = QLabel(self.widget_107)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_45.addWidget(self.label_64)


        self.horizontalLayout_46.addWidget(self.widget_107)


        self.verticalLayout_13.addWidget(self.widget_59)


        self.verticalLayout_12.addWidget(self.col_wg_1)

        self.widget_78 = QWidget(self.scrollAreaWidgetContents)
        self.widget_78.setObjectName(u"widget_78")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_78)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.label_13 = QLabel(self.widget_78)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.water_col_btn_2 = QPushButton(self.widget_78)
        self.water_col_btn_2.setObjectName(u"water_col_btn_2")
        self.water_col_btn_2.setMinimumSize(QSize(0, 40))
        self.water_col_btn_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.water_col_btn_2)

        self.fill_column_btn_2 = QPushButton(self.widget_78)
        self.fill_column_btn_2.setObjectName(u"fill_column_btn_2")
        self.fill_column_btn_2.setMinimumSize(QSize(0, 40))
        self.fill_column_btn_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.fill_column_btn_2)


        self.verticalLayout_12.addWidget(self.widget_78)

        self.col_wg_2 = QWidget(self.scrollAreaWidgetContents)
        self.col_wg_2.setObjectName(u"col_wg_2")
        self.col_wg_2.setMinimumSize(QSize(0, 474))
        self.verticalLayout_14 = QVBoxLayout(self.col_wg_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.widget_62 = QWidget(self.col_wg_2)
        self.widget_62.setObjectName(u"widget_62")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_51.setSpacing(5)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(1, 1, 1, 1)
        self.water_btn_8 = QPushButton(self.widget_62)
        self.water_btn_8.setObjectName(u"water_btn_8")
        self.water_btn_8.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_51.addWidget(self.water_btn_8)

        self.widget_110 = QWidget(self.widget_62)
        self.widget_110.setObjectName(u"widget_110")
        self.widget_110.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_49 = QHBoxLayout(self.widget_110)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(2, 2, 2, 2)
        self.label_69 = QLabel(self.widget_110)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_49.addWidget(self.label_69)

        self.water_start_le_8 = QLineEdit(self.widget_110)
        self.water_start_le_8.setObjectName(u"water_start_le_8")
        self.water_start_le_8.setMinimumSize(QSize(0, 35))
        self.water_start_le_8.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_49.addWidget(self.water_start_le_8)

        self.label_70 = QLabel(self.widget_110)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_49.addWidget(self.label_70)


        self.horizontalLayout_51.addWidget(self.widget_110)

        self.widget_108 = QWidget(self.widget_62)
        self.widget_108.setObjectName(u"widget_108")
        self.widget_108.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_47 = QHBoxLayout(self.widget_108)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(2, 2, 2, 2)
        self.label_65 = QLabel(self.widget_108)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_47.addWidget(self.label_65)

        self.water_dur_le_8 = QLineEdit(self.widget_108)
        self.water_dur_le_8.setObjectName(u"water_dur_le_8")
        self.water_dur_le_8.setMinimumSize(QSize(0, 35))
        self.water_dur_le_8.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_47.addWidget(self.water_dur_le_8)

        self.label_66 = QLabel(self.widget_108)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_47.addWidget(self.label_66)


        self.horizontalLayout_51.addWidget(self.widget_108)

        self.widget_109 = QWidget(self.widget_62)
        self.widget_109.setObjectName(u"widget_109")
        self.widget_109.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_48 = QHBoxLayout(self.widget_109)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(2, 2, 2, 2)
        self.label_67 = QLabel(self.widget_109)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_48.addWidget(self.label_67)

        self.water_interval_le_8 = QLineEdit(self.widget_109)
        self.water_interval_le_8.setObjectName(u"water_interval_le_8")
        self.water_interval_le_8.setMinimumSize(QSize(0, 35))
        self.water_interval_le_8.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_48.addWidget(self.water_interval_le_8)

        self.label_68 = QLabel(self.widget_109)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_48.addWidget(self.label_68)


        self.horizontalLayout_51.addWidget(self.widget_109)

        self.widget_111 = QWidget(self.widget_62)
        self.widget_111.setObjectName(u"widget_111")
        self.widget_111.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_50 = QHBoxLayout(self.widget_111)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(2, 2, 2, 2)
        self.label_71 = QLabel(self.widget_111)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_50.addWidget(self.label_71)

        self.water_end_le_8 = QLineEdit(self.widget_111)
        self.water_end_le_8.setObjectName(u"water_end_le_8")
        self.water_end_le_8.setMinimumSize(QSize(0, 35))
        self.water_end_le_8.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_50.addWidget(self.water_end_le_8)

        self.label_72 = QLabel(self.widget_111)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_50.addWidget(self.label_72)


        self.horizontalLayout_51.addWidget(self.widget_111)


        self.verticalLayout_14.addWidget(self.widget_62)

        self.widget_66 = QWidget(self.col_wg_2)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_56.setSpacing(5)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(1, 1, 1, 1)
        self.water_btn_9 = QPushButton(self.widget_66)
        self.water_btn_9.setObjectName(u"water_btn_9")
        self.water_btn_9.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_56.addWidget(self.water_btn_9)

        self.widget_112 = QWidget(self.widget_66)
        self.widget_112.setObjectName(u"widget_112")
        self.widget_112.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_52 = QHBoxLayout(self.widget_112)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(2, 2, 2, 2)
        self.label_73 = QLabel(self.widget_112)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_52.addWidget(self.label_73)

        self.water_start_le_9 = QLineEdit(self.widget_112)
        self.water_start_le_9.setObjectName(u"water_start_le_9")
        self.water_start_le_9.setMinimumSize(QSize(0, 35))
        self.water_start_le_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_52.addWidget(self.water_start_le_9)

        self.label_74 = QLabel(self.widget_112)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_52.addWidget(self.label_74)


        self.horizontalLayout_56.addWidget(self.widget_112)

        self.widget_113 = QWidget(self.widget_66)
        self.widget_113.setObjectName(u"widget_113")
        self.widget_113.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_53 = QHBoxLayout(self.widget_113)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(2, 2, 2, 2)
        self.label_75 = QLabel(self.widget_113)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_53.addWidget(self.label_75)

        self.water_dur_le_9 = QLineEdit(self.widget_113)
        self.water_dur_le_9.setObjectName(u"water_dur_le_9")
        self.water_dur_le_9.setMinimumSize(QSize(0, 35))
        self.water_dur_le_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_53.addWidget(self.water_dur_le_9)

        self.label_76 = QLabel(self.widget_113)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_53.addWidget(self.label_76)


        self.horizontalLayout_56.addWidget(self.widget_113)

        self.widget_114 = QWidget(self.widget_66)
        self.widget_114.setObjectName(u"widget_114")
        self.widget_114.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_54 = QHBoxLayout(self.widget_114)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(2, 2, 2, 2)
        self.label_77 = QLabel(self.widget_114)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_54.addWidget(self.label_77)

        self.water_interval_le_9 = QLineEdit(self.widget_114)
        self.water_interval_le_9.setObjectName(u"water_interval_le_9")
        self.water_interval_le_9.setMinimumSize(QSize(0, 35))
        self.water_interval_le_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_54.addWidget(self.water_interval_le_9)

        self.label_78 = QLabel(self.widget_114)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_54.addWidget(self.label_78)


        self.horizontalLayout_56.addWidget(self.widget_114)

        self.widget_115 = QWidget(self.widget_66)
        self.widget_115.setObjectName(u"widget_115")
        self.widget_115.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_55 = QHBoxLayout(self.widget_115)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(2, 2, 2, 2)
        self.label_79 = QLabel(self.widget_115)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_55.addWidget(self.label_79)

        self.water_end_le_9 = QLineEdit(self.widget_115)
        self.water_end_le_9.setObjectName(u"water_end_le_9")
        self.water_end_le_9.setMinimumSize(QSize(0, 35))
        self.water_end_le_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_55.addWidget(self.water_end_le_9)

        self.label_80 = QLabel(self.widget_115)
        self.label_80.setObjectName(u"label_80")

        self.horizontalLayout_55.addWidget(self.label_80)


        self.horizontalLayout_56.addWidget(self.widget_115)


        self.verticalLayout_14.addWidget(self.widget_66)

        self.widget_60 = QWidget(self.col_wg_2)
        self.widget_60.setObjectName(u"widget_60")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_61.setSpacing(5)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(1, 1, 1, 1)
        self.water_btn_10 = QPushButton(self.widget_60)
        self.water_btn_10.setObjectName(u"water_btn_10")
        self.water_btn_10.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_61.addWidget(self.water_btn_10)

        self.widget_116 = QWidget(self.widget_60)
        self.widget_116.setObjectName(u"widget_116")
        self.widget_116.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_57 = QHBoxLayout(self.widget_116)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(2, 2, 2, 2)
        self.label_81 = QLabel(self.widget_116)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_57.addWidget(self.label_81)

        self.water_start_le_10 = QLineEdit(self.widget_116)
        self.water_start_le_10.setObjectName(u"water_start_le_10")
        self.water_start_le_10.setMinimumSize(QSize(0, 35))
        self.water_start_le_10.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_57.addWidget(self.water_start_le_10)

        self.label_82 = QLabel(self.widget_116)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_57.addWidget(self.label_82)


        self.horizontalLayout_61.addWidget(self.widget_116)

        self.widget_117 = QWidget(self.widget_60)
        self.widget_117.setObjectName(u"widget_117")
        self.widget_117.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_58 = QHBoxLayout(self.widget_117)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(2, 2, 2, 2)
        self.label_83 = QLabel(self.widget_117)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_58.addWidget(self.label_83)

        self.water_dur_le_10 = QLineEdit(self.widget_117)
        self.water_dur_le_10.setObjectName(u"water_dur_le_10")
        self.water_dur_le_10.setMinimumSize(QSize(0, 35))
        self.water_dur_le_10.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_58.addWidget(self.water_dur_le_10)

        self.label_84 = QLabel(self.widget_117)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_58.addWidget(self.label_84)


        self.horizontalLayout_61.addWidget(self.widget_117)

        self.widget_118 = QWidget(self.widget_60)
        self.widget_118.setObjectName(u"widget_118")
        self.widget_118.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_59 = QHBoxLayout(self.widget_118)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(2, 2, 2, 2)
        self.label_85 = QLabel(self.widget_118)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_59.addWidget(self.label_85)

        self.water_interval_le_10 = QLineEdit(self.widget_118)
        self.water_interval_le_10.setObjectName(u"water_interval_le_10")
        self.water_interval_le_10.setMinimumSize(QSize(0, 35))
        self.water_interval_le_10.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_59.addWidget(self.water_interval_le_10)

        self.label_86 = QLabel(self.widget_118)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_59.addWidget(self.label_86)


        self.horizontalLayout_61.addWidget(self.widget_118)

        self.widget_119 = QWidget(self.widget_60)
        self.widget_119.setObjectName(u"widget_119")
        self.widget_119.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_60 = QHBoxLayout(self.widget_119)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(2, 2, 2, 2)
        self.label_87 = QLabel(self.widget_119)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_60.addWidget(self.label_87)

        self.water_end_le_10 = QLineEdit(self.widget_119)
        self.water_end_le_10.setObjectName(u"water_end_le_10")
        self.water_end_le_10.setMinimumSize(QSize(0, 35))
        self.water_end_le_10.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_60.addWidget(self.water_end_le_10)

        self.label_88 = QLabel(self.widget_119)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_60.addWidget(self.label_88)


        self.horizontalLayout_61.addWidget(self.widget_119)


        self.verticalLayout_14.addWidget(self.widget_60)

        self.widget_63 = QWidget(self.col_wg_2)
        self.widget_63.setObjectName(u"widget_63")
        self.horizontalLayout_66 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_66.setSpacing(5)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(1, 1, 1, 1)
        self.water_btn_11 = QPushButton(self.widget_63)
        self.water_btn_11.setObjectName(u"water_btn_11")
        self.water_btn_11.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_66.addWidget(self.water_btn_11)

        self.widget_120 = QWidget(self.widget_63)
        self.widget_120.setObjectName(u"widget_120")
        self.widget_120.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_62 = QHBoxLayout(self.widget_120)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(2, 2, 2, 2)
        self.label_89 = QLabel(self.widget_120)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_62.addWidget(self.label_89)

        self.water_start_le_11 = QLineEdit(self.widget_120)
        self.water_start_le_11.setObjectName(u"water_start_le_11")
        self.water_start_le_11.setMinimumSize(QSize(0, 35))
        self.water_start_le_11.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_62.addWidget(self.water_start_le_11)

        self.label_90 = QLabel(self.widget_120)
        self.label_90.setObjectName(u"label_90")

        self.horizontalLayout_62.addWidget(self.label_90)


        self.horizontalLayout_66.addWidget(self.widget_120)

        self.widget_121 = QWidget(self.widget_63)
        self.widget_121.setObjectName(u"widget_121")
        self.widget_121.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_63 = QHBoxLayout(self.widget_121)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(2, 2, 2, 2)
        self.label_91 = QLabel(self.widget_121)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_63.addWidget(self.label_91)

        self.water_dur_le_11 = QLineEdit(self.widget_121)
        self.water_dur_le_11.setObjectName(u"water_dur_le_11")
        self.water_dur_le_11.setMinimumSize(QSize(0, 35))
        self.water_dur_le_11.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_63.addWidget(self.water_dur_le_11)

        self.label_92 = QLabel(self.widget_121)
        self.label_92.setObjectName(u"label_92")

        self.horizontalLayout_63.addWidget(self.label_92)


        self.horizontalLayout_66.addWidget(self.widget_121)

        self.widget_122 = QWidget(self.widget_63)
        self.widget_122.setObjectName(u"widget_122")
        self.widget_122.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_64 = QHBoxLayout(self.widget_122)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(2, 2, 2, 2)
        self.label_93 = QLabel(self.widget_122)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_64.addWidget(self.label_93)

        self.water_interval_le_11 = QLineEdit(self.widget_122)
        self.water_interval_le_11.setObjectName(u"water_interval_le_11")
        self.water_interval_le_11.setMinimumSize(QSize(0, 35))
        self.water_interval_le_11.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_64.addWidget(self.water_interval_le_11)

        self.label_94 = QLabel(self.widget_122)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_64.addWidget(self.label_94)


        self.horizontalLayout_66.addWidget(self.widget_122)

        self.widget_123 = QWidget(self.widget_63)
        self.widget_123.setObjectName(u"widget_123")
        self.widget_123.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_65 = QHBoxLayout(self.widget_123)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(2, 2, 2, 2)
        self.label_95 = QLabel(self.widget_123)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_65.addWidget(self.label_95)

        self.water_end_le_11 = QLineEdit(self.widget_123)
        self.water_end_le_11.setObjectName(u"water_end_le_11")
        self.water_end_le_11.setMinimumSize(QSize(0, 35))
        self.water_end_le_11.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_65.addWidget(self.water_end_le_11)

        self.label_96 = QLabel(self.widget_123)
        self.label_96.setObjectName(u"label_96")

        self.horizontalLayout_65.addWidget(self.label_96)


        self.horizontalLayout_66.addWidget(self.widget_123)


        self.verticalLayout_14.addWidget(self.widget_63)

        self.widget_61 = QWidget(self.col_wg_2)
        self.widget_61.setObjectName(u"widget_61")
        self.horizontalLayout_71 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_71.setSpacing(5)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(1, 1, 1, 1)
        self.water_btn_12 = QPushButton(self.widget_61)
        self.water_btn_12.setObjectName(u"water_btn_12")
        self.water_btn_12.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_71.addWidget(self.water_btn_12)

        self.widget_124 = QWidget(self.widget_61)
        self.widget_124.setObjectName(u"widget_124")
        self.widget_124.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_67 = QHBoxLayout(self.widget_124)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(2, 2, 2, 2)
        self.label_97 = QLabel(self.widget_124)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_67.addWidget(self.label_97)

        self.water_start_le_12 = QLineEdit(self.widget_124)
        self.water_start_le_12.setObjectName(u"water_start_le_12")
        self.water_start_le_12.setMinimumSize(QSize(0, 35))
        self.water_start_le_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_67.addWidget(self.water_start_le_12)

        self.label_98 = QLabel(self.widget_124)
        self.label_98.setObjectName(u"label_98")

        self.horizontalLayout_67.addWidget(self.label_98)


        self.horizontalLayout_71.addWidget(self.widget_124)

        self.widget_125 = QWidget(self.widget_61)
        self.widget_125.setObjectName(u"widget_125")
        self.widget_125.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_68 = QHBoxLayout(self.widget_125)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(2, 2, 2, 2)
        self.label_99 = QLabel(self.widget_125)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_68.addWidget(self.label_99)

        self.water_dur_le_12 = QLineEdit(self.widget_125)
        self.water_dur_le_12.setObjectName(u"water_dur_le_12")
        self.water_dur_le_12.setMinimumSize(QSize(0, 35))
        self.water_dur_le_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_68.addWidget(self.water_dur_le_12)

        self.label_100 = QLabel(self.widget_125)
        self.label_100.setObjectName(u"label_100")

        self.horizontalLayout_68.addWidget(self.label_100)


        self.horizontalLayout_71.addWidget(self.widget_125)

        self.widget_126 = QWidget(self.widget_61)
        self.widget_126.setObjectName(u"widget_126")
        self.widget_126.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_69 = QHBoxLayout(self.widget_126)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(2, 2, 2, 2)
        self.label_101 = QLabel(self.widget_126)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_69.addWidget(self.label_101)

        self.water_interval_le_12 = QLineEdit(self.widget_126)
        self.water_interval_le_12.setObjectName(u"water_interval_le_12")
        self.water_interval_le_12.setMinimumSize(QSize(0, 35))
        self.water_interval_le_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_69.addWidget(self.water_interval_le_12)

        self.label_102 = QLabel(self.widget_126)
        self.label_102.setObjectName(u"label_102")

        self.horizontalLayout_69.addWidget(self.label_102)


        self.horizontalLayout_71.addWidget(self.widget_126)

        self.widget_127 = QWidget(self.widget_61)
        self.widget_127.setObjectName(u"widget_127")
        self.widget_127.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_70 = QHBoxLayout(self.widget_127)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(2, 2, 2, 2)
        self.label_103 = QLabel(self.widget_127)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_70.addWidget(self.label_103)

        self.water_end_le_12 = QLineEdit(self.widget_127)
        self.water_end_le_12.setObjectName(u"water_end_le_12")
        self.water_end_le_12.setMinimumSize(QSize(0, 35))
        self.water_end_le_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_70.addWidget(self.water_end_le_12)

        self.label_104 = QLabel(self.widget_127)
        self.label_104.setObjectName(u"label_104")

        self.horizontalLayout_70.addWidget(self.label_104)


        self.horizontalLayout_71.addWidget(self.widget_127)


        self.verticalLayout_14.addWidget(self.widget_61)

        self.widget_65 = QWidget(self.col_wg_2)
        self.widget_65.setObjectName(u"widget_65")
        self.horizontalLayout_76 = QHBoxLayout(self.widget_65)
        self.horizontalLayout_76.setSpacing(5)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(1, 1, 1, 1)
        self.water_btn_13 = QPushButton(self.widget_65)
        self.water_btn_13.setObjectName(u"water_btn_13")
        self.water_btn_13.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_76.addWidget(self.water_btn_13)

        self.widget_128 = QWidget(self.widget_65)
        self.widget_128.setObjectName(u"widget_128")
        self.widget_128.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_72 = QHBoxLayout(self.widget_128)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(2, 2, 2, 2)
        self.label_105 = QLabel(self.widget_128)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_72.addWidget(self.label_105)

        self.water_start_le_13 = QLineEdit(self.widget_128)
        self.water_start_le_13.setObjectName(u"water_start_le_13")
        self.water_start_le_13.setMinimumSize(QSize(0, 35))
        self.water_start_le_13.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_72.addWidget(self.water_start_le_13)

        self.label_106 = QLabel(self.widget_128)
        self.label_106.setObjectName(u"label_106")

        self.horizontalLayout_72.addWidget(self.label_106)


        self.horizontalLayout_76.addWidget(self.widget_128)

        self.widget_129 = QWidget(self.widget_65)
        self.widget_129.setObjectName(u"widget_129")
        self.widget_129.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_73 = QHBoxLayout(self.widget_129)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(2, 2, 2, 2)
        self.label_107 = QLabel(self.widget_129)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_73.addWidget(self.label_107)

        self.water_dur_le_13 = QLineEdit(self.widget_129)
        self.water_dur_le_13.setObjectName(u"water_dur_le_13")
        self.water_dur_le_13.setMinimumSize(QSize(0, 35))
        self.water_dur_le_13.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_73.addWidget(self.water_dur_le_13)

        self.label_108 = QLabel(self.widget_129)
        self.label_108.setObjectName(u"label_108")

        self.horizontalLayout_73.addWidget(self.label_108)


        self.horizontalLayout_76.addWidget(self.widget_129)

        self.widget_130 = QWidget(self.widget_65)
        self.widget_130.setObjectName(u"widget_130")
        self.widget_130.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_74 = QHBoxLayout(self.widget_130)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(2, 2, 2, 2)
        self.label_109 = QLabel(self.widget_130)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_74.addWidget(self.label_109)

        self.water_interval_le_13 = QLineEdit(self.widget_130)
        self.water_interval_le_13.setObjectName(u"water_interval_le_13")
        self.water_interval_le_13.setMinimumSize(QSize(0, 35))
        self.water_interval_le_13.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_74.addWidget(self.water_interval_le_13)

        self.label_110 = QLabel(self.widget_130)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_74.addWidget(self.label_110)


        self.horizontalLayout_76.addWidget(self.widget_130)

        self.widget_131 = QWidget(self.widget_65)
        self.widget_131.setObjectName(u"widget_131")
        self.widget_131.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_75 = QHBoxLayout(self.widget_131)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(2, 2, 2, 2)
        self.label_111 = QLabel(self.widget_131)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_75.addWidget(self.label_111)

        self.water_end_le_13 = QLineEdit(self.widget_131)
        self.water_end_le_13.setObjectName(u"water_end_le_13")
        self.water_end_le_13.setMinimumSize(QSize(0, 35))
        self.water_end_le_13.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_75.addWidget(self.water_end_le_13)

        self.label_112 = QLabel(self.widget_131)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_75.addWidget(self.label_112)


        self.horizontalLayout_76.addWidget(self.widget_131)


        self.verticalLayout_14.addWidget(self.widget_65)

        self.widget_64 = QWidget(self.col_wg_2)
        self.widget_64.setObjectName(u"widget_64")
        self.horizontalLayout_81 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_81.setSpacing(5)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(1, 1, 1, 1)
        self.water_btn_14 = QPushButton(self.widget_64)
        self.water_btn_14.setObjectName(u"water_btn_14")
        self.water_btn_14.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_81.addWidget(self.water_btn_14)

        self.widget_132 = QWidget(self.widget_64)
        self.widget_132.setObjectName(u"widget_132")
        self.widget_132.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_77 = QHBoxLayout(self.widget_132)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(2, 2, 2, 2)
        self.label_113 = QLabel(self.widget_132)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_77.addWidget(self.label_113)

        self.water_start_le_14 = QLineEdit(self.widget_132)
        self.water_start_le_14.setObjectName(u"water_start_le_14")
        self.water_start_le_14.setMinimumSize(QSize(0, 35))
        self.water_start_le_14.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_77.addWidget(self.water_start_le_14)

        self.label_114 = QLabel(self.widget_132)
        self.label_114.setObjectName(u"label_114")

        self.horizontalLayout_77.addWidget(self.label_114)


        self.horizontalLayout_81.addWidget(self.widget_132)

        self.widget_133 = QWidget(self.widget_64)
        self.widget_133.setObjectName(u"widget_133")
        self.widget_133.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_78 = QHBoxLayout(self.widget_133)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(2, 2, 2, 2)
        self.label_115 = QLabel(self.widget_133)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_78.addWidget(self.label_115)

        self.water_dur_le_14 = QLineEdit(self.widget_133)
        self.water_dur_le_14.setObjectName(u"water_dur_le_14")
        self.water_dur_le_14.setMinimumSize(QSize(0, 35))
        self.water_dur_le_14.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_78.addWidget(self.water_dur_le_14)

        self.label_116 = QLabel(self.widget_133)
        self.label_116.setObjectName(u"label_116")

        self.horizontalLayout_78.addWidget(self.label_116)


        self.horizontalLayout_81.addWidget(self.widget_133)

        self.widget_134 = QWidget(self.widget_64)
        self.widget_134.setObjectName(u"widget_134")
        self.widget_134.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_79 = QHBoxLayout(self.widget_134)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(2, 2, 2, 2)
        self.label_117 = QLabel(self.widget_134)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_79.addWidget(self.label_117)

        self.water_interval_le_14 = QLineEdit(self.widget_134)
        self.water_interval_le_14.setObjectName(u"water_interval_le_14")
        self.water_interval_le_14.setMinimumSize(QSize(0, 35))
        self.water_interval_le_14.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_79.addWidget(self.water_interval_le_14)

        self.label_118 = QLabel(self.widget_134)
        self.label_118.setObjectName(u"label_118")

        self.horizontalLayout_79.addWidget(self.label_118)


        self.horizontalLayout_81.addWidget(self.widget_134)

        self.widget_135 = QWidget(self.widget_64)
        self.widget_135.setObjectName(u"widget_135")
        self.widget_135.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_80 = QHBoxLayout(self.widget_135)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(2, 2, 2, 2)
        self.label_119 = QLabel(self.widget_135)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_80.addWidget(self.label_119)

        self.water_end_le_14 = QLineEdit(self.widget_135)
        self.water_end_le_14.setObjectName(u"water_end_le_14")
        self.water_end_le_14.setMinimumSize(QSize(0, 35))
        self.water_end_le_14.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_80.addWidget(self.water_end_le_14)

        self.label_120 = QLabel(self.widget_135)
        self.label_120.setObjectName(u"label_120")

        self.horizontalLayout_80.addWidget(self.label_120)


        self.horizontalLayout_81.addWidget(self.widget_135)


        self.verticalLayout_14.addWidget(self.widget_64)


        self.verticalLayout_12.addWidget(self.col_wg_2)

        self.widget_79 = QWidget(self.scrollAreaWidgetContents)
        self.widget_79.setObjectName(u"widget_79")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.label_3 = QLabel(self.widget_79)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_12.addWidget(self.label_3)

        self.water_col_btn_3 = QPushButton(self.widget_79)
        self.water_col_btn_3.setObjectName(u"water_col_btn_3")
        self.water_col_btn_3.setMinimumSize(QSize(0, 40))
        self.water_col_btn_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.water_col_btn_3)

        self.fill_column_btn_3 = QPushButton(self.widget_79)
        self.fill_column_btn_3.setObjectName(u"fill_column_btn_3")
        self.fill_column_btn_3.setMinimumSize(QSize(0, 40))
        self.fill_column_btn_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.fill_column_btn_3)


        self.verticalLayout_12.addWidget(self.widget_79)

        self.col_wg_3 = QWidget(self.scrollAreaWidgetContents)
        self.col_wg_3.setObjectName(u"col_wg_3")
        self.col_wg_3.setMinimumSize(QSize(0, 474))
        self.verticalLayout_15 = QVBoxLayout(self.col_wg_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.widget_69 = QWidget(self.col_wg_3)
        self.widget_69.setObjectName(u"widget_69")
        self.horizontalLayout_86 = QHBoxLayout(self.widget_69)
        self.horizontalLayout_86.setSpacing(5)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(1, 1, 1, 1)
        self.water_btn_15 = QPushButton(self.widget_69)
        self.water_btn_15.setObjectName(u"water_btn_15")
        self.water_btn_15.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_86.addWidget(self.water_btn_15)

        self.widget_136 = QWidget(self.widget_69)
        self.widget_136.setObjectName(u"widget_136")
        self.widget_136.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_82 = QHBoxLayout(self.widget_136)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(2, 2, 2, 2)
        self.label_121 = QLabel(self.widget_136)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_82.addWidget(self.label_121)

        self.water_start_le_15 = QLineEdit(self.widget_136)
        self.water_start_le_15.setObjectName(u"water_start_le_15")
        self.water_start_le_15.setMinimumSize(QSize(0, 35))
        self.water_start_le_15.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_82.addWidget(self.water_start_le_15)

        self.label_122 = QLabel(self.widget_136)
        self.label_122.setObjectName(u"label_122")

        self.horizontalLayout_82.addWidget(self.label_122)


        self.horizontalLayout_86.addWidget(self.widget_136)

        self.widget_137 = QWidget(self.widget_69)
        self.widget_137.setObjectName(u"widget_137")
        self.widget_137.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_83 = QHBoxLayout(self.widget_137)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(2, 2, 2, 2)
        self.label_123 = QLabel(self.widget_137)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_83.addWidget(self.label_123)

        self.water_dur_le_15 = QLineEdit(self.widget_137)
        self.water_dur_le_15.setObjectName(u"water_dur_le_15")
        self.water_dur_le_15.setMinimumSize(QSize(0, 35))
        self.water_dur_le_15.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_83.addWidget(self.water_dur_le_15)

        self.label_124 = QLabel(self.widget_137)
        self.label_124.setObjectName(u"label_124")

        self.horizontalLayout_83.addWidget(self.label_124)


        self.horizontalLayout_86.addWidget(self.widget_137)

        self.widget_138 = QWidget(self.widget_69)
        self.widget_138.setObjectName(u"widget_138")
        self.widget_138.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_84 = QHBoxLayout(self.widget_138)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(2, 2, 2, 2)
        self.label_125 = QLabel(self.widget_138)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_84.addWidget(self.label_125)

        self.water_interval_le_15 = QLineEdit(self.widget_138)
        self.water_interval_le_15.setObjectName(u"water_interval_le_15")
        self.water_interval_le_15.setMinimumSize(QSize(0, 35))
        self.water_interval_le_15.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_84.addWidget(self.water_interval_le_15)

        self.label_126 = QLabel(self.widget_138)
        self.label_126.setObjectName(u"label_126")

        self.horizontalLayout_84.addWidget(self.label_126)


        self.horizontalLayout_86.addWidget(self.widget_138)

        self.widget_139 = QWidget(self.widget_69)
        self.widget_139.setObjectName(u"widget_139")
        self.widget_139.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_85 = QHBoxLayout(self.widget_139)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(2, 2, 2, 2)
        self.label_127 = QLabel(self.widget_139)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_85.addWidget(self.label_127)

        self.water_end_le_15 = QLineEdit(self.widget_139)
        self.water_end_le_15.setObjectName(u"water_end_le_15")
        self.water_end_le_15.setMinimumSize(QSize(0, 35))
        self.water_end_le_15.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_85.addWidget(self.water_end_le_15)

        self.label_128 = QLabel(self.widget_139)
        self.label_128.setObjectName(u"label_128")

        self.horizontalLayout_85.addWidget(self.label_128)


        self.horizontalLayout_86.addWidget(self.widget_139)


        self.verticalLayout_15.addWidget(self.widget_69)

        self.widget_73 = QWidget(self.col_wg_3)
        self.widget_73.setObjectName(u"widget_73")
        self.horizontalLayout_91 = QHBoxLayout(self.widget_73)
        self.horizontalLayout_91.setSpacing(5)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(1, 1, 1, 1)
        self.water_btn_16 = QPushButton(self.widget_73)
        self.water_btn_16.setObjectName(u"water_btn_16")
        self.water_btn_16.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_91.addWidget(self.water_btn_16)

        self.widget_140 = QWidget(self.widget_73)
        self.widget_140.setObjectName(u"widget_140")
        self.widget_140.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_87 = QHBoxLayout(self.widget_140)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(2, 2, 2, 2)
        self.label_129 = QLabel(self.widget_140)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_87.addWidget(self.label_129)

        self.water_start_le_16 = QLineEdit(self.widget_140)
        self.water_start_le_16.setObjectName(u"water_start_le_16")
        self.water_start_le_16.setMinimumSize(QSize(0, 35))
        self.water_start_le_16.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_87.addWidget(self.water_start_le_16)

        self.label_130 = QLabel(self.widget_140)
        self.label_130.setObjectName(u"label_130")

        self.horizontalLayout_87.addWidget(self.label_130)


        self.horizontalLayout_91.addWidget(self.widget_140)

        self.widget_141 = QWidget(self.widget_73)
        self.widget_141.setObjectName(u"widget_141")
        self.widget_141.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_88 = QHBoxLayout(self.widget_141)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(2, 2, 2, 2)
        self.label_131 = QLabel(self.widget_141)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_88.addWidget(self.label_131)

        self.water_dur_le_16 = QLineEdit(self.widget_141)
        self.water_dur_le_16.setObjectName(u"water_dur_le_16")
        self.water_dur_le_16.setMinimumSize(QSize(0, 35))
        self.water_dur_le_16.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_88.addWidget(self.water_dur_le_16)

        self.label_132 = QLabel(self.widget_141)
        self.label_132.setObjectName(u"label_132")

        self.horizontalLayout_88.addWidget(self.label_132)


        self.horizontalLayout_91.addWidget(self.widget_141)

        self.widget_142 = QWidget(self.widget_73)
        self.widget_142.setObjectName(u"widget_142")
        self.widget_142.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_89 = QHBoxLayout(self.widget_142)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(2, 2, 2, 2)
        self.label_133 = QLabel(self.widget_142)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_89.addWidget(self.label_133)

        self.water_interval_le_16 = QLineEdit(self.widget_142)
        self.water_interval_le_16.setObjectName(u"water_interval_le_16")
        self.water_interval_le_16.setMinimumSize(QSize(0, 35))
        self.water_interval_le_16.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_89.addWidget(self.water_interval_le_16)

        self.label_134 = QLabel(self.widget_142)
        self.label_134.setObjectName(u"label_134")

        self.horizontalLayout_89.addWidget(self.label_134)


        self.horizontalLayout_91.addWidget(self.widget_142)

        self.widget_143 = QWidget(self.widget_73)
        self.widget_143.setObjectName(u"widget_143")
        self.widget_143.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_90 = QHBoxLayout(self.widget_143)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(2, 2, 2, 2)
        self.label_135 = QLabel(self.widget_143)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_90.addWidget(self.label_135)

        self.water_end_le_16 = QLineEdit(self.widget_143)
        self.water_end_le_16.setObjectName(u"water_end_le_16")
        self.water_end_le_16.setMinimumSize(QSize(0, 35))
        self.water_end_le_16.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_90.addWidget(self.water_end_le_16)

        self.label_136 = QLabel(self.widget_143)
        self.label_136.setObjectName(u"label_136")

        self.horizontalLayout_90.addWidget(self.label_136)


        self.horizontalLayout_91.addWidget(self.widget_143)


        self.verticalLayout_15.addWidget(self.widget_73)

        self.widget_67 = QWidget(self.col_wg_3)
        self.widget_67.setObjectName(u"widget_67")
        self.horizontalLayout_96 = QHBoxLayout(self.widget_67)
        self.horizontalLayout_96.setSpacing(5)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(1, 1, 1, 1)
        self.water_btn_17 = QPushButton(self.widget_67)
        self.water_btn_17.setObjectName(u"water_btn_17")
        self.water_btn_17.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_96.addWidget(self.water_btn_17)

        self.widget_144 = QWidget(self.widget_67)
        self.widget_144.setObjectName(u"widget_144")
        self.widget_144.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_92 = QHBoxLayout(self.widget_144)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(2, 2, 2, 2)
        self.label_137 = QLabel(self.widget_144)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_92.addWidget(self.label_137)

        self.water_start_le_17 = QLineEdit(self.widget_144)
        self.water_start_le_17.setObjectName(u"water_start_le_17")
        self.water_start_le_17.setMinimumSize(QSize(0, 35))
        self.water_start_le_17.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_92.addWidget(self.water_start_le_17)

        self.label_138 = QLabel(self.widget_144)
        self.label_138.setObjectName(u"label_138")

        self.horizontalLayout_92.addWidget(self.label_138)


        self.horizontalLayout_96.addWidget(self.widget_144)

        self.widget_145 = QWidget(self.widget_67)
        self.widget_145.setObjectName(u"widget_145")
        self.widget_145.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_93 = QHBoxLayout(self.widget_145)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(2, 2, 2, 2)
        self.label_139 = QLabel(self.widget_145)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_93.addWidget(self.label_139)

        self.water_dur_le_17 = QLineEdit(self.widget_145)
        self.water_dur_le_17.setObjectName(u"water_dur_le_17")
        self.water_dur_le_17.setMinimumSize(QSize(0, 35))
        self.water_dur_le_17.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_93.addWidget(self.water_dur_le_17)

        self.label_140 = QLabel(self.widget_145)
        self.label_140.setObjectName(u"label_140")

        self.horizontalLayout_93.addWidget(self.label_140)


        self.horizontalLayout_96.addWidget(self.widget_145)

        self.widget_146 = QWidget(self.widget_67)
        self.widget_146.setObjectName(u"widget_146")
        self.widget_146.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_94 = QHBoxLayout(self.widget_146)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(2, 2, 2, 2)
        self.label_141 = QLabel(self.widget_146)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_94.addWidget(self.label_141)

        self.water_interval_le_17 = QLineEdit(self.widget_146)
        self.water_interval_le_17.setObjectName(u"water_interval_le_17")
        self.water_interval_le_17.setMinimumSize(QSize(0, 35))
        self.water_interval_le_17.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_94.addWidget(self.water_interval_le_17)

        self.label_142 = QLabel(self.widget_146)
        self.label_142.setObjectName(u"label_142")

        self.horizontalLayout_94.addWidget(self.label_142)


        self.horizontalLayout_96.addWidget(self.widget_146)

        self.widget_147 = QWidget(self.widget_67)
        self.widget_147.setObjectName(u"widget_147")
        self.widget_147.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_95 = QHBoxLayout(self.widget_147)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(2, 2, 2, 2)
        self.label_143 = QLabel(self.widget_147)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_95.addWidget(self.label_143)

        self.water_end_le_17 = QLineEdit(self.widget_147)
        self.water_end_le_17.setObjectName(u"water_end_le_17")
        self.water_end_le_17.setMinimumSize(QSize(0, 35))
        self.water_end_le_17.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_95.addWidget(self.water_end_le_17)

        self.label_144 = QLabel(self.widget_147)
        self.label_144.setObjectName(u"label_144")

        self.horizontalLayout_95.addWidget(self.label_144)


        self.horizontalLayout_96.addWidget(self.widget_147)


        self.verticalLayout_15.addWidget(self.widget_67)

        self.widget_70 = QWidget(self.col_wg_3)
        self.widget_70.setObjectName(u"widget_70")
        self.horizontalLayout_101 = QHBoxLayout(self.widget_70)
        self.horizontalLayout_101.setSpacing(5)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(1, 1, 1, 1)
        self.water_btn_18 = QPushButton(self.widget_70)
        self.water_btn_18.setObjectName(u"water_btn_18")
        self.water_btn_18.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_101.addWidget(self.water_btn_18)

        self.widget_148 = QWidget(self.widget_70)
        self.widget_148.setObjectName(u"widget_148")
        self.widget_148.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_97 = QHBoxLayout(self.widget_148)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(2, 2, 2, 2)
        self.label_145 = QLabel(self.widget_148)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_97.addWidget(self.label_145)

        self.water_start_le_18 = QLineEdit(self.widget_148)
        self.water_start_le_18.setObjectName(u"water_start_le_18")
        self.water_start_le_18.setMinimumSize(QSize(0, 35))
        self.water_start_le_18.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_97.addWidget(self.water_start_le_18)

        self.label_146 = QLabel(self.widget_148)
        self.label_146.setObjectName(u"label_146")

        self.horizontalLayout_97.addWidget(self.label_146)


        self.horizontalLayout_101.addWidget(self.widget_148)

        self.widget_149 = QWidget(self.widget_70)
        self.widget_149.setObjectName(u"widget_149")
        self.widget_149.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_98 = QHBoxLayout(self.widget_149)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(2, 2, 2, 2)
        self.label_147 = QLabel(self.widget_149)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_98.addWidget(self.label_147)

        self.water_dur_le_18 = QLineEdit(self.widget_149)
        self.water_dur_le_18.setObjectName(u"water_dur_le_18")
        self.water_dur_le_18.setMinimumSize(QSize(0, 35))
        self.water_dur_le_18.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_98.addWidget(self.water_dur_le_18)

        self.label_148 = QLabel(self.widget_149)
        self.label_148.setObjectName(u"label_148")

        self.horizontalLayout_98.addWidget(self.label_148)


        self.horizontalLayout_101.addWidget(self.widget_149)

        self.widget_150 = QWidget(self.widget_70)
        self.widget_150.setObjectName(u"widget_150")
        self.widget_150.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_99 = QHBoxLayout(self.widget_150)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(2, 2, 2, 2)
        self.label_149 = QLabel(self.widget_150)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_99.addWidget(self.label_149)

        self.water_interval_le_18 = QLineEdit(self.widget_150)
        self.water_interval_le_18.setObjectName(u"water_interval_le_18")
        self.water_interval_le_18.setMinimumSize(QSize(0, 35))
        self.water_interval_le_18.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_99.addWidget(self.water_interval_le_18)

        self.label_150 = QLabel(self.widget_150)
        self.label_150.setObjectName(u"label_150")

        self.horizontalLayout_99.addWidget(self.label_150)


        self.horizontalLayout_101.addWidget(self.widget_150)

        self.widget_151 = QWidget(self.widget_70)
        self.widget_151.setObjectName(u"widget_151")
        self.widget_151.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_100 = QHBoxLayout(self.widget_151)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(2, 2, 2, 2)
        self.label_151 = QLabel(self.widget_151)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_100.addWidget(self.label_151)

        self.water_end_le_18 = QLineEdit(self.widget_151)
        self.water_end_le_18.setObjectName(u"water_end_le_18")
        self.water_end_le_18.setMinimumSize(QSize(0, 35))
        self.water_end_le_18.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_100.addWidget(self.water_end_le_18)

        self.label_152 = QLabel(self.widget_151)
        self.label_152.setObjectName(u"label_152")

        self.horizontalLayout_100.addWidget(self.label_152)


        self.horizontalLayout_101.addWidget(self.widget_151)


        self.verticalLayout_15.addWidget(self.widget_70)

        self.widget_68 = QWidget(self.col_wg_3)
        self.widget_68.setObjectName(u"widget_68")
        self.horizontalLayout_106 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_106.setSpacing(5)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(1, 1, 1, 1)
        self.water_btn_19 = QPushButton(self.widget_68)
        self.water_btn_19.setObjectName(u"water_btn_19")
        self.water_btn_19.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_106.addWidget(self.water_btn_19)

        self.widget_152 = QWidget(self.widget_68)
        self.widget_152.setObjectName(u"widget_152")
        self.widget_152.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_102 = QHBoxLayout(self.widget_152)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(2, 2, 2, 2)
        self.label_153 = QLabel(self.widget_152)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_102.addWidget(self.label_153)

        self.water_start_le_19 = QLineEdit(self.widget_152)
        self.water_start_le_19.setObjectName(u"water_start_le_19")
        self.water_start_le_19.setMinimumSize(QSize(0, 35))
        self.water_start_le_19.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_102.addWidget(self.water_start_le_19)

        self.label_154 = QLabel(self.widget_152)
        self.label_154.setObjectName(u"label_154")

        self.horizontalLayout_102.addWidget(self.label_154)


        self.horizontalLayout_106.addWidget(self.widget_152)

        self.widget_153 = QWidget(self.widget_68)
        self.widget_153.setObjectName(u"widget_153")
        self.widget_153.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_103 = QHBoxLayout(self.widget_153)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(2, 2, 2, 2)
        self.label_155 = QLabel(self.widget_153)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_103.addWidget(self.label_155)

        self.water_dur_le_19 = QLineEdit(self.widget_153)
        self.water_dur_le_19.setObjectName(u"water_dur_le_19")
        self.water_dur_le_19.setMinimumSize(QSize(0, 35))
        self.water_dur_le_19.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_103.addWidget(self.water_dur_le_19)

        self.label_156 = QLabel(self.widget_153)
        self.label_156.setObjectName(u"label_156")

        self.horizontalLayout_103.addWidget(self.label_156)


        self.horizontalLayout_106.addWidget(self.widget_153)

        self.widget_154 = QWidget(self.widget_68)
        self.widget_154.setObjectName(u"widget_154")
        self.widget_154.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_104 = QHBoxLayout(self.widget_154)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(2, 2, 2, 2)
        self.label_157 = QLabel(self.widget_154)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_104.addWidget(self.label_157)

        self.water_interval_le_19 = QLineEdit(self.widget_154)
        self.water_interval_le_19.setObjectName(u"water_interval_le_19")
        self.water_interval_le_19.setMinimumSize(QSize(0, 35))
        self.water_interval_le_19.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_104.addWidget(self.water_interval_le_19)

        self.label_158 = QLabel(self.widget_154)
        self.label_158.setObjectName(u"label_158")

        self.horizontalLayout_104.addWidget(self.label_158)


        self.horizontalLayout_106.addWidget(self.widget_154)

        self.widget_155 = QWidget(self.widget_68)
        self.widget_155.setObjectName(u"widget_155")
        self.widget_155.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_105 = QHBoxLayout(self.widget_155)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(2, 2, 2, 2)
        self.label_159 = QLabel(self.widget_155)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_105.addWidget(self.label_159)

        self.water_end_le_19 = QLineEdit(self.widget_155)
        self.water_end_le_19.setObjectName(u"water_end_le_19")
        self.water_end_le_19.setMinimumSize(QSize(0, 35))
        self.water_end_le_19.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_105.addWidget(self.water_end_le_19)

        self.label_160 = QLabel(self.widget_155)
        self.label_160.setObjectName(u"label_160")

        self.horizontalLayout_105.addWidget(self.label_160)


        self.horizontalLayout_106.addWidget(self.widget_155)


        self.verticalLayout_15.addWidget(self.widget_68)

        self.widget_72 = QWidget(self.col_wg_3)
        self.widget_72.setObjectName(u"widget_72")
        self.horizontalLayout_111 = QHBoxLayout(self.widget_72)
        self.horizontalLayout_111.setSpacing(5)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(1, 1, 1, 1)
        self.water_btn_20 = QPushButton(self.widget_72)
        self.water_btn_20.setObjectName(u"water_btn_20")
        self.water_btn_20.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_111.addWidget(self.water_btn_20)

        self.widget_156 = QWidget(self.widget_72)
        self.widget_156.setObjectName(u"widget_156")
        self.widget_156.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_107 = QHBoxLayout(self.widget_156)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(2, 2, 2, 2)
        self.label_161 = QLabel(self.widget_156)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_107.addWidget(self.label_161)

        self.water_start_le_20 = QLineEdit(self.widget_156)
        self.water_start_le_20.setObjectName(u"water_start_le_20")
        self.water_start_le_20.setMinimumSize(QSize(0, 35))
        self.water_start_le_20.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_107.addWidget(self.water_start_le_20)

        self.label_162 = QLabel(self.widget_156)
        self.label_162.setObjectName(u"label_162")

        self.horizontalLayout_107.addWidget(self.label_162)


        self.horizontalLayout_111.addWidget(self.widget_156)

        self.widget_157 = QWidget(self.widget_72)
        self.widget_157.setObjectName(u"widget_157")
        self.widget_157.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_108 = QHBoxLayout(self.widget_157)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(2, 2, 2, 2)
        self.label_163 = QLabel(self.widget_157)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_108.addWidget(self.label_163)

        self.water_dur_le_20 = QLineEdit(self.widget_157)
        self.water_dur_le_20.setObjectName(u"water_dur_le_20")
        self.water_dur_le_20.setMinimumSize(QSize(0, 35))
        self.water_dur_le_20.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_108.addWidget(self.water_dur_le_20)

        self.label_164 = QLabel(self.widget_157)
        self.label_164.setObjectName(u"label_164")

        self.horizontalLayout_108.addWidget(self.label_164)


        self.horizontalLayout_111.addWidget(self.widget_157)

        self.widget_158 = QWidget(self.widget_72)
        self.widget_158.setObjectName(u"widget_158")
        self.widget_158.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_109 = QHBoxLayout(self.widget_158)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(2, 2, 2, 2)
        self.label_165 = QLabel(self.widget_158)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_109.addWidget(self.label_165)

        self.water_interval_le_20 = QLineEdit(self.widget_158)
        self.water_interval_le_20.setObjectName(u"water_interval_le_20")
        self.water_interval_le_20.setMinimumSize(QSize(0, 35))
        self.water_interval_le_20.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_109.addWidget(self.water_interval_le_20)

        self.label_166 = QLabel(self.widget_158)
        self.label_166.setObjectName(u"label_166")

        self.horizontalLayout_109.addWidget(self.label_166)


        self.horizontalLayout_111.addWidget(self.widget_158)

        self.widget_159 = QWidget(self.widget_72)
        self.widget_159.setObjectName(u"widget_159")
        self.widget_159.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_110 = QHBoxLayout(self.widget_159)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(2, 2, 2, 2)
        self.label_167 = QLabel(self.widget_159)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_110.addWidget(self.label_167)

        self.water_end_le_20 = QLineEdit(self.widget_159)
        self.water_end_le_20.setObjectName(u"water_end_le_20")
        self.water_end_le_20.setMinimumSize(QSize(0, 35))
        self.water_end_le_20.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_110.addWidget(self.water_end_le_20)

        self.label_168 = QLabel(self.widget_159)
        self.label_168.setObjectName(u"label_168")

        self.horizontalLayout_110.addWidget(self.label_168)


        self.horizontalLayout_111.addWidget(self.widget_159)


        self.verticalLayout_15.addWidget(self.widget_72)

        self.widget_71 = QWidget(self.col_wg_3)
        self.widget_71.setObjectName(u"widget_71")
        self.horizontalLayout_116 = QHBoxLayout(self.widget_71)
        self.horizontalLayout_116.setSpacing(5)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(1, 1, 1, 1)
        self.water_btn_21 = QPushButton(self.widget_71)
        self.water_btn_21.setObjectName(u"water_btn_21")
        self.water_btn_21.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_116.addWidget(self.water_btn_21)

        self.widget_160 = QWidget(self.widget_71)
        self.widget_160.setObjectName(u"widget_160")
        self.widget_160.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_112 = QHBoxLayout(self.widget_160)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(2, 2, 2, 2)
        self.label_169 = QLabel(self.widget_160)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_112.addWidget(self.label_169)

        self.water_start_le_21 = QLineEdit(self.widget_160)
        self.water_start_le_21.setObjectName(u"water_start_le_21")
        self.water_start_le_21.setMinimumSize(QSize(0, 35))
        self.water_start_le_21.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_112.addWidget(self.water_start_le_21)

        self.label_170 = QLabel(self.widget_160)
        self.label_170.setObjectName(u"label_170")

        self.horizontalLayout_112.addWidget(self.label_170)


        self.horizontalLayout_116.addWidget(self.widget_160)

        self.widget_161 = QWidget(self.widget_71)
        self.widget_161.setObjectName(u"widget_161")
        self.widget_161.setMaximumSize(QSize(160, 16777215))
        self.horizontalLayout_113 = QHBoxLayout(self.widget_161)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(2, 2, 2, 2)
        self.label_171 = QLabel(self.widget_161)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_113.addWidget(self.label_171)

        self.water_dur_le_21 = QLineEdit(self.widget_161)
        self.water_dur_le_21.setObjectName(u"water_dur_le_21")
        self.water_dur_le_21.setMinimumSize(QSize(0, 35))
        self.water_dur_le_21.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_113.addWidget(self.water_dur_le_21)

        self.label_172 = QLabel(self.widget_161)
        self.label_172.setObjectName(u"label_172")

        self.horizontalLayout_113.addWidget(self.label_172)


        self.horizontalLayout_116.addWidget(self.widget_161)

        self.widget_162 = QWidget(self.widget_71)
        self.widget_162.setObjectName(u"widget_162")
        self.widget_162.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_114 = QHBoxLayout(self.widget_162)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(2, 2, 2, 2)
        self.label_173 = QLabel(self.widget_162)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_114.addWidget(self.label_173)

        self.water_interval_le_21 = QLineEdit(self.widget_162)
        self.water_interval_le_21.setObjectName(u"water_interval_le_21")
        self.water_interval_le_21.setMinimumSize(QSize(0, 35))
        self.water_interval_le_21.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_114.addWidget(self.water_interval_le_21)

        self.label_174 = QLabel(self.widget_162)
        self.label_174.setObjectName(u"label_174")

        self.horizontalLayout_114.addWidget(self.label_174)


        self.horizontalLayout_116.addWidget(self.widget_162)

        self.widget_163 = QWidget(self.widget_71)
        self.widget_163.setObjectName(u"widget_163")
        self.widget_163.setMaximumSize(QSize(190, 16777215))
        self.horizontalLayout_115 = QHBoxLayout(self.widget_163)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(2, 2, 2, 2)
        self.label_175 = QLabel(self.widget_163)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_115.addWidget(self.label_175)

        self.water_end_le_21 = QLineEdit(self.widget_163)
        self.water_end_le_21.setObjectName(u"water_end_le_21")
        self.water_end_le_21.setMinimumSize(QSize(0, 35))
        self.water_end_le_21.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_115.addWidget(self.water_end_le_21)

        self.label_176 = QLabel(self.widget_163)
        self.label_176.setObjectName(u"label_176")

        self.horizontalLayout_115.addWidget(self.label_176)


        self.horizontalLayout_116.addWidget(self.widget_163)


        self.verticalLayout_15.addWidget(self.widget_71)


        self.verticalLayout_12.addWidget(self.col_wg_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.watering_pg)
        self.camera_pg = QWidget()
        self.camera_pg.setObjectName(u"camera_pg")
        self.verticalLayout_5 = QVBoxLayout(self.camera_pg)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_6 = QWidget(self.camera_pg)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.cam_dir_le = QLineEdit(self.widget_6)
        self.cam_dir_le.setObjectName(u"cam_dir_le")
        self.cam_dir_le.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.cam_dir_le)

        self.cam_dir_btn = QPushButton(self.widget_6)
        self.cam_dir_btn.setObjectName(u"cam_dir_btn")
        self.cam_dir_btn.setMinimumSize(QSize(40, 35))
        self.cam_dir_btn.setIconSize(QSize(40, 35))

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

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_4j_btn.setText("")
        self.watering_page_btn.setText(QCoreApplication.translate("MainWindow", u"Zavla\u017eov\u00e1n\u00ed", None))
        self.solutio_page_btn.setText(QCoreApplication.translate("MainWindow", u"Nastaven\u00ed roztoku", None))
        self.cams_page_btn.setText(QCoreApplication.translate("MainWindow", u"Kamery", None))
        self.chart_page_btn.setText(QCoreApplication.translate("MainWindow", u"Grafy", None))
        self.expand_menu_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.solution_dir_btn.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit do csv", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit nastaven\u00ed", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"???", None))
        self.water_all_btn.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt v\u0161e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sloupec 1:", None))
        self.water_col_btn_1.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt sloupec", None))
        self.fill_column_btn_1.setText(QCoreApplication.translate("MainWindow", u"Nastavit sloupec", None))
        self.water_btn_1.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_2.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_3.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_4.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_5.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_6.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_7.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sloupec 2:", None))
        self.water_col_btn_2.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt sloupec", None))
        self.fill_column_btn_2.setText(QCoreApplication.translate("MainWindow", u"Nastavit sloupec", None))
        self.water_btn_8.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_9.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_10.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_11.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_12.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_13.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_14.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sloupec 3:", None))
        self.water_col_btn_3.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt sloupec", None))
        self.fill_column_btn_3.setText(QCoreApplication.translate("MainWindow", u"Nastavit sloupec", None))
        self.water_btn_15.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_16.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_17.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_18.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_19.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_20.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.water_btn_21.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cam_dir_btn.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit sn\u00edmek", None))
    # retranslateUi

