# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Green_wallnGskzc.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

from Gui.Custom_widgets.toggle import AnimatedToggle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1482, 873)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"font: 11pt \\\"Yu Gothic UI\\\";\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgb(180, 180, 180);\n"
"	border-radius: 5px;\n"
"	\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #729D1F;\n"
"}\n"
"\n"
"#widget, #widget_2, #widget_6, #widget_10, #widget_40, #widget_39, #widget_38, #widget_32, #widget_31,#widget_30, #widget_75, #widget_14, #widget_77, #widget_78, #widget_79, #widget_190, #scrollArea{\n"
"	border: 1px solid #ccc;\n"
"}\n"
"\n"
"#widget_165{\n"
"background-color: #ccc;\n"
"}\n"
"        \n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border-image: url(:/images/up_arrow_disabled.png);\n"
"}\n"
"        \n"
"QScrollBar::add-line:vertical\n"
"{\n"
"     border-image: url(:/ima"
                        "ges/down_arrow_disabled.png);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(180, 16777215))
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: #ccc;\n"
"}\n"
"")
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
        self.widget_4.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #729D1F;\n"
"}")
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

        self.solution_config_btn = QPushButton(self.widget_4)
        self.solution_config_btn.setObjectName(u"solution_config_btn")
        self.solution_config_btn.setEnabled(True)
        self.solution_config_btn.setMinimumSize(QSize(0, 0))
        self.solution_config_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.solution_config_btn)

        self.cams_page_btn = QPushButton(self.widget_4)
        self.cams_page_btn.setObjectName(u"cams_page_btn")
        self.cams_page_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.cams_page_btn)

        self.chart_page_btn = QPushButton(self.widget_4)
        self.chart_page_btn.setObjectName(u"chart_page_btn")
        self.chart_page_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.chart_page_btn)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_1 = QWidget(self.widget)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setEnabled(True)
        self.widget_1.setMaximumSize(QSize(16777215, 150))
        self.widget_1.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #FF3636;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FF2626;\n"
"}")
        self.horizontalLayout_143 = QHBoxLayout(self.widget_1)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.stop_watering_btn = QPushButton(self.widget_1)
        self.stop_watering_btn.setObjectName(u"stop_watering_btn")
        self.stop_watering_btn.setEnabled(True)
        self.stop_watering_btn.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_143.addWidget(self.stop_watering_btn)


        self.verticalLayout.addWidget(self.widget_1)


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
        self.stackedWidget.setEnabled(True)
        self.solution_pg = QWidget()
        self.solution_pg.setObjectName(u"solution_pg")
        self.verticalLayout_8 = QVBoxLayout(self.solution_pg)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_10 = QWidget(self.solution_pg)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_176 = QLabel(self.widget_10)
        self.label_176.setObjectName(u"label_176")

        self.horizontalLayout_4.addWidget(self.label_176)

        self.dir_name_le = QLineEdit(self.widget_10)
        self.dir_name_le.setObjectName(u"dir_name_le")
        self.dir_name_le.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_4.addWidget(self.dir_name_le)

        self.dir_name_btn = QPushButton(self.widget_10)
        self.dir_name_btn.setObjectName(u"dir_name_btn")
        self.dir_name_btn.setMinimumSize(QSize(110, 0))
        self.dir_name_btn.setMaximumSize(QSize(120, 35))

        self.horizontalLayout_4.addWidget(self.dir_name_btn)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

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

        self.stop_saving_btn = QPushButton(self.widget_10)
        self.stop_saving_btn.setObjectName(u"stop_saving_btn")
        self.stop_saving_btn.setMinimumSize(QSize(100, 35))

        self.horizontalLayout_4.addWidget(self.stop_saving_btn)

        self.start_saving_btn = QPushButton(self.widget_10)
        self.start_saving_btn.setObjectName(u"start_saving_btn")
        self.start_saving_btn.setMinimumSize(QSize(100, 35))

        self.horizontalLayout_4.addWidget(self.start_saving_btn)


        self.verticalLayout_8.addWidget(self.widget_10)

        self.widget_35 = QWidget(self.solution_pg)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 1, -1, 1)
        self.widget_166 = QWidget(self.widget_35)
        self.widget_166.setObjectName(u"widget_166")
        self.widget_166.setMaximumSize(QSize(1100, 16777215))
        self.horizontalLayout_141 = QHBoxLayout(self.widget_166)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(-1, 0, -1, 0)
        self.widget_39 = QWidget(self.widget_166)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMaximumSize(QSize(360, 16777215))
        self.verticalLayout_18 = QVBoxLayout(self.widget_39)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(1, 1, 1, 1)
        self.label_185 = QLabel(self.widget_39)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setMaximumSize(QSize(16777215, 20))
        self.label_185.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_185)

        self.widget_22 = QWidget(self.widget_39)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_123 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.label_186 = QLabel(self.widget_22)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_123.addWidget(self.label_186)

        self.wall_tep_lbl = QLabel(self.widget_22)
        self.wall_tep_lbl.setObjectName(u"wall_tep_lbl")
        self.wall_tep_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_123.addWidget(self.wall_tep_lbl)

        self.label_178 = QLabel(self.widget_22)
        self.label_178.setObjectName(u"label_178")

        self.horizontalLayout_123.addWidget(self.label_178)


        self.verticalLayout_18.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.widget_39)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_124 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.label_188 = QLabel(self.widget_23)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_124.addWidget(self.label_188)

        self.wall_hum_lbl = QLabel(self.widget_23)
        self.wall_hum_lbl.setObjectName(u"wall_hum_lbl")
        self.wall_hum_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_124.addWidget(self.wall_hum_lbl)

        self.label_180 = QLabel(self.widget_23)
        self.label_180.setObjectName(u"label_180")

        self.horizontalLayout_124.addWidget(self.label_180)


        self.verticalLayout_18.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.widget_39)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_125 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.label_190 = QLabel(self.widget_24)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_125.addWidget(self.label_190)

        self.wall_co2_lbl = QLabel(self.widget_24)
        self.wall_co2_lbl.setObjectName(u"wall_co2_lbl")
        self.wall_co2_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_125.addWidget(self.wall_co2_lbl)

        self.label_182 = QLabel(self.widget_24)
        self.label_182.setObjectName(u"label_182")

        self.horizontalLayout_125.addWidget(self.label_182)


        self.verticalLayout_18.addWidget(self.widget_24)


        self.horizontalLayout_141.addWidget(self.widget_39)

        self.widget_38 = QWidget(self.widget_166)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setMaximumSize(QSize(360, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.widget_38)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(1, 1, 1, 1)
        self.label_6 = QLabel(self.widget_38)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_6)

        self.widget_16 = QWidget(self.widget_38)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_16)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.water_oxyd_lbl = QLabel(self.widget_16)
        self.water_oxyd_lbl.setObjectName(u"water_oxyd_lbl")
        self.water_oxyd_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.water_oxyd_lbl)

        self.label_184 = QLabel(self.widget_16)
        self.label_184.setObjectName(u"label_184")

        self.horizontalLayout_6.addWidget(self.label_184)


        self.verticalLayout_16.addWidget(self.widget_16)

        self.widget_18 = QWidget(self.widget_38)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_119 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.label_177 = QLabel(self.widget_18)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_119.addWidget(self.label_177)

        self.water_ph_lbl = QLabel(self.widget_18)
        self.water_ph_lbl.setObjectName(u"water_ph_lbl")
        self.water_ph_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_119.addWidget(self.water_ph_lbl)

        self.label_187 = QLabel(self.widget_18)
        self.label_187.setObjectName(u"label_187")

        self.horizontalLayout_119.addWidget(self.label_187)


        self.verticalLayout_16.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.widget_38)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_120 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.label_179 = QLabel(self.widget_19)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_120.addWidget(self.label_179)

        self.water_redox_lbl = QLabel(self.widget_19)
        self.water_redox_lbl.setObjectName(u"water_redox_lbl")
        self.water_redox_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_120.addWidget(self.water_redox_lbl)

        self.label_189 = QLabel(self.widget_19)
        self.label_189.setObjectName(u"label_189")

        self.horizontalLayout_120.addWidget(self.label_189)


        self.verticalLayout_16.addWidget(self.widget_19)

        self.widget_21 = QWidget(self.widget_38)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_121 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.label_181 = QLabel(self.widget_21)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_121.addWidget(self.label_181)

        self.water_cond_lbl = QLabel(self.widget_21)
        self.water_cond_lbl.setObjectName(u"water_cond_lbl")
        self.water_cond_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_121.addWidget(self.water_cond_lbl)

        self.label_191 = QLabel(self.widget_21)
        self.label_191.setObjectName(u"label_191")

        self.horizontalLayout_121.addWidget(self.label_191)


        self.verticalLayout_16.addWidget(self.widget_21)

        self.widget_20 = QWidget(self.widget_38)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_122 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.label_183 = QLabel(self.widget_20)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_122.addWidget(self.label_183)

        self.water_temp_lbl = QLabel(self.widget_20)
        self.water_temp_lbl.setObjectName(u"water_temp_lbl")
        self.water_temp_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_122.addWidget(self.water_temp_lbl)

        self.label_193 = QLabel(self.widget_20)
        self.label_193.setObjectName(u"label_193")

        self.horizontalLayout_122.addWidget(self.label_193)


        self.verticalLayout_16.addWidget(self.widget_20)


        self.horizontalLayout_141.addWidget(self.widget_38)

        self.widget_40 = QWidget(self.widget_166)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMaximumSize(QSize(360, 16777215))
        self.verticalLayout_19 = QVBoxLayout(self.widget_40)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(1, 1, 1, 1)
        self.label_194 = QLabel(self.widget_40)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setMaximumSize(QSize(16777215, 20))
        self.label_194.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_194)

        self.widget_26 = QWidget(self.widget_40)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_127 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.label_195 = QLabel(self.widget_26)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_127.addWidget(self.label_195)

        self.outside_temp_lbl = QLabel(self.widget_26)
        self.outside_temp_lbl.setObjectName(u"outside_temp_lbl")
        self.outside_temp_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_127.addWidget(self.outside_temp_lbl)

        self.label_196 = QLabel(self.widget_26)
        self.label_196.setObjectName(u"label_196")

        self.horizontalLayout_127.addWidget(self.label_196)


        self.verticalLayout_19.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.widget_40)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_128 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.label_197 = QLabel(self.widget_27)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_128.addWidget(self.label_197)

        self.outside_hum_lbl = QLabel(self.widget_27)
        self.outside_hum_lbl.setObjectName(u"outside_hum_lbl")
        self.outside_hum_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_128.addWidget(self.outside_hum_lbl)

        self.label_198 = QLabel(self.widget_27)
        self.label_198.setObjectName(u"label_198")

        self.horizontalLayout_128.addWidget(self.label_198)


        self.verticalLayout_19.addWidget(self.widget_27)

        self.widget_25 = QWidget(self.widget_40)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_126 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.label_192 = QLabel(self.widget_25)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_126.addWidget(self.label_192)

        self.outside_co2_lbl = QLabel(self.widget_25)
        self.outside_co2_lbl.setObjectName(u"outside_co2_lbl")
        self.outside_co2_lbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_126.addWidget(self.outside_co2_lbl)

        self.label_213 = QLabel(self.widget_25)
        self.label_213.setObjectName(u"label_213")

        self.horizontalLayout_126.addWidget(self.label_213)


        self.verticalLayout_19.addWidget(self.widget_25)


        self.horizontalLayout_141.addWidget(self.widget_40)


        self.horizontalLayout_5.addWidget(self.widget_166)


        self.verticalLayout_8.addWidget(self.widget_35)

        self.widget_165 = QWidget(self.solution_pg)
        self.widget_165.setObjectName(u"widget_165")
        self.widget_165.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_8.addWidget(self.widget_165)

        self.widget_12 = QWidget(self.solution_pg)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_136 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(-1, 1, 9, 1)
        self.widget_167 = QWidget(self.widget_12)
        self.widget_167.setObjectName(u"widget_167")
        self.widget_167.setMaximumSize(QSize(1100, 16777215))
        self.horizontalLayout_142 = QHBoxLayout(self.widget_167)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(-1, 0, -1, 0)
        self.widget_31 = QWidget(self.widget_167)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMaximumSize(QSize(360, 16777215))
        self.verticalLayout_24 = QVBoxLayout(self.widget_31)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(5, 9, 5, 9)
        self.label_208 = QLabel(self.widget_31)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setMaximumSize(QSize(16777215, 25))
        self.label_208.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_208)

        self.widget_48 = QWidget(self.widget_31)
        self.widget_48.setObjectName(u"widget_48")
        self.horizontalLayout_131 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, -1, 0, -1)
        self.label_202 = QLabel(self.widget_48)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setMaximumSize(QSize(150, 16777215))
        self.label_202.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_131.addWidget(self.label_202)

        self.ph_reg_le = QLineEdit(self.widget_48)
        self.ph_reg_le.setObjectName(u"ph_reg_le")
        self.ph_reg_le.setMinimumSize(QSize(0, 35))
        self.ph_reg_le.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_131.addWidget(self.ph_reg_le)


        self.verticalLayout_24.addWidget(self.widget_48)

        self.widget_202 = QWidget(self.widget_31)
        self.widget_202.setObjectName(u"widget_202")
        self.horizontalLayout_132 = QHBoxLayout(self.widget_202)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.widget_207 = QWidget(self.widget_202)
        self.widget_207.setObjectName(u"widget_207")
        self.widget_207.setMaximumSize(QSize(120, 16777215))
        self.horizontalLayout_178 = QHBoxLayout(self.widget_207)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.horizontalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.set_ph_value_btn = QPushButton(self.widget_207)
        self.set_ph_value_btn.setObjectName(u"set_ph_value_btn")
        self.set_ph_value_btn.setMaximumSize(QSize(80, 35))

        self.horizontalLayout_178.addWidget(self.set_ph_value_btn)


        self.horizontalLayout_132.addWidget(self.widget_207)

        self.ph_on_btn = QPushButton(self.widget_202)
        self.ph_on_btn.setObjectName(u"ph_on_btn")
        self.ph_on_btn.setMinimumSize(QSize(0, 35))
        self.ph_on_btn.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_132.addWidget(self.ph_on_btn)

        self.ph_off_btn = QPushButton(self.widget_202)
        self.ph_off_btn.setObjectName(u"ph_off_btn")
        self.ph_off_btn.setMinimumSize(QSize(0, 35))
        self.ph_off_btn.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_132.addWidget(self.ph_off_btn)


        self.verticalLayout_24.addWidget(self.widget_202)


        self.horizontalLayout_142.addWidget(self.widget_31)

        self.widget_75 = QWidget(self.widget_167)
        self.widget_75.setObjectName(u"widget_75")
        self.widget_75.setMaximumSize(QSize(360, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.widget_75)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, -1, 5, -1)
        self.label_211 = QLabel(self.widget_75)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setMaximumSize(QSize(16777215, 25))
        self.label_211.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_211)

        self.widget_76 = QWidget(self.widget_75)
        self.widget_76.setObjectName(u"widget_76")
        self.horizontalLayout_139 = QHBoxLayout(self.widget_76)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, -1, 0, -1)
        self.label_210 = QLabel(self.widget_76)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setMaximumSize(QSize(150, 16777215))
        self.label_210.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_139.addWidget(self.label_210)

        self.oxygenation_reg_le = QLineEdit(self.widget_76)
        self.oxygenation_reg_le.setObjectName(u"oxygenation_reg_le")
        self.oxygenation_reg_le.setMinimumSize(QSize(0, 35))
        self.oxygenation_reg_le.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_139.addWidget(self.oxygenation_reg_le)

        self.widget_169 = QWidget(self.widget_76)
        self.widget_169.setObjectName(u"widget_169")
        self.widget_169.setMaximumSize(QSize(150, 35))
        self.horizontalLayout_144 = QHBoxLayout(self.widget_169)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.pump_chb = AnimatedToggle(self.widget_169)
        self.pump_chb.setObjectName(u"pump_chb")
        self.pump_chb.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_144.addWidget(self.pump_chb)

        self.label_212 = QLabel(self.widget_169)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_144.addWidget(self.label_212)


        self.horizontalLayout_139.addWidget(self.widget_169)


        self.verticalLayout_20.addWidget(self.widget_76)

        self.widget_209 = QWidget(self.widget_75)
        self.widget_209.setObjectName(u"widget_209")
        self.horizontalLayout_179 = QHBoxLayout(self.widget_209)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.widget_211 = QWidget(self.widget_209)
        self.widget_211.setObjectName(u"widget_211")
        self.widget_211.setMaximumSize(QSize(120, 16777215))
        self.horizontalLayout_180 = QHBoxLayout(self.widget_211)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(1, 1, 1, 1)
        self.set_oxy_value_btn = QPushButton(self.widget_211)
        self.set_oxy_value_btn.setObjectName(u"set_oxy_value_btn")
        self.set_oxy_value_btn.setMaximumSize(QSize(80, 35))

        self.horizontalLayout_180.addWidget(self.set_oxy_value_btn)


        self.horizontalLayout_179.addWidget(self.widget_211)

        self.oxidation_on_btn = QPushButton(self.widget_209)
        self.oxidation_on_btn.setObjectName(u"oxidation_on_btn")
        self.oxidation_on_btn.setMinimumSize(QSize(0, 35))
        self.oxidation_on_btn.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_179.addWidget(self.oxidation_on_btn)

        self.oxidation_off_btn = QPushButton(self.widget_209)
        self.oxidation_off_btn.setObjectName(u"oxidation_off_btn")
        self.oxidation_off_btn.setMinimumSize(QSize(0, 35))
        self.oxidation_off_btn.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_179.addWidget(self.oxidation_off_btn)


        self.verticalLayout_20.addWidget(self.widget_209)


        self.horizontalLayout_142.addWidget(self.widget_75)

        self.widget_32 = QWidget(self.widget_167)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMaximumSize(QSize(360, 16777215))
        self.verticalLayout_23 = QVBoxLayout(self.widget_32)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 9, 5, 9)
        self.label_207 = QLabel(self.widget_32)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setMaximumSize(QSize(16777215, 25))
        self.label_207.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_207)

        self.widget_33 = QWidget(self.widget_32)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_129 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, -1, 0, -1)
        self.label_199 = QLabel(self.widget_33)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setMaximumSize(QSize(150, 16777215))
        self.label_199.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_129.addWidget(self.label_199)

        self.cond_reg_le = QLineEdit(self.widget_33)
        self.cond_reg_le.setObjectName(u"cond_reg_le")
        self.cond_reg_le.setMinimumSize(QSize(0, 35))
        self.cond_reg_le.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_129.addWidget(self.cond_reg_le)

        self.label_241 = QLabel(self.widget_33)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_129.addWidget(self.label_241)

        self.cond_ratio_le = QLineEdit(self.widget_33)
        self.cond_ratio_le.setObjectName(u"cond_ratio_le")
        self.cond_ratio_le.setMaximumSize(QSize(30, 35))

        self.horizontalLayout_129.addWidget(self.cond_ratio_le)

        self.label_242 = QLabel(self.widget_33)
        self.label_242.setObjectName(u"label_242")

        self.horizontalLayout_129.addWidget(self.label_242)


        self.verticalLayout_23.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.widget_32)
        self.widget_34.setObjectName(u"widget_34")
        self.horizontalLayout_130 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, -1, 0, -1)
        self.widget_201 = QWidget(self.widget_34)
        self.widget_201.setObjectName(u"widget_201")
        self.widget_201.setMaximumSize(QSize(120, 16777215))
        self.horizontalLayout_177 = QHBoxLayout(self.widget_201)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_177.setContentsMargins(0, 0, 0, 0)
        self.set_cond_value_btn = QPushButton(self.widget_201)
        self.set_cond_value_btn.setObjectName(u"set_cond_value_btn")
        self.set_cond_value_btn.setMaximumSize(QSize(80, 35))

        self.horizontalLayout_177.addWidget(self.set_cond_value_btn)


        self.horizontalLayout_130.addWidget(self.widget_201)

        self.cond_reg_on_btn = QPushButton(self.widget_34)
        self.cond_reg_on_btn.setObjectName(u"cond_reg_on_btn")
        self.cond_reg_on_btn.setMinimumSize(QSize(0, 35))
        self.cond_reg_on_btn.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_130.addWidget(self.cond_reg_on_btn)

        self.cond_reg_off_btn = QPushButton(self.widget_34)
        self.cond_reg_off_btn.setObjectName(u"cond_reg_off_btn")
        self.cond_reg_off_btn.setEnabled(True)
        self.cond_reg_off_btn.setMinimumSize(QSize(0, 35))
        self.cond_reg_off_btn.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_130.addWidget(self.cond_reg_off_btn)


        self.verticalLayout_23.addWidget(self.widget_34)


        self.horizontalLayout_142.addWidget(self.widget_32)


        self.horizontalLayout_136.addWidget(self.widget_167)


        self.verticalLayout_8.addWidget(self.widget_12)

        self.widget_36 = QWidget(self.solution_pg)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_137 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(-1, 1, -1, 1)
        self.widget_30 = QWidget(self.widget_36)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMaximumSize(QSize(360, 16777215))
        self.verticalLayout_25 = QVBoxLayout(self.widget_30)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(9, 9, 9, 9)
        self.label_209 = QLabel(self.widget_30)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setMaximumSize(QSize(16777215, 25))
        self.label_209.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_209)

        self.widget_195 = QWidget(self.widget_30)
        self.widget_195.setObjectName(u"widget_195")
        self.horizontalLayout_172 = QHBoxLayout(self.widget_195)
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.horizontalLayout_172.setContentsMargins(0, 0, 0, 0)
        self.widget_196 = QWidget(self.widget_195)
        self.widget_196.setObjectName(u"widget_196")
        self.widget_196.setMaximumSize(QSize(211, 16777215))
        self.horizontalLayout_173 = QHBoxLayout(self.widget_196)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalLayout_173.setContentsMargins(0, 0, 0, 0)
        self.automatic_lights_chb = AnimatedToggle(self.widget_196)
        self.automatic_lights_chb.setObjectName(u"automatic_lights_chb")
        self.automatic_lights_chb.setMaximumSize(QSize(60, 16777215))
        self.automatic_lights_chb.setChecked(True)

        self.horizontalLayout_173.addWidget(self.automatic_lights_chb)

        self.label_200 = QLabel(self.widget_196)
        self.label_200.setObjectName(u"label_200")

        self.horizontalLayout_173.addWidget(self.label_200)


        self.horizontalLayout_172.addWidget(self.widget_196)


        self.verticalLayout_25.addWidget(self.widget_195)

        self.widget_51 = QWidget(self.widget_30)
        self.widget_51.setObjectName(u"widget_51")
        self.horizontalLayout_133 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 1, 0, 1)
        self.label_205 = QLabel(self.widget_51)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setMaximumSize(QSize(150, 16777215))
        self.label_205.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_133.addWidget(self.label_205)

        self.lights_on_le = QLineEdit(self.widget_51)
        self.lights_on_le.setObjectName(u"lights_on_le")
        self.lights_on_le.setMinimumSize(QSize(0, 35))
        self.lights_on_le.setMaximumSize(QSize(70, 16777215))
        self.lights_on_le.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_133.addWidget(self.lights_on_le)


        self.verticalLayout_25.addWidget(self.widget_51)

        self.widget_52 = QWidget(self.widget_30)
        self.widget_52.setObjectName(u"widget_52")
        self.horizontalLayout_134 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 1, 0, 1)
        self.label_206 = QLabel(self.widget_52)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setMaximumSize(QSize(150, 16777215))
        self.label_206.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_134.addWidget(self.label_206)

        self.lights_off_le = QLineEdit(self.widget_52)
        self.lights_off_le.setObjectName(u"lights_off_le")
        self.lights_off_le.setMinimumSize(QSize(0, 35))
        self.lights_off_le.setMaximumSize(QSize(70, 16777215))
        self.lights_off_le.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_134.addWidget(self.lights_off_le)


        self.verticalLayout_25.addWidget(self.widget_52)

        self.widget_74 = QWidget(self.widget_30)
        self.widget_74.setObjectName(u"widget_74")
        self.widget_74.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_135 = QHBoxLayout(self.widget_74)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.save_lights_btn = QPushButton(self.widget_74)
        self.save_lights_btn.setObjectName(u"save_lights_btn")
        self.save_lights_btn.setMinimumSize(QSize(0, 35))
        self.save_lights_btn.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_135.addWidget(self.save_lights_btn)

        self.lights_on_btn = QPushButton(self.widget_74)
        self.lights_on_btn.setObjectName(u"lights_on_btn")
        self.lights_on_btn.setMaximumSize(QSize(110, 35))

        self.horizontalLayout_135.addWidget(self.lights_on_btn)

        self.lights_off_btn = QPushButton(self.widget_74)
        self.lights_off_btn.setObjectName(u"lights_off_btn")
        self.lights_off_btn.setMaximumSize(QSize(110, 35))

        self.horizontalLayout_135.addWidget(self.lights_off_btn)


        self.verticalLayout_25.addWidget(self.widget_74)


        self.horizontalLayout_137.addWidget(self.widget_30)


        self.verticalLayout_8.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.solution_pg)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMaximumSize(QSize(16777215, 50))

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
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.widget_43 = QWidget(self.widget_41)
        self.widget_43.setObjectName(u"widget_43")
        self.chart_1 = QHBoxLayout(self.widget_43)
        self.chart_1.setSpacing(0)
        self.chart_1.setObjectName(u"chart_1")
        self.chart_1.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.widget_43)

        self.widget_44 = QWidget(self.widget_41)
        self.widget_44.setObjectName(u"widget_44")
        self.chart_2 = QHBoxLayout(self.widget_44)
        self.chart_2.setObjectName(u"chart_2")
        self.chart_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.widget_44)


        self.horizontalLayout_117.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.widget_15)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_10 = QVBoxLayout(self.widget_42)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.widget_45 = QWidget(self.widget_42)
        self.widget_45.setObjectName(u"widget_45")
        self.chart_3 = QHBoxLayout(self.widget_45)
        self.chart_3.setObjectName(u"chart_3")
        self.chart_3.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.widget_45)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.chart_3.addWidget(self.frame)


        self.verticalLayout_10.addWidget(self.widget_45)

        self.widget_46 = QWidget(self.widget_42)
        self.widget_46.setObjectName(u"widget_46")
        self.chart_4 = QHBoxLayout(self.widget_46)
        self.chart_4.setObjectName(u"chart_4")
        self.chart_4.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(self.widget_46)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.chart_4.addWidget(self.frame_2)


        self.verticalLayout_10.addWidget(self.widget_46)

        self.widget_47 = QWidget(self.widget_42)
        self.widget_47.setObjectName(u"widget_47")
        self.chart_5 = QHBoxLayout(self.widget_47)
        self.chart_5.setObjectName(u"chart_5")
        self.chart_5.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.widget_47)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.chart_5.addWidget(self.frame_3)


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
        self.horizontalLayout_7.setContentsMargins(0, 3, 0, 3)
        self.widget_200 = QWidget(self.widget_14)
        self.widget_200.setObjectName(u"widget_200")
        self.widget_200.setMaximumSize(QSize(235, 16777215))
        self.horizontalLayout_176 = QHBoxLayout(self.widget_200)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.auto_watering_chb = AnimatedToggle(self.widget_200)
        self.auto_watering_chb.setObjectName(u"auto_watering_chb")
        self.auto_watering_chb.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_176.addWidget(self.auto_watering_chb)

        self.label_240 = QLabel(self.widget_200)
        self.label_240.setObjectName(u"label_240")

        self.horizontalLayout_176.addWidget(self.label_240)


        self.horizontalLayout_7.addWidget(self.widget_200)

        self.save_watering_setting_btn = QPushButton(self.widget_14)
        self.save_watering_setting_btn.setObjectName(u"save_watering_setting_btn")
        self.save_watering_setting_btn.setMinimumSize(QSize(0, 40))
        self.save_watering_setting_btn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.save_watering_setting_btn)

        self.current_settings_btn = QPushButton(self.widget_14)
        self.current_settings_btn.setObjectName(u"current_settings_btn")
        self.current_settings_btn.setEnabled(True)
        self.current_settings_btn.setMinimumSize(QSize(0, 40))
        self.current_settings_btn.setMaximumSize(QSize(173, 16777215))

        self.horizontalLayout_7.addWidget(self.current_settings_btn)

        self.water_all_btn = QPushButton(self.widget_14)
        self.water_all_btn.setObjectName(u"water_all_btn")
        self.water_all_btn.setEnabled(True)
        self.water_all_btn.setMinimumSize(QSize(0, 40))
        self.water_all_btn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.water_all_btn)


        self.horizontalLayout_8.addWidget(self.widget_14)


        self.verticalLayout_11.addWidget(self.widget_49)

        self.scrollArea = QScrollArea(self.watering_pg)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setBaseSize(QSize(0, 0))
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"background-color: rgb(180, 180, 180); \n"
"width: 15px;\n"
"margin: 15px 3px 15px 3px; \n"
"border: none; \n"
"border-radius: 4px; }\n"
" \n"
"QScrollBar::handle:vertical { \n"
"background-color: #4CAF50; \n"
"min-height: 20px; \n"
"border-radius: 4px; }\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical { \n"
"height: 0px; \n"
"subcontrol-position: top; \n"
"subcontrol-origin: margin; } \n"
"\n"
"QScrollBar::up-arrow:vertical, \n"
"QScrollBar::down-arrow:vertical { \n"
"background: none; \n"
"border: none; }\n"
" \n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical { \n"
"background: none; }")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 769, 1732))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_77 = QWidget(self.scrollAreaWidgetContents)
        self.widget_77.setObjectName(u"widget_77")
        self.widget_77.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_77)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 1, 9, 1)
        self.label_2 = QLabel(self.widget_77)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_10.addWidget(self.label_2)

        self.stop_watering_col_1 = QPushButton(self.widget_77)
        self.stop_watering_col_1.setObjectName(u"stop_watering_col_1")
        self.stop_watering_col_1.setMaximumSize(QSize(120, 40))

        self.horizontalLayout_10.addWidget(self.stop_watering_col_1)

        self.water_col_btn_1 = QPushButton(self.widget_77)
        self.water_col_btn_1.setObjectName(u"water_col_btn_1")
        self.water_col_btn_1.setMinimumSize(QSize(0, 40))
        self.water_col_btn_1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.water_col_btn_1)

        self.fill_column_btn_1 = QPushButton(self.widget_77)
        self.fill_column_btn_1.setObjectName(u"fill_column_btn_1")
        self.fill_column_btn_1.setMinimumSize(QSize(0, 40))
        self.fill_column_btn_1.setMaximumSize(QSize(120, 16777215))

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
        self.widget_5 = QWidget(self.widget_53)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_145 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_145.setSpacing(6)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_7 = QLabel(self.widget_5)
        self.valve_state_lbl_7.setObjectName(u"valve_state_lbl_7")
        self.valve_state_lbl_7.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_145.addWidget(self.valve_state_lbl_7)

        self.water_btn_7 = QPushButton(self.widget_5)
        self.water_btn_7.setObjectName(u"water_btn_7")
        self.water_btn_7.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_145.addWidget(self.water_btn_7)


        self.horizontalLayout_9.addWidget(self.widget_5)

        self.widget_95 = QWidget(self.widget_53)
        self.widget_95.setObjectName(u"widget_95")
        self.widget_95.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_30 = QHBoxLayout(self.widget_95)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(2, 2, 2, 2)
        self.label_39 = QLabel(self.widget_95)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_30.addWidget(self.label_39)

        self.water_start_le_7 = QLineEdit(self.widget_95)
        self.water_start_le_7.setObjectName(u"water_start_le_7")
        self.water_start_le_7.setMinimumSize(QSize(0, 35))
        self.water_start_le_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_30.addWidget(self.water_start_le_7)

        self.label_40 = QLabel(self.widget_95)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_30.addWidget(self.label_40)


        self.horizontalLayout_9.addWidget(self.widget_95)

        self.widget_99 = QWidget(self.widget_53)
        self.widget_99.setObjectName(u"widget_99")
        self.widget_99.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_34 = QHBoxLayout(self.widget_99)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(2, 2, 2, 2)
        self.label_46 = QLabel(self.widget_99)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_34.addWidget(self.label_46)

        self.water_dur_le_7 = QLineEdit(self.widget_99)
        self.water_dur_le_7.setObjectName(u"water_dur_le_7")
        self.water_dur_le_7.setMinimumSize(QSize(0, 35))
        self.water_dur_le_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_34.addWidget(self.water_dur_le_7)

        self.label_47 = QLabel(self.widget_99)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_34.addWidget(self.label_47)


        self.horizontalLayout_9.addWidget(self.widget_99)

        self.widget_103 = QWidget(self.widget_53)
        self.widget_103.setObjectName(u"widget_103")
        self.widget_103.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_38 = QHBoxLayout(self.widget_103)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(2, 2, 2, 2)
        self.label_54 = QLabel(self.widget_103)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_38.addWidget(self.label_54)

        self.water_interval_le_7 = QLineEdit(self.widget_103)
        self.water_interval_le_7.setObjectName(u"water_interval_le_7")
        self.water_interval_le_7.setMinimumSize(QSize(0, 35))
        self.water_interval_le_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_38.addWidget(self.water_interval_le_7)

        self.label_55 = QLabel(self.widget_103)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_38.addWidget(self.label_55)


        self.horizontalLayout_9.addWidget(self.widget_103)

        self.widget_107 = QWidget(self.widget_53)
        self.widget_107.setObjectName(u"widget_107")
        self.widget_107.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_42 = QHBoxLayout(self.widget_107)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(2, 2, 2, 2)
        self.label_62 = QLabel(self.widget_107)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_42.addWidget(self.label_62)

        self.water_end_le_7 = QLineEdit(self.widget_107)
        self.water_end_le_7.setObjectName(u"water_end_le_7")
        self.water_end_le_7.setMinimumSize(QSize(0, 35))
        self.water_end_le_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_42.addWidget(self.water_end_le_7)

        self.label_63 = QLabel(self.widget_107)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_42.addWidget(self.label_63)


        self.horizontalLayout_9.addWidget(self.widget_107)


        self.verticalLayout_13.addWidget(self.widget_53)

        self.widget_54 = QWidget(self.col_wg_1)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.widget_174 = QWidget(self.widget_54)
        self.widget_174.setObjectName(u"widget_174")
        self.widget_174.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_151 = QHBoxLayout(self.widget_174)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_6 = QLabel(self.widget_174)
        self.valve_state_lbl_6.setObjectName(u"valve_state_lbl_6")
        self.valve_state_lbl_6.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_151.addWidget(self.valve_state_lbl_6)

        self.water_btn_6 = QPushButton(self.widget_174)
        self.water_btn_6.setObjectName(u"water_btn_6")
        self.water_btn_6.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_151.addWidget(self.water_btn_6)


        self.horizontalLayout_21.addWidget(self.widget_174)

        self.widget_94 = QWidget(self.widget_54)
        self.widget_94.setObjectName(u"widget_94")
        self.widget_94.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_29 = QHBoxLayout(self.widget_94)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(2, 2, 2, 2)
        self.label_37 = QLabel(self.widget_94)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_29.addWidget(self.label_37)

        self.water_start_le_6 = QLineEdit(self.widget_94)
        self.water_start_le_6.setObjectName(u"water_start_le_6")
        self.water_start_le_6.setMinimumSize(QSize(0, 35))
        self.water_start_le_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_29.addWidget(self.water_start_le_6)

        self.label_38 = QLabel(self.widget_94)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_29.addWidget(self.label_38)


        self.horizontalLayout_21.addWidget(self.widget_94)

        self.widget_98 = QWidget(self.widget_54)
        self.widget_98.setObjectName(u"widget_98")
        self.widget_98.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_33 = QHBoxLayout(self.widget_98)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(2, 2, 2, 2)
        self.label_44 = QLabel(self.widget_98)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_33.addWidget(self.label_44)

        self.water_dur_le_6 = QLineEdit(self.widget_98)
        self.water_dur_le_6.setObjectName(u"water_dur_le_6")
        self.water_dur_le_6.setMinimumSize(QSize(0, 35))
        self.water_dur_le_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_33.addWidget(self.water_dur_le_6)

        self.label_45 = QLabel(self.widget_98)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_33.addWidget(self.label_45)


        self.horizontalLayout_21.addWidget(self.widget_98)

        self.widget_102 = QWidget(self.widget_54)
        self.widget_102.setObjectName(u"widget_102")
        self.widget_102.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_102)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(2, 2, 2, 2)
        self.label_52 = QLabel(self.widget_102)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_37.addWidget(self.label_52)

        self.water_interval_le_6 = QLineEdit(self.widget_102)
        self.water_interval_le_6.setObjectName(u"water_interval_le_6")
        self.water_interval_le_6.setMinimumSize(QSize(0, 35))
        self.water_interval_le_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_37.addWidget(self.water_interval_le_6)

        self.label_53 = QLabel(self.widget_102)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_37.addWidget(self.label_53)


        self.horizontalLayout_21.addWidget(self.widget_102)

        self.widget_106 = QWidget(self.widget_54)
        self.widget_106.setObjectName(u"widget_106")
        self.widget_106.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_41 = QHBoxLayout(self.widget_106)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(2, 2, 2, 2)
        self.label_60 = QLabel(self.widget_106)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_41.addWidget(self.label_60)

        self.water_end_le_6 = QLineEdit(self.widget_106)
        self.water_end_le_6.setObjectName(u"water_end_le_6")
        self.water_end_le_6.setMinimumSize(QSize(0, 35))
        self.water_end_le_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_41.addWidget(self.water_end_le_6)

        self.label_61 = QLabel(self.widget_106)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_41.addWidget(self.label_61)


        self.horizontalLayout_21.addWidget(self.widget_106)


        self.verticalLayout_13.addWidget(self.widget_54)

        self.widget_55 = QWidget(self.col_wg_1)
        self.widget_55.setObjectName(u"widget_55")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(1, 1, 1, 1)
        self.widget_173 = QWidget(self.widget_55)
        self.widget_173.setObjectName(u"widget_173")
        self.widget_173.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_150 = QHBoxLayout(self.widget_173)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_5 = QLabel(self.widget_173)
        self.valve_state_lbl_5.setObjectName(u"valve_state_lbl_5")
        self.valve_state_lbl_5.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_150.addWidget(self.valve_state_lbl_5)

        self.water_btn_5 = QPushButton(self.widget_173)
        self.water_btn_5.setObjectName(u"water_btn_5")
        self.water_btn_5.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_150.addWidget(self.water_btn_5)


        self.horizontalLayout_26.addWidget(self.widget_173)

        self.widget_93 = QWidget(self.widget_55)
        self.widget_93.setObjectName(u"widget_93")
        self.widget_93.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_93)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(2, 2, 2, 2)
        self.label_35 = QLabel(self.widget_93)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_28.addWidget(self.label_35)

        self.water_start_le_5 = QLineEdit(self.widget_93)
        self.water_start_le_5.setObjectName(u"water_start_le_5")
        self.water_start_le_5.setMinimumSize(QSize(0, 35))
        self.water_start_le_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_28.addWidget(self.water_start_le_5)

        self.label_36 = QLabel(self.widget_93)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_28.addWidget(self.label_36)


        self.horizontalLayout_26.addWidget(self.widget_93)

        self.widget_97 = QWidget(self.widget_55)
        self.widget_97.setObjectName(u"widget_97")
        self.widget_97.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_32 = QHBoxLayout(self.widget_97)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(2, 2, 2, 2)
        self.label_42 = QLabel(self.widget_97)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_32.addWidget(self.label_42)

        self.water_dur_le_5 = QLineEdit(self.widget_97)
        self.water_dur_le_5.setObjectName(u"water_dur_le_5")
        self.water_dur_le_5.setMinimumSize(QSize(0, 35))
        self.water_dur_le_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_32.addWidget(self.water_dur_le_5)

        self.label_43 = QLabel(self.widget_97)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_32.addWidget(self.label_43)


        self.horizontalLayout_26.addWidget(self.widget_97)

        self.widget_101 = QWidget(self.widget_55)
        self.widget_101.setObjectName(u"widget_101")
        self.widget_101.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_101)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(2, 2, 2, 2)
        self.label_50 = QLabel(self.widget_101)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_36.addWidget(self.label_50)

        self.water_interval_le_5 = QLineEdit(self.widget_101)
        self.water_interval_le_5.setObjectName(u"water_interval_le_5")
        self.water_interval_le_5.setMinimumSize(QSize(0, 35))
        self.water_interval_le_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_36.addWidget(self.water_interval_le_5)

        self.label_51 = QLabel(self.widget_101)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_36.addWidget(self.label_51)


        self.horizontalLayout_26.addWidget(self.widget_101)

        self.widget_105 = QWidget(self.widget_55)
        self.widget_105.setObjectName(u"widget_105")
        self.widget_105.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_40 = QHBoxLayout(self.widget_105)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(2, 2, 2, 2)
        self.label_58 = QLabel(self.widget_105)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_40.addWidget(self.label_58)

        self.water_end_le_5 = QLineEdit(self.widget_105)
        self.water_end_le_5.setObjectName(u"water_end_le_5")
        self.water_end_le_5.setMinimumSize(QSize(0, 35))
        self.water_end_le_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_40.addWidget(self.water_end_le_5)

        self.label_59 = QLabel(self.widget_105)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_40.addWidget(self.label_59)


        self.horizontalLayout_26.addWidget(self.widget_105)


        self.verticalLayout_13.addWidget(self.widget_55)

        self.widget_56 = QWidget(self.col_wg_1)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(1, 1, 1, 1)
        self.widget_172 = QWidget(self.widget_56)
        self.widget_172.setObjectName(u"widget_172")
        self.widget_172.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_149 = QHBoxLayout(self.widget_172)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_4 = QLabel(self.widget_172)
        self.valve_state_lbl_4.setObjectName(u"valve_state_lbl_4")
        self.valve_state_lbl_4.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_149.addWidget(self.valve_state_lbl_4)

        self.water_btn_4 = QPushButton(self.widget_172)
        self.water_btn_4.setObjectName(u"water_btn_4")
        self.water_btn_4.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_149.addWidget(self.water_btn_4)


        self.horizontalLayout_43.addWidget(self.widget_172)

        self.widget_92 = QWidget(self.widget_56)
        self.widget_92.setObjectName(u"widget_92")
        self.widget_92.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_92)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(2, 2, 2, 2)
        self.label_33 = QLabel(self.widget_92)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_27.addWidget(self.label_33)

        self.water_start_le_4 = QLineEdit(self.widget_92)
        self.water_start_le_4.setObjectName(u"water_start_le_4")
        self.water_start_le_4.setMinimumSize(QSize(0, 35))
        self.water_start_le_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_27.addWidget(self.water_start_le_4)

        self.label_34 = QLabel(self.widget_92)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_27.addWidget(self.label_34)


        self.horizontalLayout_43.addWidget(self.widget_92)

        self.widget_96 = QWidget(self.widget_56)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_31 = QHBoxLayout(self.widget_96)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(2, 2, 2, 2)
        self.label_41 = QLabel(self.widget_96)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_31.addWidget(self.label_41)

        self.water_dur_le_4 = QLineEdit(self.widget_96)
        self.water_dur_le_4.setObjectName(u"water_dur_le_4")
        self.water_dur_le_4.setMinimumSize(QSize(0, 35))
        self.water_dur_le_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_31.addWidget(self.water_dur_le_4)

        self.label_8 = QLabel(self.widget_96)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_31.addWidget(self.label_8)


        self.horizontalLayout_43.addWidget(self.widget_96)

        self.widget_100 = QWidget(self.widget_56)
        self.widget_100.setObjectName(u"widget_100")
        self.widget_100.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_100)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(2, 2, 2, 2)
        self.label_48 = QLabel(self.widget_100)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_35.addWidget(self.label_48)

        self.water_interval_le_4 = QLineEdit(self.widget_100)
        self.water_interval_le_4.setObjectName(u"water_interval_le_4")
        self.water_interval_le_4.setMinimumSize(QSize(0, 35))
        self.water_interval_le_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_35.addWidget(self.water_interval_le_4)

        self.label_49 = QLabel(self.widget_100)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_35.addWidget(self.label_49)


        self.horizontalLayout_43.addWidget(self.widget_100)

        self.widget_104 = QWidget(self.widget_56)
        self.widget_104.setObjectName(u"widget_104")
        self.widget_104.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_39 = QHBoxLayout(self.widget_104)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(2, 2, 2, 2)
        self.label_56 = QLabel(self.widget_104)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_39.addWidget(self.label_56)

        self.water_end_le_4 = QLineEdit(self.widget_104)
        self.water_end_le_4.setObjectName(u"water_end_le_4")
        self.water_end_le_4.setMinimumSize(QSize(0, 35))
        self.water_end_le_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_39.addWidget(self.water_end_le_4)

        self.label_57 = QLabel(self.widget_104)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_39.addWidget(self.label_57)


        self.horizontalLayout_43.addWidget(self.widget_104)


        self.verticalLayout_13.addWidget(self.widget_56)

        self.widget_57 = QWidget(self.col_wg_1)
        self.widget_57.setObjectName(u"widget_57")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(1, 1, 1, 1)
        self.widget_171 = QWidget(self.widget_57)
        self.widget_171.setObjectName(u"widget_171")
        self.widget_171.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_148 = QHBoxLayout(self.widget_171)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_3 = QLabel(self.widget_171)
        self.valve_state_lbl_3.setObjectName(u"valve_state_lbl_3")
        self.valve_state_lbl_3.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_148.addWidget(self.valve_state_lbl_3)

        self.water_btn_3 = QPushButton(self.widget_171)
        self.water_btn_3.setObjectName(u"water_btn_3")
        self.water_btn_3.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_148.addWidget(self.water_btn_3)


        self.horizontalLayout_44.addWidget(self.widget_171)

        self.widget_88 = QWidget(self.widget_57)
        self.widget_88.setObjectName(u"widget_88")
        self.widget_88.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_88)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(2, 2, 2, 2)
        self.label_25 = QLabel(self.widget_88)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_22.addWidget(self.label_25)

        self.water_start_le_3 = QLineEdit(self.widget_88)
        self.water_start_le_3.setObjectName(u"water_start_le_3")
        self.water_start_le_3.setMinimumSize(QSize(0, 35))
        self.water_start_le_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_22.addWidget(self.water_start_le_3)

        self.label_26 = QLabel(self.widget_88)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_22.addWidget(self.label_26)


        self.horizontalLayout_44.addWidget(self.widget_88)

        self.widget_89 = QWidget(self.widget_57)
        self.widget_89.setObjectName(u"widget_89")
        self.widget_89.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_89)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(2, 2, 2, 2)
        self.label_27 = QLabel(self.widget_89)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_23.addWidget(self.label_27)

        self.water_dur_le_3 = QLineEdit(self.widget_89)
        self.water_dur_le_3.setObjectName(u"water_dur_le_3")
        self.water_dur_le_3.setMinimumSize(QSize(0, 35))
        self.water_dur_le_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_23.addWidget(self.water_dur_le_3)

        self.label_28 = QLabel(self.widget_89)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_23.addWidget(self.label_28)


        self.horizontalLayout_44.addWidget(self.widget_89)

        self.widget_90 = QWidget(self.widget_57)
        self.widget_90.setObjectName(u"widget_90")
        self.widget_90.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_90)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(2, 2, 2, 2)
        self.label_29 = QLabel(self.widget_90)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_24.addWidget(self.label_29)

        self.water_interval_le_3 = QLineEdit(self.widget_90)
        self.water_interval_le_3.setObjectName(u"water_interval_le_3")
        self.water_interval_le_3.setMinimumSize(QSize(0, 35))
        self.water_interval_le_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_24.addWidget(self.water_interval_le_3)

        self.label_30 = QLabel(self.widget_90)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_24.addWidget(self.label_30)


        self.horizontalLayout_44.addWidget(self.widget_90)

        self.widget_91 = QWidget(self.widget_57)
        self.widget_91.setObjectName(u"widget_91")
        self.widget_91.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_91)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(2, 2, 2, 2)
        self.label_31 = QLabel(self.widget_91)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_25.addWidget(self.label_31)

        self.water_end_le_3 = QLineEdit(self.widget_91)
        self.water_end_le_3.setObjectName(u"water_end_le_3")
        self.water_end_le_3.setMinimumSize(QSize(0, 35))
        self.water_end_le_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_25.addWidget(self.water_end_le_3)

        self.label_32 = QLabel(self.widget_91)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_25.addWidget(self.label_32)


        self.horizontalLayout_44.addWidget(self.widget_91)


        self.verticalLayout_13.addWidget(self.widget_57)

        self.widget_58 = QWidget(self.col_wg_1)
        self.widget_58.setObjectName(u"widget_58")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(1, 1, 1, 1)
        self.widget_170 = QWidget(self.widget_58)
        self.widget_170.setObjectName(u"widget_170")
        self.widget_170.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_147 = QHBoxLayout(self.widget_170)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_2 = QLabel(self.widget_170)
        self.valve_state_lbl_2.setObjectName(u"valve_state_lbl_2")
        self.valve_state_lbl_2.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_147.addWidget(self.valve_state_lbl_2)

        self.water_btn_2 = QPushButton(self.widget_170)
        self.water_btn_2.setObjectName(u"water_btn_2")
        self.water_btn_2.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_147.addWidget(self.water_btn_2)


        self.horizontalLayout_45.addWidget(self.widget_170)

        self.widget_85 = QWidget(self.widget_58)
        self.widget_85.setObjectName(u"widget_85")
        self.widget_85.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_85)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(2, 2, 2, 2)
        self.label_19 = QLabel(self.widget_85)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_18.addWidget(self.label_19)

        self.water_start_le_2 = QLineEdit(self.widget_85)
        self.water_start_le_2.setObjectName(u"water_start_le_2")
        self.water_start_le_2.setMinimumSize(QSize(0, 35))
        self.water_start_le_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_18.addWidget(self.water_start_le_2)

        self.label_20 = QLabel(self.widget_85)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_18.addWidget(self.label_20)


        self.horizontalLayout_45.addWidget(self.widget_85)

        self.widget_87 = QWidget(self.widget_58)
        self.widget_87.setObjectName(u"widget_87")
        self.widget_87.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_87)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(2, 2, 2, 2)
        self.label_23 = QLabel(self.widget_87)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_20.addWidget(self.label_23)

        self.water_dur_le_2 = QLineEdit(self.widget_87)
        self.water_dur_le_2.setObjectName(u"water_dur_le_2")
        self.water_dur_le_2.setMinimumSize(QSize(0, 35))
        self.water_dur_le_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_20.addWidget(self.water_dur_le_2)

        self.label_24 = QLabel(self.widget_87)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_20.addWidget(self.label_24)


        self.horizontalLayout_45.addWidget(self.widget_87)

        self.widget_84 = QWidget(self.widget_58)
        self.widget_84.setObjectName(u"widget_84")
        self.widget_84.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_84)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.label_17 = QLabel(self.widget_84)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_17.addWidget(self.label_17)

        self.water_interval_le_2 = QLineEdit(self.widget_84)
        self.water_interval_le_2.setObjectName(u"water_interval_le_2")
        self.water_interval_le_2.setMinimumSize(QSize(0, 35))
        self.water_interval_le_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_17.addWidget(self.water_interval_le_2)

        self.label_18 = QLabel(self.widget_84)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_17.addWidget(self.label_18)


        self.horizontalLayout_45.addWidget(self.widget_84)

        self.widget_86 = QWidget(self.widget_58)
        self.widget_86.setObjectName(u"widget_86")
        self.widget_86.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_86)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.label_21 = QLabel(self.widget_86)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_19.addWidget(self.label_21)

        self.water_end_le_2 = QLineEdit(self.widget_86)
        self.water_end_le_2.setObjectName(u"water_end_le_2")
        self.water_end_le_2.setMinimumSize(QSize(0, 35))
        self.water_end_le_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_19.addWidget(self.water_end_le_2)

        self.label_22 = QLabel(self.widget_86)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_19.addWidget(self.label_22)


        self.horizontalLayout_45.addWidget(self.widget_86)


        self.verticalLayout_13.addWidget(self.widget_58)

        self.widget_59 = QWidget(self.col_wg_1)
        self.widget_59.setObjectName(u"widget_59")
        self.horizontalLayout_46 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(1, 1, 1, 1)
        self.widget_168 = QWidget(self.widget_59)
        self.widget_168.setObjectName(u"widget_168")
        self.widget_168.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_146 = QHBoxLayout(self.widget_168)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_1 = QLabel(self.widget_168)
        self.valve_state_lbl_1.setObjectName(u"valve_state_lbl_1")
        self.valve_state_lbl_1.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_146.addWidget(self.valve_state_lbl_1)

        self.water_btn_1 = QPushButton(self.widget_168)
        self.water_btn_1.setObjectName(u"water_btn_1")
        self.water_btn_1.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_146.addWidget(self.water_btn_1)


        self.horizontalLayout_46.addWidget(self.widget_168)

        self.widget_80 = QWidget(self.widget_59)
        self.widget_80.setObjectName(u"widget_80")
        self.widget_80.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_80)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.label_9 = QLabel(self.widget_80)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_13.addWidget(self.label_9)

        self.water_start_le_1 = QLineEdit(self.widget_80)
        self.water_start_le_1.setObjectName(u"water_start_le_1")
        self.water_start_le_1.setMinimumSize(QSize(0, 35))
        self.water_start_le_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_13.addWidget(self.water_start_le_1)

        self.label_15 = QLabel(self.widget_80)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)


        self.horizontalLayout_46.addWidget(self.widget_80)

        self.widget_81 = QWidget(self.widget_59)
        self.widget_81.setObjectName(u"widget_81")
        self.widget_81.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_81)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.label_10 = QLabel(self.widget_81)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_14.addWidget(self.label_10)

        self.water_dur_le_1 = QLineEdit(self.widget_81)
        self.water_dur_le_1.setObjectName(u"water_dur_le_1")
        self.water_dur_le_1.setMinimumSize(QSize(0, 35))
        self.water_dur_le_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_14.addWidget(self.water_dur_le_1)

        self.label_4 = QLabel(self.widget_81)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_14.addWidget(self.label_4)


        self.horizontalLayout_46.addWidget(self.widget_81)

        self.widget_82 = QWidget(self.widget_59)
        self.widget_82.setObjectName(u"widget_82")
        self.widget_82.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_82)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.label_11 = QLabel(self.widget_82)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_15.addWidget(self.label_11)

        self.water_interval_le_1 = QLineEdit(self.widget_82)
        self.water_interval_le_1.setObjectName(u"water_interval_le_1")
        self.water_interval_le_1.setMinimumSize(QSize(0, 35))
        self.water_interval_le_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_15.addWidget(self.water_interval_le_1)

        self.label_14 = QLabel(self.widget_82)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_15.addWidget(self.label_14)


        self.horizontalLayout_46.addWidget(self.widget_82)

        self.widget_83 = QWidget(self.widget_59)
        self.widget_83.setObjectName(u"widget_83")
        self.widget_83.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_83)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.label_12 = QLabel(self.widget_83)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_16.addWidget(self.label_12)

        self.water_end_le_1 = QLineEdit(self.widget_83)
        self.water_end_le_1.setObjectName(u"water_end_le_1")
        self.water_end_le_1.setMinimumSize(QSize(0, 35))
        self.water_end_le_1.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_16.addWidget(self.water_end_le_1)

        self.label_16 = QLabel(self.widget_83)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)


        self.horizontalLayout_46.addWidget(self.widget_83)


        self.verticalLayout_13.addWidget(self.widget_59)


        self.verticalLayout_12.addWidget(self.col_wg_1)

        self.widget_28 = QWidget(self.scrollAreaWidgetContents)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(0, 50))

        self.verticalLayout_12.addWidget(self.widget_28)

        self.widget_78 = QWidget(self.scrollAreaWidgetContents)
        self.widget_78.setObjectName(u"widget_78")
        self.widget_78.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_78)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 1, 9, 1)
        self.label_13 = QLabel(self.widget_78)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.stop_watering_col_2 = QPushButton(self.widget_78)
        self.stop_watering_col_2.setObjectName(u"stop_watering_col_2")
        self.stop_watering_col_2.setMaximumSize(QSize(120, 40))

        self.horizontalLayout_11.addWidget(self.stop_watering_col_2)

        self.water_col_btn_2 = QPushButton(self.widget_78)
        self.water_col_btn_2.setObjectName(u"water_col_btn_2")
        self.water_col_btn_2.setMinimumSize(QSize(0, 40))
        self.water_col_btn_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_11.addWidget(self.water_col_btn_2)

        self.fill_column_btn_2 = QPushButton(self.widget_78)
        self.fill_column_btn_2.setObjectName(u"fill_column_btn_2")
        self.fill_column_btn_2.setMinimumSize(QSize(0, 40))
        self.fill_column_btn_2.setMaximumSize(QSize(120, 16777215))

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
        self.horizontalLayout_75 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(1, 1, 1, 1)
        self.widget_181 = QWidget(self.widget_62)
        self.widget_181.setObjectName(u"widget_181")
        self.widget_181.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_158 = QHBoxLayout(self.widget_181)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.horizontalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_14 = QLabel(self.widget_181)
        self.valve_state_lbl_14.setObjectName(u"valve_state_lbl_14")
        self.valve_state_lbl_14.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_158.addWidget(self.valve_state_lbl_14)

        self.water_btn_14 = QPushButton(self.widget_181)
        self.water_btn_14.setObjectName(u"water_btn_14")
        self.water_btn_14.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_158.addWidget(self.water_btn_14)


        self.horizontalLayout_75.addWidget(self.widget_181)

        self.widget_114 = QWidget(self.widget_62)
        self.widget_114.setObjectName(u"widget_114")
        self.widget_114.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_53 = QHBoxLayout(self.widget_114)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(2, 2, 2, 2)
        self.label_76 = QLabel(self.widget_114)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_53.addWidget(self.label_76)

        self.water_start_le_14 = QLineEdit(self.widget_114)
        self.water_start_le_14.setObjectName(u"water_start_le_14")
        self.water_start_le_14.setMinimumSize(QSize(0, 35))
        self.water_start_le_14.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_53.addWidget(self.water_start_le_14)

        self.label_77 = QLabel(self.widget_114)
        self.label_77.setObjectName(u"label_77")

        self.horizontalLayout_53.addWidget(self.label_77)


        self.horizontalLayout_75.addWidget(self.widget_114)

        self.widget_121 = QWidget(self.widget_62)
        self.widget_121.setObjectName(u"widget_121")
        self.widget_121.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_60 = QHBoxLayout(self.widget_121)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(2, 2, 2, 2)
        self.label_90 = QLabel(self.widget_121)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_60.addWidget(self.label_90)

        self.water_dur_le_14 = QLineEdit(self.widget_121)
        self.water_dur_le_14.setObjectName(u"water_dur_le_14")
        self.water_dur_le_14.setMinimumSize(QSize(0, 35))
        self.water_dur_le_14.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_60.addWidget(self.water_dur_le_14)

        self.label_91 = QLabel(self.widget_121)
        self.label_91.setObjectName(u"label_91")

        self.horizontalLayout_60.addWidget(self.label_91)


        self.horizontalLayout_75.addWidget(self.widget_121)

        self.widget_128 = QWidget(self.widget_62)
        self.widget_128.setObjectName(u"widget_128")
        self.widget_128.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_67 = QHBoxLayout(self.widget_128)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(2, 2, 2, 2)
        self.label_104 = QLabel(self.widget_128)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_67.addWidget(self.label_104)

        self.water_interval_le_14 = QLineEdit(self.widget_128)
        self.water_interval_le_14.setObjectName(u"water_interval_le_14")
        self.water_interval_le_14.setMinimumSize(QSize(0, 35))
        self.water_interval_le_14.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_67.addWidget(self.water_interval_le_14)

        self.label_105 = QLabel(self.widget_128)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_67.addWidget(self.label_105)


        self.horizontalLayout_75.addWidget(self.widget_128)

        self.widget_135 = QWidget(self.widget_62)
        self.widget_135.setObjectName(u"widget_135")
        self.widget_135.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_74 = QHBoxLayout(self.widget_135)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(2, 2, 2, 2)
        self.label_118 = QLabel(self.widget_135)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_74.addWidget(self.label_118)

        self.water_end_le_14 = QLineEdit(self.widget_135)
        self.water_end_le_14.setObjectName(u"water_end_le_14")
        self.water_end_le_14.setMinimumSize(QSize(0, 35))
        self.water_end_le_14.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_74.addWidget(self.water_end_le_14)

        self.label_119 = QLabel(self.widget_135)
        self.label_119.setObjectName(u"label_119")

        self.horizontalLayout_74.addWidget(self.label_119)


        self.horizontalLayout_75.addWidget(self.widget_135)


        self.verticalLayout_14.addWidget(self.widget_62)

        self.widget_66 = QWidget(self.col_wg_2)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_76 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(1, 1, 1, 1)
        self.widget_180 = QWidget(self.widget_66)
        self.widget_180.setObjectName(u"widget_180")
        self.widget_180.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_157 = QHBoxLayout(self.widget_180)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_13 = QLabel(self.widget_180)
        self.valve_state_lbl_13.setObjectName(u"valve_state_lbl_13")
        self.valve_state_lbl_13.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_157.addWidget(self.valve_state_lbl_13)

        self.water_btn_13 = QPushButton(self.widget_180)
        self.water_btn_13.setObjectName(u"water_btn_13")
        self.water_btn_13.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_157.addWidget(self.water_btn_13)


        self.horizontalLayout_76.addWidget(self.widget_180)

        self.widget_113 = QWidget(self.widget_66)
        self.widget_113.setObjectName(u"widget_113")
        self.widget_113.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_52 = QHBoxLayout(self.widget_113)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(2, 2, 2, 2)
        self.label_74 = QLabel(self.widget_113)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_52.addWidget(self.label_74)

        self.water_start_le_13 = QLineEdit(self.widget_113)
        self.water_start_le_13.setObjectName(u"water_start_le_13")
        self.water_start_le_13.setMinimumSize(QSize(0, 35))
        self.water_start_le_13.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_52.addWidget(self.water_start_le_13)

        self.label_75 = QLabel(self.widget_113)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_52.addWidget(self.label_75)


        self.horizontalLayout_76.addWidget(self.widget_113)

        self.widget_120 = QWidget(self.widget_66)
        self.widget_120.setObjectName(u"widget_120")
        self.widget_120.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_59 = QHBoxLayout(self.widget_120)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(2, 2, 2, 2)
        self.label_88 = QLabel(self.widget_120)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_59.addWidget(self.label_88)

        self.water_dur_le_13 = QLineEdit(self.widget_120)
        self.water_dur_le_13.setObjectName(u"water_dur_le_13")
        self.water_dur_le_13.setMinimumSize(QSize(0, 35))
        self.water_dur_le_13.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_59.addWidget(self.water_dur_le_13)

        self.label_89 = QLabel(self.widget_120)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_59.addWidget(self.label_89)


        self.horizontalLayout_76.addWidget(self.widget_120)

        self.widget_127 = QWidget(self.widget_66)
        self.widget_127.setObjectName(u"widget_127")
        self.widget_127.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_66 = QHBoxLayout(self.widget_127)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(2, 2, 2, 2)
        self.label_102 = QLabel(self.widget_127)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_66.addWidget(self.label_102)

        self.water_interval_le_13 = QLineEdit(self.widget_127)
        self.water_interval_le_13.setObjectName(u"water_interval_le_13")
        self.water_interval_le_13.setMinimumSize(QSize(0, 35))
        self.water_interval_le_13.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_66.addWidget(self.water_interval_le_13)

        self.label_103 = QLabel(self.widget_127)
        self.label_103.setObjectName(u"label_103")

        self.horizontalLayout_66.addWidget(self.label_103)


        self.horizontalLayout_76.addWidget(self.widget_127)

        self.widget_134 = QWidget(self.widget_66)
        self.widget_134.setObjectName(u"widget_134")
        self.widget_134.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_73 = QHBoxLayout(self.widget_134)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(2, 2, 2, 2)
        self.label_116 = QLabel(self.widget_134)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_73.addWidget(self.label_116)

        self.water_end_le_13 = QLineEdit(self.widget_134)
        self.water_end_le_13.setObjectName(u"water_end_le_13")
        self.water_end_le_13.setMinimumSize(QSize(0, 35))
        self.water_end_le_13.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_73.addWidget(self.water_end_le_13)

        self.label_117 = QLabel(self.widget_134)
        self.label_117.setObjectName(u"label_117")

        self.horizontalLayout_73.addWidget(self.label_117)


        self.horizontalLayout_76.addWidget(self.widget_134)


        self.verticalLayout_14.addWidget(self.widget_66)

        self.widget_60 = QWidget(self.col_wg_2)
        self.widget_60.setObjectName(u"widget_60")
        self.horizontalLayout_77 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(1, 1, 1, 1)
        self.widget_179 = QWidget(self.widget_60)
        self.widget_179.setObjectName(u"widget_179")
        self.widget_179.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_156 = QHBoxLayout(self.widget_179)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_12 = QLabel(self.widget_179)
        self.valve_state_lbl_12.setObjectName(u"valve_state_lbl_12")
        self.valve_state_lbl_12.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_156.addWidget(self.valve_state_lbl_12)

        self.water_btn_12 = QPushButton(self.widget_179)
        self.water_btn_12.setObjectName(u"water_btn_12")
        self.water_btn_12.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_156.addWidget(self.water_btn_12)


        self.horizontalLayout_77.addWidget(self.widget_179)

        self.widget_112 = QWidget(self.widget_60)
        self.widget_112.setObjectName(u"widget_112")
        self.widget_112.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_51 = QHBoxLayout(self.widget_112)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(2, 2, 2, 2)
        self.label_72 = QLabel(self.widget_112)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_51.addWidget(self.label_72)

        self.water_start_le_12 = QLineEdit(self.widget_112)
        self.water_start_le_12.setObjectName(u"water_start_le_12")
        self.water_start_le_12.setMinimumSize(QSize(0, 35))
        self.water_start_le_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_51.addWidget(self.water_start_le_12)

        self.label_73 = QLabel(self.widget_112)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_51.addWidget(self.label_73)


        self.horizontalLayout_77.addWidget(self.widget_112)

        self.widget_119 = QWidget(self.widget_60)
        self.widget_119.setObjectName(u"widget_119")
        self.widget_119.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_58 = QHBoxLayout(self.widget_119)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(2, 2, 2, 2)
        self.label_86 = QLabel(self.widget_119)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_58.addWidget(self.label_86)

        self.water_dur_le_12 = QLineEdit(self.widget_119)
        self.water_dur_le_12.setObjectName(u"water_dur_le_12")
        self.water_dur_le_12.setMinimumSize(QSize(0, 35))
        self.water_dur_le_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_58.addWidget(self.water_dur_le_12)

        self.label_87 = QLabel(self.widget_119)
        self.label_87.setObjectName(u"label_87")

        self.horizontalLayout_58.addWidget(self.label_87)


        self.horizontalLayout_77.addWidget(self.widget_119)

        self.widget_126 = QWidget(self.widget_60)
        self.widget_126.setObjectName(u"widget_126")
        self.widget_126.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_65 = QHBoxLayout(self.widget_126)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(2, 2, 2, 2)
        self.label_100 = QLabel(self.widget_126)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_65.addWidget(self.label_100)

        self.water_interval_le_12 = QLineEdit(self.widget_126)
        self.water_interval_le_12.setObjectName(u"water_interval_le_12")
        self.water_interval_le_12.setMinimumSize(QSize(0, 35))
        self.water_interval_le_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_65.addWidget(self.water_interval_le_12)

        self.label_101 = QLabel(self.widget_126)
        self.label_101.setObjectName(u"label_101")

        self.horizontalLayout_65.addWidget(self.label_101)


        self.horizontalLayout_77.addWidget(self.widget_126)

        self.widget_133 = QWidget(self.widget_60)
        self.widget_133.setObjectName(u"widget_133")
        self.widget_133.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_72 = QHBoxLayout(self.widget_133)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(2, 2, 2, 2)
        self.label_114 = QLabel(self.widget_133)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_72.addWidget(self.label_114)

        self.water_end_le_12 = QLineEdit(self.widget_133)
        self.water_end_le_12.setObjectName(u"water_end_le_12")
        self.water_end_le_12.setMinimumSize(QSize(0, 35))
        self.water_end_le_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_72.addWidget(self.water_end_le_12)

        self.label_115 = QLabel(self.widget_133)
        self.label_115.setObjectName(u"label_115")

        self.horizontalLayout_72.addWidget(self.label_115)


        self.horizontalLayout_77.addWidget(self.widget_133)


        self.verticalLayout_14.addWidget(self.widget_60)

        self.widget_63 = QWidget(self.col_wg_2)
        self.widget_63.setObjectName(u"widget_63")
        self.horizontalLayout_78 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(1, 1, 1, 1)
        self.widget_178 = QWidget(self.widget_63)
        self.widget_178.setObjectName(u"widget_178")
        self.widget_178.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_155 = QHBoxLayout(self.widget_178)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_11 = QLabel(self.widget_178)
        self.valve_state_lbl_11.setObjectName(u"valve_state_lbl_11")
        self.valve_state_lbl_11.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_155.addWidget(self.valve_state_lbl_11)

        self.water_btn_11 = QPushButton(self.widget_178)
        self.water_btn_11.setObjectName(u"water_btn_11")
        self.water_btn_11.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_155.addWidget(self.water_btn_11)


        self.horizontalLayout_78.addWidget(self.widget_178)

        self.widget_111 = QWidget(self.widget_63)
        self.widget_111.setObjectName(u"widget_111")
        self.widget_111.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_50 = QHBoxLayout(self.widget_111)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(2, 2, 2, 2)
        self.label_70 = QLabel(self.widget_111)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_50.addWidget(self.label_70)

        self.water_start_le_11 = QLineEdit(self.widget_111)
        self.water_start_le_11.setObjectName(u"water_start_le_11")
        self.water_start_le_11.setMinimumSize(QSize(0, 35))
        self.water_start_le_11.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_50.addWidget(self.water_start_le_11)

        self.label_71 = QLabel(self.widget_111)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_50.addWidget(self.label_71)


        self.horizontalLayout_78.addWidget(self.widget_111)

        self.widget_118 = QWidget(self.widget_63)
        self.widget_118.setObjectName(u"widget_118")
        self.widget_118.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_57 = QHBoxLayout(self.widget_118)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(2, 2, 2, 2)
        self.label_84 = QLabel(self.widget_118)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_57.addWidget(self.label_84)

        self.water_dur_le_11 = QLineEdit(self.widget_118)
        self.water_dur_le_11.setObjectName(u"water_dur_le_11")
        self.water_dur_le_11.setMinimumSize(QSize(0, 35))
        self.water_dur_le_11.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_57.addWidget(self.water_dur_le_11)

        self.label_85 = QLabel(self.widget_118)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_57.addWidget(self.label_85)


        self.horizontalLayout_78.addWidget(self.widget_118)

        self.widget_125 = QWidget(self.widget_63)
        self.widget_125.setObjectName(u"widget_125")
        self.widget_125.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_64 = QHBoxLayout(self.widget_125)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(2, 2, 2, 2)
        self.label_98 = QLabel(self.widget_125)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_64.addWidget(self.label_98)

        self.water_interval_le_11 = QLineEdit(self.widget_125)
        self.water_interval_le_11.setObjectName(u"water_interval_le_11")
        self.water_interval_le_11.setMinimumSize(QSize(0, 35))
        self.water_interval_le_11.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_64.addWidget(self.water_interval_le_11)

        self.label_99 = QLabel(self.widget_125)
        self.label_99.setObjectName(u"label_99")

        self.horizontalLayout_64.addWidget(self.label_99)


        self.horizontalLayout_78.addWidget(self.widget_125)

        self.widget_132 = QWidget(self.widget_63)
        self.widget_132.setObjectName(u"widget_132")
        self.widget_132.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_71 = QHBoxLayout(self.widget_132)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(2, 2, 2, 2)
        self.label_112 = QLabel(self.widget_132)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_71.addWidget(self.label_112)

        self.water_end_le_11 = QLineEdit(self.widget_132)
        self.water_end_le_11.setObjectName(u"water_end_le_11")
        self.water_end_le_11.setMinimumSize(QSize(0, 35))
        self.water_end_le_11.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_71.addWidget(self.water_end_le_11)

        self.label_113 = QLabel(self.widget_132)
        self.label_113.setObjectName(u"label_113")

        self.horizontalLayout_71.addWidget(self.label_113)


        self.horizontalLayout_78.addWidget(self.widget_132)


        self.verticalLayout_14.addWidget(self.widget_63)

        self.widget_61 = QWidget(self.col_wg_2)
        self.widget_61.setObjectName(u"widget_61")
        self.horizontalLayout_79 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(1, 1, 1, 1)
        self.widget_177 = QWidget(self.widget_61)
        self.widget_177.setObjectName(u"widget_177")
        self.widget_177.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_154 = QHBoxLayout(self.widget_177)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_10 = QLabel(self.widget_177)
        self.valve_state_lbl_10.setObjectName(u"valve_state_lbl_10")
        self.valve_state_lbl_10.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_154.addWidget(self.valve_state_lbl_10)

        self.water_btn_10 = QPushButton(self.widget_177)
        self.water_btn_10.setObjectName(u"water_btn_10")
        self.water_btn_10.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_154.addWidget(self.water_btn_10)


        self.horizontalLayout_79.addWidget(self.widget_177)

        self.widget_110 = QWidget(self.widget_61)
        self.widget_110.setObjectName(u"widget_110")
        self.widget_110.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_49 = QHBoxLayout(self.widget_110)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(2, 2, 2, 2)
        self.label_68 = QLabel(self.widget_110)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_49.addWidget(self.label_68)

        self.water_start_le_10 = QLineEdit(self.widget_110)
        self.water_start_le_10.setObjectName(u"water_start_le_10")
        self.water_start_le_10.setMinimumSize(QSize(0, 35))
        self.water_start_le_10.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_49.addWidget(self.water_start_le_10)

        self.label_69 = QLabel(self.widget_110)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_49.addWidget(self.label_69)


        self.horizontalLayout_79.addWidget(self.widget_110)

        self.widget_117 = QWidget(self.widget_61)
        self.widget_117.setObjectName(u"widget_117")
        self.widget_117.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_56 = QHBoxLayout(self.widget_117)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(2, 2, 2, 2)
        self.label_82 = QLabel(self.widget_117)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_56.addWidget(self.label_82)

        self.water_dur_le_10 = QLineEdit(self.widget_117)
        self.water_dur_le_10.setObjectName(u"water_dur_le_10")
        self.water_dur_le_10.setMinimumSize(QSize(0, 35))
        self.water_dur_le_10.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_56.addWidget(self.water_dur_le_10)

        self.label_83 = QLabel(self.widget_117)
        self.label_83.setObjectName(u"label_83")

        self.horizontalLayout_56.addWidget(self.label_83)


        self.horizontalLayout_79.addWidget(self.widget_117)

        self.widget_124 = QWidget(self.widget_61)
        self.widget_124.setObjectName(u"widget_124")
        self.widget_124.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_63 = QHBoxLayout(self.widget_124)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(2, 2, 2, 2)
        self.label_96 = QLabel(self.widget_124)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_63.addWidget(self.label_96)

        self.water_interval_le_10 = QLineEdit(self.widget_124)
        self.water_interval_le_10.setObjectName(u"water_interval_le_10")
        self.water_interval_le_10.setMinimumSize(QSize(0, 35))
        self.water_interval_le_10.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_63.addWidget(self.water_interval_le_10)

        self.label_97 = QLabel(self.widget_124)
        self.label_97.setObjectName(u"label_97")

        self.horizontalLayout_63.addWidget(self.label_97)


        self.horizontalLayout_79.addWidget(self.widget_124)

        self.widget_131 = QWidget(self.widget_61)
        self.widget_131.setObjectName(u"widget_131")
        self.widget_131.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_70 = QHBoxLayout(self.widget_131)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(2, 2, 2, 2)
        self.label_110 = QLabel(self.widget_131)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_70.addWidget(self.label_110)

        self.water_end_le_10 = QLineEdit(self.widget_131)
        self.water_end_le_10.setObjectName(u"water_end_le_10")
        self.water_end_le_10.setMinimumSize(QSize(0, 35))
        self.water_end_le_10.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_70.addWidget(self.water_end_le_10)

        self.label_111 = QLabel(self.widget_131)
        self.label_111.setObjectName(u"label_111")

        self.horizontalLayout_70.addWidget(self.label_111)


        self.horizontalLayout_79.addWidget(self.widget_131)


        self.verticalLayout_14.addWidget(self.widget_61)

        self.widget_65 = QWidget(self.col_wg_2)
        self.widget_65.setObjectName(u"widget_65")
        self.horizontalLayout_80 = QHBoxLayout(self.widget_65)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(1, 1, 1, 1)
        self.widget_176 = QWidget(self.widget_65)
        self.widget_176.setObjectName(u"widget_176")
        self.widget_176.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_153 = QHBoxLayout(self.widget_176)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_9 = QLabel(self.widget_176)
        self.valve_state_lbl_9.setObjectName(u"valve_state_lbl_9")
        self.valve_state_lbl_9.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_153.addWidget(self.valve_state_lbl_9)

        self.water_btn_9 = QPushButton(self.widget_176)
        self.water_btn_9.setObjectName(u"water_btn_9")
        self.water_btn_9.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_153.addWidget(self.water_btn_9)


        self.horizontalLayout_80.addWidget(self.widget_176)

        self.widget_109 = QWidget(self.widget_65)
        self.widget_109.setObjectName(u"widget_109")
        self.widget_109.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_48 = QHBoxLayout(self.widget_109)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(2, 2, 2, 2)
        self.label_66 = QLabel(self.widget_109)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_48.addWidget(self.label_66)

        self.water_start_le_9 = QLineEdit(self.widget_109)
        self.water_start_le_9.setObjectName(u"water_start_le_9")
        self.water_start_le_9.setMinimumSize(QSize(0, 35))
        self.water_start_le_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_48.addWidget(self.water_start_le_9)

        self.label_67 = QLabel(self.widget_109)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_48.addWidget(self.label_67)


        self.horizontalLayout_80.addWidget(self.widget_109)

        self.widget_116 = QWidget(self.widget_65)
        self.widget_116.setObjectName(u"widget_116")
        self.widget_116.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_55 = QHBoxLayout(self.widget_116)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(2, 2, 2, 2)
        self.label_80 = QLabel(self.widget_116)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_55.addWidget(self.label_80)

        self.water_dur_le_9 = QLineEdit(self.widget_116)
        self.water_dur_le_9.setObjectName(u"water_dur_le_9")
        self.water_dur_le_9.setMinimumSize(QSize(0, 35))
        self.water_dur_le_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_55.addWidget(self.water_dur_le_9)

        self.label_81 = QLabel(self.widget_116)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_55.addWidget(self.label_81)


        self.horizontalLayout_80.addWidget(self.widget_116)

        self.widget_123 = QWidget(self.widget_65)
        self.widget_123.setObjectName(u"widget_123")
        self.widget_123.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_62 = QHBoxLayout(self.widget_123)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(2, 2, 2, 2)
        self.label_94 = QLabel(self.widget_123)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_62.addWidget(self.label_94)

        self.water_interval_le_9 = QLineEdit(self.widget_123)
        self.water_interval_le_9.setObjectName(u"water_interval_le_9")
        self.water_interval_le_9.setMinimumSize(QSize(0, 35))
        self.water_interval_le_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_62.addWidget(self.water_interval_le_9)

        self.label_95 = QLabel(self.widget_123)
        self.label_95.setObjectName(u"label_95")

        self.horizontalLayout_62.addWidget(self.label_95)


        self.horizontalLayout_80.addWidget(self.widget_123)

        self.widget_130 = QWidget(self.widget_65)
        self.widget_130.setObjectName(u"widget_130")
        self.widget_130.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_69 = QHBoxLayout(self.widget_130)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(2, 2, 2, 2)
        self.label_108 = QLabel(self.widget_130)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_69.addWidget(self.label_108)

        self.water_end_le_9 = QLineEdit(self.widget_130)
        self.water_end_le_9.setObjectName(u"water_end_le_9")
        self.water_end_le_9.setMinimumSize(QSize(0, 35))
        self.water_end_le_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_69.addWidget(self.water_end_le_9)

        self.label_109 = QLabel(self.widget_130)
        self.label_109.setObjectName(u"label_109")

        self.horizontalLayout_69.addWidget(self.label_109)


        self.horizontalLayout_80.addWidget(self.widget_130)


        self.verticalLayout_14.addWidget(self.widget_65)

        self.widget_64 = QWidget(self.col_wg_2)
        self.widget_64.setObjectName(u"widget_64")
        self.horizontalLayout_81 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(1, 1, 1, 1)
        self.widget_175 = QWidget(self.widget_64)
        self.widget_175.setObjectName(u"widget_175")
        self.widget_175.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_152 = QHBoxLayout(self.widget_175)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalLayout_152.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_8 = QLabel(self.widget_175)
        self.valve_state_lbl_8.setObjectName(u"valve_state_lbl_8")
        self.valve_state_lbl_8.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_152.addWidget(self.valve_state_lbl_8)

        self.water_btn_8 = QPushButton(self.widget_175)
        self.water_btn_8.setObjectName(u"water_btn_8")
        self.water_btn_8.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_152.addWidget(self.water_btn_8)


        self.horizontalLayout_81.addWidget(self.widget_175)

        self.widget_108 = QWidget(self.widget_64)
        self.widget_108.setObjectName(u"widget_108")
        self.widget_108.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_47 = QHBoxLayout(self.widget_108)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(2, 2, 2, 2)
        self.label_64 = QLabel(self.widget_108)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_47.addWidget(self.label_64)

        self.water_start_le_8 = QLineEdit(self.widget_108)
        self.water_start_le_8.setObjectName(u"water_start_le_8")
        self.water_start_le_8.setMinimumSize(QSize(0, 35))
        self.water_start_le_8.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_47.addWidget(self.water_start_le_8)

        self.label_65 = QLabel(self.widget_108)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_47.addWidget(self.label_65)


        self.horizontalLayout_81.addWidget(self.widget_108)

        self.widget_115 = QWidget(self.widget_64)
        self.widget_115.setObjectName(u"widget_115")
        self.widget_115.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_54 = QHBoxLayout(self.widget_115)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(2, 2, 2, 2)
        self.label_78 = QLabel(self.widget_115)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_54.addWidget(self.label_78)

        self.water_dur_le_8 = QLineEdit(self.widget_115)
        self.water_dur_le_8.setObjectName(u"water_dur_le_8")
        self.water_dur_le_8.setMinimumSize(QSize(0, 35))
        self.water_dur_le_8.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_54.addWidget(self.water_dur_le_8)

        self.label_79 = QLabel(self.widget_115)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_54.addWidget(self.label_79)


        self.horizontalLayout_81.addWidget(self.widget_115)

        self.widget_122 = QWidget(self.widget_64)
        self.widget_122.setObjectName(u"widget_122")
        self.widget_122.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_61 = QHBoxLayout(self.widget_122)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(2, 2, 2, 2)
        self.label_92 = QLabel(self.widget_122)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_61.addWidget(self.label_92)

        self.water_interval_le_8 = QLineEdit(self.widget_122)
        self.water_interval_le_8.setObjectName(u"water_interval_le_8")
        self.water_interval_le_8.setMinimumSize(QSize(0, 35))
        self.water_interval_le_8.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_61.addWidget(self.water_interval_le_8)

        self.label_93 = QLabel(self.widget_122)
        self.label_93.setObjectName(u"label_93")

        self.horizontalLayout_61.addWidget(self.label_93)


        self.horizontalLayout_81.addWidget(self.widget_122)

        self.widget_129 = QWidget(self.widget_64)
        self.widget_129.setObjectName(u"widget_129")
        self.widget_129.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_68 = QHBoxLayout(self.widget_129)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(2, 2, 2, 2)
        self.label_106 = QLabel(self.widget_129)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_68.addWidget(self.label_106)

        self.water_end_le_8 = QLineEdit(self.widget_129)
        self.water_end_le_8.setObjectName(u"water_end_le_8")
        self.water_end_le_8.setMinimumSize(QSize(0, 35))
        self.water_end_le_8.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_68.addWidget(self.water_end_le_8)

        self.label_107 = QLabel(self.widget_129)
        self.label_107.setObjectName(u"label_107")

        self.horizontalLayout_68.addWidget(self.label_107)


        self.horizontalLayout_81.addWidget(self.widget_129)


        self.verticalLayout_14.addWidget(self.widget_64)


        self.verticalLayout_12.addWidget(self.col_wg_2)

        self.widget_29 = QWidget(self.scrollAreaWidgetContents)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMinimumSize(QSize(0, 50))

        self.verticalLayout_12.addWidget(self.widget_29)

        self.widget_79 = QWidget(self.scrollAreaWidgetContents)
        self.widget_79.setObjectName(u"widget_79")
        self.widget_79.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, 1, 9, 1)
        self.label_3 = QLabel(self.widget_79)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_12.addWidget(self.label_3)

        self.stop_watering_col_3 = QPushButton(self.widget_79)
        self.stop_watering_col_3.setObjectName(u"stop_watering_col_3")
        self.stop_watering_col_3.setMaximumSize(QSize(120, 40))

        self.horizontalLayout_12.addWidget(self.stop_watering_col_3)

        self.water_col_btn_3 = QPushButton(self.widget_79)
        self.water_col_btn_3.setObjectName(u"water_col_btn_3")
        self.water_col_btn_3.setMinimumSize(QSize(0, 40))
        self.water_col_btn_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.water_col_btn_3)

        self.fill_column_btn_3 = QPushButton(self.widget_79)
        self.fill_column_btn_3.setObjectName(u"fill_column_btn_3")
        self.fill_column_btn_3.setMinimumSize(QSize(0, 40))
        self.fill_column_btn_3.setMaximumSize(QSize(120, 16777215))

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
        self.horizontalLayout_110 = QHBoxLayout(self.widget_69)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(1, 1, 1, 1)
        self.widget_188 = QWidget(self.widget_69)
        self.widget_188.setObjectName(u"widget_188")
        self.widget_188.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_165 = QHBoxLayout(self.widget_188)
        self.horizontalLayout_165.setSpacing(6)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalLayout_165.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_21 = QLabel(self.widget_188)
        self.valve_state_lbl_21.setObjectName(u"valve_state_lbl_21")
        self.valve_state_lbl_21.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_165.addWidget(self.valve_state_lbl_21)

        self.water_btn_21 = QPushButton(self.widget_188)
        self.water_btn_21.setObjectName(u"water_btn_21")
        self.water_btn_21.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_165.addWidget(self.water_btn_21)


        self.horizontalLayout_110.addWidget(self.widget_188)

        self.widget_142 = QWidget(self.widget_69)
        self.widget_142.setObjectName(u"widget_142")
        self.widget_142.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_88 = QHBoxLayout(self.widget_142)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(2, 2, 2, 2)
        self.label_132 = QLabel(self.widget_142)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_88.addWidget(self.label_132)

        self.water_start_le_21 = QLineEdit(self.widget_142)
        self.water_start_le_21.setObjectName(u"water_start_le_21")
        self.water_start_le_21.setMinimumSize(QSize(0, 35))
        self.water_start_le_21.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_88.addWidget(self.water_start_le_21)

        self.label_133 = QLabel(self.widget_142)
        self.label_133.setObjectName(u"label_133")

        self.horizontalLayout_88.addWidget(self.label_133)


        self.horizontalLayout_110.addWidget(self.widget_142)

        self.widget_149 = QWidget(self.widget_69)
        self.widget_149.setObjectName(u"widget_149")
        self.widget_149.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_95 = QHBoxLayout(self.widget_149)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(2, 2, 2, 2)
        self.label_146 = QLabel(self.widget_149)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_95.addWidget(self.label_146)

        self.water_dur_le_21 = QLineEdit(self.widget_149)
        self.water_dur_le_21.setObjectName(u"water_dur_le_21")
        self.water_dur_le_21.setMinimumSize(QSize(0, 35))
        self.water_dur_le_21.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_95.addWidget(self.water_dur_le_21)

        self.label_147 = QLabel(self.widget_149)
        self.label_147.setObjectName(u"label_147")

        self.horizontalLayout_95.addWidget(self.label_147)


        self.horizontalLayout_110.addWidget(self.widget_149)

        self.widget_156 = QWidget(self.widget_69)
        self.widget_156.setObjectName(u"widget_156")
        self.widget_156.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_102 = QHBoxLayout(self.widget_156)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(2, 2, 2, 2)
        self.label_160 = QLabel(self.widget_156)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_102.addWidget(self.label_160)

        self.water_interval_le_21 = QLineEdit(self.widget_156)
        self.water_interval_le_21.setObjectName(u"water_interval_le_21")
        self.water_interval_le_21.setMinimumSize(QSize(0, 35))
        self.water_interval_le_21.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_102.addWidget(self.water_interval_le_21)

        self.label_161 = QLabel(self.widget_156)
        self.label_161.setObjectName(u"label_161")

        self.horizontalLayout_102.addWidget(self.label_161)


        self.horizontalLayout_110.addWidget(self.widget_156)

        self.widget_163 = QWidget(self.widget_69)
        self.widget_163.setObjectName(u"widget_163")
        self.widget_163.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_109 = QHBoxLayout(self.widget_163)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(2, 2, 2, 2)
        self.label_174 = QLabel(self.widget_163)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_109.addWidget(self.label_174)

        self.water_end_le_21 = QLineEdit(self.widget_163)
        self.water_end_le_21.setObjectName(u"water_end_le_21")
        self.water_end_le_21.setMinimumSize(QSize(0, 35))
        self.water_end_le_21.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_109.addWidget(self.water_end_le_21)

        self.label_175 = QLabel(self.widget_163)
        self.label_175.setObjectName(u"label_175")

        self.horizontalLayout_109.addWidget(self.label_175)


        self.horizontalLayout_110.addWidget(self.widget_163)


        self.verticalLayout_15.addWidget(self.widget_69)

        self.widget_73 = QWidget(self.col_wg_3)
        self.widget_73.setObjectName(u"widget_73")
        self.horizontalLayout_111 = QHBoxLayout(self.widget_73)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(1, 1, 1, 1)
        self.widget_187 = QWidget(self.widget_73)
        self.widget_187.setObjectName(u"widget_187")
        self.widget_187.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_164 = QHBoxLayout(self.widget_187)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.horizontalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_20 = QLabel(self.widget_187)
        self.valve_state_lbl_20.setObjectName(u"valve_state_lbl_20")
        self.valve_state_lbl_20.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_164.addWidget(self.valve_state_lbl_20)

        self.water_btn_20 = QPushButton(self.widget_187)
        self.water_btn_20.setObjectName(u"water_btn_20")
        self.water_btn_20.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_164.addWidget(self.water_btn_20)


        self.horizontalLayout_111.addWidget(self.widget_187)

        self.widget_141 = QWidget(self.widget_73)
        self.widget_141.setObjectName(u"widget_141")
        self.widget_141.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_87 = QHBoxLayout(self.widget_141)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(2, 2, 2, 2)
        self.label_130 = QLabel(self.widget_141)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_87.addWidget(self.label_130)

        self.water_start_le_20 = QLineEdit(self.widget_141)
        self.water_start_le_20.setObjectName(u"water_start_le_20")
        self.water_start_le_20.setMinimumSize(QSize(0, 35))
        self.water_start_le_20.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_87.addWidget(self.water_start_le_20)

        self.label_131 = QLabel(self.widget_141)
        self.label_131.setObjectName(u"label_131")

        self.horizontalLayout_87.addWidget(self.label_131)


        self.horizontalLayout_111.addWidget(self.widget_141)

        self.widget_148 = QWidget(self.widget_73)
        self.widget_148.setObjectName(u"widget_148")
        self.widget_148.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_94 = QHBoxLayout(self.widget_148)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(2, 2, 2, 2)
        self.label_144 = QLabel(self.widget_148)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_94.addWidget(self.label_144)

        self.water_dur_le_20 = QLineEdit(self.widget_148)
        self.water_dur_le_20.setObjectName(u"water_dur_le_20")
        self.water_dur_le_20.setMinimumSize(QSize(0, 35))
        self.water_dur_le_20.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_94.addWidget(self.water_dur_le_20)

        self.label_145 = QLabel(self.widget_148)
        self.label_145.setObjectName(u"label_145")

        self.horizontalLayout_94.addWidget(self.label_145)


        self.horizontalLayout_111.addWidget(self.widget_148)

        self.widget_155 = QWidget(self.widget_73)
        self.widget_155.setObjectName(u"widget_155")
        self.widget_155.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_101 = QHBoxLayout(self.widget_155)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(2, 2, 2, 2)
        self.label_158 = QLabel(self.widget_155)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_101.addWidget(self.label_158)

        self.water_interval_le_20 = QLineEdit(self.widget_155)
        self.water_interval_le_20.setObjectName(u"water_interval_le_20")
        self.water_interval_le_20.setMinimumSize(QSize(0, 35))
        self.water_interval_le_20.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_101.addWidget(self.water_interval_le_20)

        self.label_159 = QLabel(self.widget_155)
        self.label_159.setObjectName(u"label_159")

        self.horizontalLayout_101.addWidget(self.label_159)


        self.horizontalLayout_111.addWidget(self.widget_155)

        self.widget_162 = QWidget(self.widget_73)
        self.widget_162.setObjectName(u"widget_162")
        self.widget_162.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_108 = QHBoxLayout(self.widget_162)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(2, 2, 2, 2)
        self.label_172 = QLabel(self.widget_162)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_108.addWidget(self.label_172)

        self.water_end_le_20 = QLineEdit(self.widget_162)
        self.water_end_le_20.setObjectName(u"water_end_le_20")
        self.water_end_le_20.setMinimumSize(QSize(0, 35))
        self.water_end_le_20.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_108.addWidget(self.water_end_le_20)

        self.label_173 = QLabel(self.widget_162)
        self.label_173.setObjectName(u"label_173")

        self.horizontalLayout_108.addWidget(self.label_173)


        self.horizontalLayout_111.addWidget(self.widget_162)


        self.verticalLayout_15.addWidget(self.widget_73)

        self.widget_67 = QWidget(self.col_wg_3)
        self.widget_67.setObjectName(u"widget_67")
        self.horizontalLayout_112 = QHBoxLayout(self.widget_67)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(1, 1, 1, 1)
        self.widget_186 = QWidget(self.widget_67)
        self.widget_186.setObjectName(u"widget_186")
        self.widget_186.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_163 = QHBoxLayout(self.widget_186)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_19 = QLabel(self.widget_186)
        self.valve_state_lbl_19.setObjectName(u"valve_state_lbl_19")
        self.valve_state_lbl_19.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_163.addWidget(self.valve_state_lbl_19)

        self.water_btn_19 = QPushButton(self.widget_186)
        self.water_btn_19.setObjectName(u"water_btn_19")
        self.water_btn_19.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_163.addWidget(self.water_btn_19)


        self.horizontalLayout_112.addWidget(self.widget_186)

        self.widget_140 = QWidget(self.widget_67)
        self.widget_140.setObjectName(u"widget_140")
        self.widget_140.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_86 = QHBoxLayout(self.widget_140)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(2, 2, 2, 2)
        self.label_128 = QLabel(self.widget_140)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_86.addWidget(self.label_128)

        self.water_start_le_19 = QLineEdit(self.widget_140)
        self.water_start_le_19.setObjectName(u"water_start_le_19")
        self.water_start_le_19.setMinimumSize(QSize(0, 35))
        self.water_start_le_19.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_86.addWidget(self.water_start_le_19)

        self.label_129 = QLabel(self.widget_140)
        self.label_129.setObjectName(u"label_129")

        self.horizontalLayout_86.addWidget(self.label_129)


        self.horizontalLayout_112.addWidget(self.widget_140)

        self.widget_147 = QWidget(self.widget_67)
        self.widget_147.setObjectName(u"widget_147")
        self.widget_147.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_93 = QHBoxLayout(self.widget_147)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(2, 2, 2, 2)
        self.label_142 = QLabel(self.widget_147)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_93.addWidget(self.label_142)

        self.water_dur_le_19 = QLineEdit(self.widget_147)
        self.water_dur_le_19.setObjectName(u"water_dur_le_19")
        self.water_dur_le_19.setMinimumSize(QSize(0, 35))
        self.water_dur_le_19.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_93.addWidget(self.water_dur_le_19)

        self.label_143 = QLabel(self.widget_147)
        self.label_143.setObjectName(u"label_143")

        self.horizontalLayout_93.addWidget(self.label_143)


        self.horizontalLayout_112.addWidget(self.widget_147)

        self.widget_154 = QWidget(self.widget_67)
        self.widget_154.setObjectName(u"widget_154")
        self.widget_154.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_100 = QHBoxLayout(self.widget_154)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(2, 2, 2, 2)
        self.label_156 = QLabel(self.widget_154)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_100.addWidget(self.label_156)

        self.water_interval_le_19 = QLineEdit(self.widget_154)
        self.water_interval_le_19.setObjectName(u"water_interval_le_19")
        self.water_interval_le_19.setMinimumSize(QSize(0, 35))
        self.water_interval_le_19.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_100.addWidget(self.water_interval_le_19)

        self.label_157 = QLabel(self.widget_154)
        self.label_157.setObjectName(u"label_157")

        self.horizontalLayout_100.addWidget(self.label_157)


        self.horizontalLayout_112.addWidget(self.widget_154)

        self.widget_161 = QWidget(self.widget_67)
        self.widget_161.setObjectName(u"widget_161")
        self.widget_161.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_107 = QHBoxLayout(self.widget_161)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(2, 2, 2, 2)
        self.label_170 = QLabel(self.widget_161)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_107.addWidget(self.label_170)

        self.water_end_le_19 = QLineEdit(self.widget_161)
        self.water_end_le_19.setObjectName(u"water_end_le_19")
        self.water_end_le_19.setMinimumSize(QSize(0, 35))
        self.water_end_le_19.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_107.addWidget(self.water_end_le_19)

        self.label_171 = QLabel(self.widget_161)
        self.label_171.setObjectName(u"label_171")

        self.horizontalLayout_107.addWidget(self.label_171)


        self.horizontalLayout_112.addWidget(self.widget_161)


        self.verticalLayout_15.addWidget(self.widget_67)

        self.widget_70 = QWidget(self.col_wg_3)
        self.widget_70.setObjectName(u"widget_70")
        self.horizontalLayout_113 = QHBoxLayout(self.widget_70)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(1, 1, 1, 1)
        self.widget_185 = QWidget(self.widget_70)
        self.widget_185.setObjectName(u"widget_185")
        self.widget_185.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_162 = QHBoxLayout(self.widget_185)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalLayout_162.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_18 = QLabel(self.widget_185)
        self.valve_state_lbl_18.setObjectName(u"valve_state_lbl_18")
        self.valve_state_lbl_18.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_162.addWidget(self.valve_state_lbl_18)

        self.water_btn_18 = QPushButton(self.widget_185)
        self.water_btn_18.setObjectName(u"water_btn_18")
        self.water_btn_18.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_162.addWidget(self.water_btn_18)


        self.horizontalLayout_113.addWidget(self.widget_185)

        self.widget_139 = QWidget(self.widget_70)
        self.widget_139.setObjectName(u"widget_139")
        self.widget_139.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_85 = QHBoxLayout(self.widget_139)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(2, 2, 2, 2)
        self.label_126 = QLabel(self.widget_139)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_85.addWidget(self.label_126)

        self.water_start_le_18 = QLineEdit(self.widget_139)
        self.water_start_le_18.setObjectName(u"water_start_le_18")
        self.water_start_le_18.setMinimumSize(QSize(0, 35))
        self.water_start_le_18.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_85.addWidget(self.water_start_le_18)

        self.label_127 = QLabel(self.widget_139)
        self.label_127.setObjectName(u"label_127")

        self.horizontalLayout_85.addWidget(self.label_127)


        self.horizontalLayout_113.addWidget(self.widget_139)

        self.widget_146 = QWidget(self.widget_70)
        self.widget_146.setObjectName(u"widget_146")
        self.widget_146.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_92 = QHBoxLayout(self.widget_146)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(2, 2, 2, 2)
        self.label_140 = QLabel(self.widget_146)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_92.addWidget(self.label_140)

        self.water_dur_le_18 = QLineEdit(self.widget_146)
        self.water_dur_le_18.setObjectName(u"water_dur_le_18")
        self.water_dur_le_18.setMinimumSize(QSize(0, 35))
        self.water_dur_le_18.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_92.addWidget(self.water_dur_le_18)

        self.label_141 = QLabel(self.widget_146)
        self.label_141.setObjectName(u"label_141")

        self.horizontalLayout_92.addWidget(self.label_141)


        self.horizontalLayout_113.addWidget(self.widget_146)

        self.widget_153 = QWidget(self.widget_70)
        self.widget_153.setObjectName(u"widget_153")
        self.widget_153.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_99 = QHBoxLayout(self.widget_153)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(2, 2, 2, 2)
        self.label_154 = QLabel(self.widget_153)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_99.addWidget(self.label_154)

        self.water_interval_le_18 = QLineEdit(self.widget_153)
        self.water_interval_le_18.setObjectName(u"water_interval_le_18")
        self.water_interval_le_18.setMinimumSize(QSize(0, 35))
        self.water_interval_le_18.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_99.addWidget(self.water_interval_le_18)

        self.label_155 = QLabel(self.widget_153)
        self.label_155.setObjectName(u"label_155")

        self.horizontalLayout_99.addWidget(self.label_155)


        self.horizontalLayout_113.addWidget(self.widget_153)

        self.widget_160 = QWidget(self.widget_70)
        self.widget_160.setObjectName(u"widget_160")
        self.widget_160.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_106 = QHBoxLayout(self.widget_160)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(2, 2, 2, 2)
        self.label_168 = QLabel(self.widget_160)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_106.addWidget(self.label_168)

        self.water_end_le_18 = QLineEdit(self.widget_160)
        self.water_end_le_18.setObjectName(u"water_end_le_18")
        self.water_end_le_18.setMinimumSize(QSize(0, 35))
        self.water_end_le_18.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_106.addWidget(self.water_end_le_18)

        self.label_169 = QLabel(self.widget_160)
        self.label_169.setObjectName(u"label_169")

        self.horizontalLayout_106.addWidget(self.label_169)


        self.horizontalLayout_113.addWidget(self.widget_160)


        self.verticalLayout_15.addWidget(self.widget_70)

        self.widget_68 = QWidget(self.col_wg_3)
        self.widget_68.setObjectName(u"widget_68")
        self.horizontalLayout_114 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(1, 1, 1, 1)
        self.widget_184 = QWidget(self.widget_68)
        self.widget_184.setObjectName(u"widget_184")
        self.widget_184.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_161 = QHBoxLayout(self.widget_184)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.horizontalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_17 = QLabel(self.widget_184)
        self.valve_state_lbl_17.setObjectName(u"valve_state_lbl_17")
        self.valve_state_lbl_17.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_161.addWidget(self.valve_state_lbl_17)

        self.water_btn_17 = QPushButton(self.widget_184)
        self.water_btn_17.setObjectName(u"water_btn_17")
        self.water_btn_17.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_161.addWidget(self.water_btn_17)


        self.horizontalLayout_114.addWidget(self.widget_184)

        self.widget_138 = QWidget(self.widget_68)
        self.widget_138.setObjectName(u"widget_138")
        self.widget_138.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_84 = QHBoxLayout(self.widget_138)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(2, 2, 2, 2)
        self.label_124 = QLabel(self.widget_138)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_84.addWidget(self.label_124)

        self.water_start_le_17 = QLineEdit(self.widget_138)
        self.water_start_le_17.setObjectName(u"water_start_le_17")
        self.water_start_le_17.setMinimumSize(QSize(0, 35))
        self.water_start_le_17.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_84.addWidget(self.water_start_le_17)

        self.label_125 = QLabel(self.widget_138)
        self.label_125.setObjectName(u"label_125")

        self.horizontalLayout_84.addWidget(self.label_125)


        self.horizontalLayout_114.addWidget(self.widget_138)

        self.widget_145 = QWidget(self.widget_68)
        self.widget_145.setObjectName(u"widget_145")
        self.widget_145.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_91 = QHBoxLayout(self.widget_145)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(2, 2, 2, 2)
        self.label_138 = QLabel(self.widget_145)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_91.addWidget(self.label_138)

        self.water_dur_le_17 = QLineEdit(self.widget_145)
        self.water_dur_le_17.setObjectName(u"water_dur_le_17")
        self.water_dur_le_17.setMinimumSize(QSize(0, 35))
        self.water_dur_le_17.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_91.addWidget(self.water_dur_le_17)

        self.label_139 = QLabel(self.widget_145)
        self.label_139.setObjectName(u"label_139")

        self.horizontalLayout_91.addWidget(self.label_139)


        self.horizontalLayout_114.addWidget(self.widget_145)

        self.widget_152 = QWidget(self.widget_68)
        self.widget_152.setObjectName(u"widget_152")
        self.widget_152.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_98 = QHBoxLayout(self.widget_152)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(2, 2, 2, 2)
        self.label_152 = QLabel(self.widget_152)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_98.addWidget(self.label_152)

        self.water_interval_le_17 = QLineEdit(self.widget_152)
        self.water_interval_le_17.setObjectName(u"water_interval_le_17")
        self.water_interval_le_17.setMinimumSize(QSize(0, 35))
        self.water_interval_le_17.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_98.addWidget(self.water_interval_le_17)

        self.label_153 = QLabel(self.widget_152)
        self.label_153.setObjectName(u"label_153")

        self.horizontalLayout_98.addWidget(self.label_153)


        self.horizontalLayout_114.addWidget(self.widget_152)

        self.widget_159 = QWidget(self.widget_68)
        self.widget_159.setObjectName(u"widget_159")
        self.widget_159.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_105 = QHBoxLayout(self.widget_159)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(2, 2, 2, 2)
        self.label_166 = QLabel(self.widget_159)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_105.addWidget(self.label_166)

        self.water_end_le_17 = QLineEdit(self.widget_159)
        self.water_end_le_17.setObjectName(u"water_end_le_17")
        self.water_end_le_17.setMinimumSize(QSize(0, 35))
        self.water_end_le_17.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_105.addWidget(self.water_end_le_17)

        self.label_167 = QLabel(self.widget_159)
        self.label_167.setObjectName(u"label_167")

        self.horizontalLayout_105.addWidget(self.label_167)


        self.horizontalLayout_114.addWidget(self.widget_159)


        self.verticalLayout_15.addWidget(self.widget_68)

        self.widget_72 = QWidget(self.col_wg_3)
        self.widget_72.setObjectName(u"widget_72")
        self.horizontalLayout_115 = QHBoxLayout(self.widget_72)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(1, 1, 1, 1)
        self.widget_183 = QWidget(self.widget_72)
        self.widget_183.setObjectName(u"widget_183")
        self.widget_183.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_160 = QHBoxLayout(self.widget_183)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalLayout_160.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_16 = QLabel(self.widget_183)
        self.valve_state_lbl_16.setObjectName(u"valve_state_lbl_16")
        self.valve_state_lbl_16.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_160.addWidget(self.valve_state_lbl_16)

        self.water_btn_16 = QPushButton(self.widget_183)
        self.water_btn_16.setObjectName(u"water_btn_16")
        self.water_btn_16.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_160.addWidget(self.water_btn_16)


        self.horizontalLayout_115.addWidget(self.widget_183)

        self.widget_137 = QWidget(self.widget_72)
        self.widget_137.setObjectName(u"widget_137")
        self.widget_137.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_83 = QHBoxLayout(self.widget_137)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(2, 2, 2, 2)
        self.label_122 = QLabel(self.widget_137)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_83.addWidget(self.label_122)

        self.water_start_le_16 = QLineEdit(self.widget_137)
        self.water_start_le_16.setObjectName(u"water_start_le_16")
        self.water_start_le_16.setMinimumSize(QSize(0, 35))
        self.water_start_le_16.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_83.addWidget(self.water_start_le_16)

        self.label_123 = QLabel(self.widget_137)
        self.label_123.setObjectName(u"label_123")

        self.horizontalLayout_83.addWidget(self.label_123)


        self.horizontalLayout_115.addWidget(self.widget_137)

        self.widget_144 = QWidget(self.widget_72)
        self.widget_144.setObjectName(u"widget_144")
        self.widget_144.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_90 = QHBoxLayout(self.widget_144)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(2, 2, 2, 2)
        self.label_136 = QLabel(self.widget_144)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_90.addWidget(self.label_136)

        self.water_dur_le_16 = QLineEdit(self.widget_144)
        self.water_dur_le_16.setObjectName(u"water_dur_le_16")
        self.water_dur_le_16.setMinimumSize(QSize(0, 35))
        self.water_dur_le_16.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_90.addWidget(self.water_dur_le_16)

        self.label_137 = QLabel(self.widget_144)
        self.label_137.setObjectName(u"label_137")

        self.horizontalLayout_90.addWidget(self.label_137)


        self.horizontalLayout_115.addWidget(self.widget_144)

        self.widget_151 = QWidget(self.widget_72)
        self.widget_151.setObjectName(u"widget_151")
        self.widget_151.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_97 = QHBoxLayout(self.widget_151)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(2, 2, 2, 2)
        self.label_150 = QLabel(self.widget_151)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_97.addWidget(self.label_150)

        self.water_interval_le_16 = QLineEdit(self.widget_151)
        self.water_interval_le_16.setObjectName(u"water_interval_le_16")
        self.water_interval_le_16.setMinimumSize(QSize(0, 35))
        self.water_interval_le_16.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_97.addWidget(self.water_interval_le_16)

        self.label_151 = QLabel(self.widget_151)
        self.label_151.setObjectName(u"label_151")

        self.horizontalLayout_97.addWidget(self.label_151)


        self.horizontalLayout_115.addWidget(self.widget_151)

        self.widget_158 = QWidget(self.widget_72)
        self.widget_158.setObjectName(u"widget_158")
        self.widget_158.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_104 = QHBoxLayout(self.widget_158)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(2, 2, 2, 2)
        self.label_164 = QLabel(self.widget_158)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_104.addWidget(self.label_164)

        self.water_end_le_16 = QLineEdit(self.widget_158)
        self.water_end_le_16.setObjectName(u"water_end_le_16")
        self.water_end_le_16.setMinimumSize(QSize(0, 35))
        self.water_end_le_16.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_104.addWidget(self.water_end_le_16)

        self.label_165 = QLabel(self.widget_158)
        self.label_165.setObjectName(u"label_165")

        self.horizontalLayout_104.addWidget(self.label_165)


        self.horizontalLayout_115.addWidget(self.widget_158)


        self.verticalLayout_15.addWidget(self.widget_72)

        self.widget_71 = QWidget(self.col_wg_3)
        self.widget_71.setObjectName(u"widget_71")
        self.horizontalLayout_116 = QHBoxLayout(self.widget_71)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(1, 1, 1, 1)
        self.widget_182 = QWidget(self.widget_71)
        self.widget_182.setObjectName(u"widget_182")
        self.widget_182.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_159 = QHBoxLayout(self.widget_182)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(0, 0, 0, 0)
        self.valve_state_lbl_15 = QLabel(self.widget_182)
        self.valve_state_lbl_15.setObjectName(u"valve_state_lbl_15")
        self.valve_state_lbl_15.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_159.addWidget(self.valve_state_lbl_15)

        self.water_btn_15 = QPushButton(self.widget_182)
        self.water_btn_15.setObjectName(u"water_btn_15")
        self.water_btn_15.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_159.addWidget(self.water_btn_15)


        self.horizontalLayout_116.addWidget(self.widget_182)

        self.widget_136 = QWidget(self.widget_71)
        self.widget_136.setObjectName(u"widget_136")
        self.widget_136.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_82 = QHBoxLayout(self.widget_136)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(2, 2, 2, 2)
        self.label_120 = QLabel(self.widget_136)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMaximumSize(QSize(115, 16777215))

        self.horizontalLayout_82.addWidget(self.label_120)

        self.water_start_le_15 = QLineEdit(self.widget_136)
        self.water_start_le_15.setObjectName(u"water_start_le_15")
        self.water_start_le_15.setMinimumSize(QSize(0, 35))
        self.water_start_le_15.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_82.addWidget(self.water_start_le_15)

        self.label_121 = QLabel(self.widget_136)
        self.label_121.setObjectName(u"label_121")

        self.horizontalLayout_82.addWidget(self.label_121)


        self.horizontalLayout_116.addWidget(self.widget_136)

        self.widget_143 = QWidget(self.widget_71)
        self.widget_143.setObjectName(u"widget_143")
        self.widget_143.setMaximumSize(QSize(165, 16777215))
        self.horizontalLayout_89 = QHBoxLayout(self.widget_143)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(2, 2, 2, 2)
        self.label_134 = QLabel(self.widget_143)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_89.addWidget(self.label_134)

        self.water_dur_le_15 = QLineEdit(self.widget_143)
        self.water_dur_le_15.setObjectName(u"water_dur_le_15")
        self.water_dur_le_15.setMinimumSize(QSize(0, 35))
        self.water_dur_le_15.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_89.addWidget(self.water_dur_le_15)

        self.label_135 = QLabel(self.widget_143)
        self.label_135.setObjectName(u"label_135")

        self.horizontalLayout_89.addWidget(self.label_135)


        self.horizontalLayout_116.addWidget(self.widget_143)

        self.widget_150 = QWidget(self.widget_71)
        self.widget_150.setObjectName(u"widget_150")
        self.widget_150.setMaximumSize(QSize(210, 16777215))
        self.horizontalLayout_96 = QHBoxLayout(self.widget_150)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(2, 2, 2, 2)
        self.label_148 = QLabel(self.widget_150)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_96.addWidget(self.label_148)

        self.water_interval_le_15 = QLineEdit(self.widget_150)
        self.water_interval_le_15.setObjectName(u"water_interval_le_15")
        self.water_interval_le_15.setMinimumSize(QSize(0, 35))
        self.water_interval_le_15.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_96.addWidget(self.water_interval_le_15)

        self.label_149 = QLabel(self.widget_150)
        self.label_149.setObjectName(u"label_149")

        self.horizontalLayout_96.addWidget(self.label_149)


        self.horizontalLayout_116.addWidget(self.widget_150)

        self.widget_157 = QWidget(self.widget_71)
        self.widget_157.setObjectName(u"widget_157")
        self.widget_157.setMaximumSize(QSize(195, 16777215))
        self.horizontalLayout_103 = QHBoxLayout(self.widget_157)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(2, 2, 2, 2)
        self.label_162 = QLabel(self.widget_157)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_103.addWidget(self.label_162)

        self.water_end_le_15 = QLineEdit(self.widget_157)
        self.water_end_le_15.setObjectName(u"water_end_le_15")
        self.water_end_le_15.setMinimumSize(QSize(0, 35))
        self.water_end_le_15.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_103.addWidget(self.water_end_le_15)

        self.label_163 = QLabel(self.widget_157)
        self.label_163.setObjectName(u"label_163")

        self.horizontalLayout_103.addWidget(self.label_163)


        self.horizontalLayout_116.addWidget(self.widget_157)


        self.verticalLayout_15.addWidget(self.widget_71)


        self.verticalLayout_12.addWidget(self.col_wg_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.watering_pg)
        self.solution_config_pg = QWidget()
        self.solution_config_pg.setObjectName(u"solution_config_pg")
        self.verticalLayout_26 = QVBoxLayout(self.solution_config_pg)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_189 = QWidget(self.solution_config_pg)
        self.widget_189.setObjectName(u"widget_189")
        self.horizontalLayout_166 = QHBoxLayout(self.widget_189)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.widget_190 = QWidget(self.widget_189)
        self.widget_190.setObjectName(u"widget_190")
        self.widget_190.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_27 = QVBoxLayout(self.widget_190)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_203 = QWidget(self.widget_190)
        self.widget_203.setObjectName(u"widget_203")
        self.widget_203.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_27.addWidget(self.widget_203)

        self.widget_199 = QWidget(self.widget_190)
        self.widget_199.setObjectName(u"widget_199")
        self.horizontalLayout_171 = QHBoxLayout(self.widget_199)
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.widget_205 = QWidget(self.widget_199)
        self.widget_205.setObjectName(u"widget_205")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_205.sizePolicy().hasHeightForWidth())
        self.widget_205.setSizePolicy(sizePolicy)
        self.verticalLayout_28 = QVBoxLayout(self.widget_205)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget_198 = QWidget(self.widget_205)
        self.widget_198.setObjectName(u"widget_198")
        sizePolicy.setHeightForWidth(self.widget_198.sizePolicy().hasHeightForWidth())
        self.widget_198.setSizePolicy(sizePolicy)
        self.widget_198.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_175 = QHBoxLayout(self.widget_198)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_175.setContentsMargins(1, 1, 1, 1)
        self.label_233 = QLabel(self.widget_198)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setMaximumSize(QSize(185, 16777215))

        self.horizontalLayout_175.addWidget(self.label_233)

        self.conductivity_set_le_1 = QLineEdit(self.widget_198)
        self.conductivity_set_le_1.setObjectName(u"conductivity_set_le_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.conductivity_set_le_1.sizePolicy().hasHeightForWidth())
        self.conductivity_set_le_1.setSizePolicy(sizePolicy1)
        self.conductivity_set_le_1.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_175.addWidget(self.conductivity_set_le_1)

        self.label_234 = QLabel(self.widget_198)
        self.label_234.setObjectName(u"label_234")

        self.horizontalLayout_175.addWidget(self.label_234)


        self.verticalLayout_28.addWidget(self.widget_198)

        self.widget_197 = QWidget(self.widget_205)
        self.widget_197.setObjectName(u"widget_197")
        sizePolicy.setHeightForWidth(self.widget_197.sizePolicy().hasHeightForWidth())
        self.widget_197.setSizePolicy(sizePolicy)
        self.widget_197.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_174 = QHBoxLayout(self.widget_197)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalLayout_174.setContentsMargins(1, 1, 1, 1)
        self.label_231 = QLabel(self.widget_197)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setMaximumSize(QSize(185, 16777215))

        self.horizontalLayout_174.addWidget(self.label_231)

        self.con_interval_set_le_1 = QLineEdit(self.widget_197)
        self.con_interval_set_le_1.setObjectName(u"con_interval_set_le_1")
        sizePolicy1.setHeightForWidth(self.con_interval_set_le_1.sizePolicy().hasHeightForWidth())
        self.con_interval_set_le_1.setSizePolicy(sizePolicy1)
        self.con_interval_set_le_1.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_174.addWidget(self.con_interval_set_le_1)

        self.label_232 = QLabel(self.widget_197)
        self.label_232.setObjectName(u"label_232")

        self.horizontalLayout_174.addWidget(self.label_232)


        self.verticalLayout_28.addWidget(self.widget_197)

        self.widget_194 = QWidget(self.widget_205)
        self.widget_194.setObjectName(u"widget_194")
        sizePolicy.setHeightForWidth(self.widget_194.sizePolicy().hasHeightForWidth())
        self.widget_194.setSizePolicy(sizePolicy)
        self.widget_194.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_170 = QHBoxLayout(self.widget_194)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.horizontalLayout_170.setContentsMargins(1, 1, 1, 1)
        self.label_219 = QLabel(self.widget_194)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setMaximumSize(QSize(185, 16777215))

        self.horizontalLayout_170.addWidget(self.label_219)

        self.ph_set_le = QLineEdit(self.widget_194)
        self.ph_set_le.setObjectName(u"ph_set_le")
        sizePolicy1.setHeightForWidth(self.ph_set_le.sizePolicy().hasHeightForWidth())
        self.ph_set_le.setSizePolicy(sizePolicy1)
        self.ph_set_le.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_170.addWidget(self.ph_set_le)

        self.label_220 = QLabel(self.widget_194)
        self.label_220.setObjectName(u"label_220")

        self.horizontalLayout_170.addWidget(self.label_220)


        self.verticalLayout_28.addWidget(self.widget_194)

        self.widget_193 = QWidget(self.widget_205)
        self.widget_193.setObjectName(u"widget_193")
        sizePolicy.setHeightForWidth(self.widget_193.sizePolicy().hasHeightForWidth())
        self.widget_193.setSizePolicy(sizePolicy)
        self.widget_193.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_168 = QHBoxLayout(self.widget_193)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(1, 1, 1, 1)
        self.label_216 = QLabel(self.widget_193)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setMaximumSize(QSize(185, 16777215))

        self.horizontalLayout_168.addWidget(self.label_216)

        self.ph_interval_set_le = QLineEdit(self.widget_193)
        self.ph_interval_set_le.setObjectName(u"ph_interval_set_le")
        sizePolicy1.setHeightForWidth(self.ph_interval_set_le.sizePolicy().hasHeightForWidth())
        self.ph_interval_set_le.setSizePolicy(sizePolicy1)
        self.ph_interval_set_le.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_168.addWidget(self.ph_interval_set_le)

        self.label_218 = QLabel(self.widget_193)
        self.label_218.setObjectName(u"label_218")

        self.horizontalLayout_168.addWidget(self.label_218)


        self.verticalLayout_28.addWidget(self.widget_193)


        self.horizontalLayout_171.addWidget(self.widget_205)

        self.widget_206 = QWidget(self.widget_199)
        self.widget_206.setObjectName(u"widget_206")
        self.gridLayout_2 = QGridLayout(self.widget_206)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_217 = QLabel(self.widget_206)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setMaximumSize(QSize(178, 16777215))

        self.gridLayout_2.addWidget(self.label_217, 0, 0, 1, 1)

        self.con_cod_lbl = QLabel(self.widget_206)
        self.con_cod_lbl.setObjectName(u"con_cod_lbl")

        self.gridLayout_2.addWidget(self.con_cod_lbl, 0, 2, 1, 1)

        self.con_ph_lbl = QLabel(self.widget_206)
        self.con_ph_lbl.setObjectName(u"con_ph_lbl")

        self.gridLayout_2.addWidget(self.con_ph_lbl, 2, 2, 1, 1)

        self.label_226 = QLabel(self.widget_206)
        self.label_226.setObjectName(u"label_226")

        self.gridLayout_2.addWidget(self.label_226, 2, 0, 1, 1)

        self.con_ph_timer_lbl = QLabel(self.widget_206)
        self.con_ph_timer_lbl.setObjectName(u"con_ph_timer_lbl")

        self.gridLayout_2.addWidget(self.con_ph_timer_lbl, 3, 2, 1, 1)

        self.label_227 = QLabel(self.widget_206)
        self.label_227.setObjectName(u"label_227")

        self.gridLayout_2.addWidget(self.label_227, 3, 0, 1, 1)

        self.label_223 = QLabel(self.widget_206)
        self.label_223.setObjectName(u"label_223")

        self.gridLayout_2.addWidget(self.label_223, 1, 0, 1, 1)

        self.con_cod_timer_lbl = QLabel(self.widget_206)
        self.con_cod_timer_lbl.setObjectName(u"con_cod_timer_lbl")

        self.gridLayout_2.addWidget(self.con_cod_timer_lbl, 1, 2, 1, 1)


        self.horizontalLayout_171.addWidget(self.widget_206)


        self.verticalLayout_27.addWidget(self.widget_199)

        self.widget_204 = QWidget(self.widget_190)
        self.widget_204.setObjectName(u"widget_204")
        self.widget_204.setMaximumSize(QSize(16777215, 180))
        self.horizontalLayout_169 = QHBoxLayout(self.widget_204)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.save_sol_setting_btn = QPushButton(self.widget_204)
        self.save_sol_setting_btn.setObjectName(u"save_sol_setting_btn")
        self.save_sol_setting_btn.setMaximumSize(QSize(120, 40))

        self.horizontalLayout_169.addWidget(self.save_sol_setting_btn)


        self.verticalLayout_27.addWidget(self.widget_204)


        self.horizontalLayout_166.addWidget(self.widget_190)


        self.verticalLayout_26.addWidget(self.widget_189)

        self.stackedWidget.addWidget(self.solution_config_pg)
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

        self.stop_saving_frames_btn = QPushButton(self.widget_6)
        self.stop_saving_frames_btn.setObjectName(u"stop_saving_frames_btn")
        self.stop_saving_frames_btn.setMinimumSize(QSize(115, 0))
        self.stop_saving_frames_btn.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_3.addWidget(self.stop_saving_frames_btn)

        self.save_frame_btn = QPushButton(self.widget_6)
        self.save_frame_btn.setObjectName(u"save_frame_btn")
        self.save_frame_btn.setMinimumSize(QSize(100, 0))
        self.save_frame_btn.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_3.addWidget(self.save_frame_btn)


        self.verticalLayout_5.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.camera_pg)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.widget_191 = QWidget(self.widget_8)
        self.widget_191.setObjectName(u"widget_191")
        self.widget_191.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_138 = QHBoxLayout(self.widget_191)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.label_214 = QLabel(self.widget_191)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_138.addWidget(self.label_214)

        self.time_cam_lbl_1 = QLabel(self.widget_191)
        self.time_cam_lbl_1.setObjectName(u"time_cam_lbl_1")

        self.horizontalLayout_138.addWidget(self.time_cam_lbl_1)


        self.verticalLayout_6.addWidget(self.widget_191)

        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_21 = QVBoxLayout(self.widget_11)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.cam_lbl_1 = QLabel(self.widget_11)
        self.cam_lbl_1.setObjectName(u"cam_lbl_1")

        self.verticalLayout_21.addWidget(self.cam_lbl_1)


        self.verticalLayout_6.addWidget(self.widget_11)

        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_7 = QVBoxLayout(self.widget_9)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.verticalSpacer_3 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.widget_192 = QWidget(self.widget_9)
        self.widget_192.setObjectName(u"widget_192")
        self.widget_192.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_167 = QHBoxLayout(self.widget_192)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")

        self.verticalLayout_7.addWidget(self.widget_192)

        self.widget_13 = QWidget(self.widget_9)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_22 = QVBoxLayout(self.widget_13)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.cam_lbl_2 = QLabel(self.widget_13)
        self.cam_lbl_2.setObjectName(u"cam_lbl_2")

        self.verticalLayout_22.addWidget(self.cam_lbl_2)


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
        self.menubar.setGeometry(QRect(0, 0, 1482, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_4j_btn.setText("")
        self.watering_page_btn.setText(QCoreApplication.translate("MainWindow", u"Zavla\u017eov\u00e1n\u00ed", None))
        self.solutio_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u0158\u00edzen\u00ed", None))
        self.solution_config_btn.setText(QCoreApplication.translate("MainWindow", u"Konfigurace", None))
        self.cams_page_btn.setText(QCoreApplication.translate("MainWindow", u"Kamery", None))
        self.chart_page_btn.setText(QCoreApplication.translate("MainWindow", u"Grafy", None))
        self.stop_watering_btn.setText(QCoreApplication.translate("MainWindow", u"Zastavit zal\u00e9v\u00e1n\u00ed", None))
        self.expand_menu_btn.setText("")
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"Jmeno:", None))
        self.dir_name_btn.setText(QCoreApplication.translate("MainWindow", u"Nastavit jmeno", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017ei\u0161t\u011b:", None))
        self.solution_dir_btn.setText("")
        self.stop_saving_btn.setText(QCoreApplication.translate("MainWindow", u"P\u0159estat ukl\u00e1dat", None))
        self.start_saving_btn.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00edt ukl\u00e1dat", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Vn\u011bj\u0161\u00ed podm\u00ednky p\u011bstebn\u00ed st\u011bna", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"Teplota:", None))
        self.wall_tep_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"\u00baC", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"Vlhkost:", None))
        self.wall_hum_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"CO2:", None))
        self.wall_co2_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"ppm", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Parametry vody", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Kysl\u00edk:", None))
        self.water_oxyd_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"mg/l", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"pH:", None))
        self.water_ph_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_187.setText("")
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"Redox potenci\u00e1l:", None))
        self.water_redox_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Elektrick\u00e1 vodivost:", None))
        self.water_cond_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"uS/cm", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Teplota vody:", None))
        self.water_temp_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"\u00baC", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"Vn\u011bj\u0161\u00ed podm\u00ednky studovna", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"Teplota:", None))
        self.outside_temp_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"\u00baC", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Vlhkost:", None))
        self.outside_hum_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"CO2:", None))
        self.outside_co2_lbl.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"ppm", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"Regulace pH", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"Vy\u017eadovan\u00e1 hodnota:", None))
        self.set_ph_value_btn.setText(QCoreApplication.translate("MainWindow", u"Nastavit", None))
        self.ph_on_btn.setText(QCoreApplication.translate("MainWindow", u"Zapnout", None))
        self.ph_off_btn.setText(QCoreApplication.translate("MainWindow", u"Vypnout", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"Regulace okysli\u010den\u00ed", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"Vy\u017eadovan\u00e1 hodnota:", None))
        self.pump_chb.setText("")
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"Kompresor", None))
        self.set_oxy_value_btn.setText(QCoreApplication.translate("MainWindow", u"Nastavit", None))
        self.oxidation_on_btn.setText(QCoreApplication.translate("MainWindow", u"Zapnout", None))
        self.oxidation_off_btn.setText(QCoreApplication.translate("MainWindow", u"Vypnout", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"Regulace vodivosti", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"Vy\u017eadovan\u00e1 hodnota:", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"1/", None))
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"Pom\u011br A/B", None))
        self.set_cond_value_btn.setText(QCoreApplication.translate("MainWindow", u"Nastavit", None))
        self.cond_reg_on_btn.setText(QCoreApplication.translate("MainWindow", u"Zapnout", None))
        self.cond_reg_off_btn.setText(QCoreApplication.translate("MainWindow", u"Vypnout", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"Nastaven\u00ed sv\u011btel", None))
        self.automatic_lights_chb.setText("")
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"automatick\u00e9 osv\u011btlen\u00ed", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"Zap\u00edn\u00e1n\u00ed sv\u011btel:", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"Vyp\u00edn\u00e1n\u00ed sv\u011btel:", None))
        self.save_lights_btn.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit", None))
        self.lights_on_btn.setText(QCoreApplication.translate("MainWindow", u"Zapnout sv\u011btla", None))
        self.lights_off_btn.setText(QCoreApplication.translate("MainWindow", u"Vypnout sv\u011btla", None))
        self.auto_watering_chb.setText("")
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"Automatick\u00e9 zavla\u017eov\u00e1n\u00ed", None))
        self.save_watering_setting_btn.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit nastaven\u00ed", None))
        self.current_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Vratit aktualn\u00ed nastaven\u00ed", None))
        self.water_all_btn.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt v\u0161e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sloupec 1:", None))
        self.stop_watering_col_1.setText(QCoreApplication.translate("MainWindow", u"Zastavit zal\u00e9v\u00e1n\u00ed", None))
        self.water_col_btn_1.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt sloupec", None))
        self.fill_column_btn_1.setText(QCoreApplication.translate("MainWindow", u"Nastavit sloupec", None))
        self.valve_state_lbl_7.setText("")
        self.water_btn_7.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_6.setText("")
        self.water_btn_6.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_5.setText("")
        self.water_btn_5.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_4.setText("")
        self.water_btn_4.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_3.setText("")
        self.water_btn_3.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_2.setText("")
        self.water_btn_2.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_1.setText("")
        self.water_btn_1.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sloupec 2:", None))
        self.stop_watering_col_2.setText(QCoreApplication.translate("MainWindow", u"Zastavit zal\u00e9v\u00e1n\u00ed", None))
        self.water_col_btn_2.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt sloupec", None))
        self.fill_column_btn_2.setText(QCoreApplication.translate("MainWindow", u"Nastavit sloupec", None))
        self.valve_state_lbl_14.setText("")
        self.water_btn_14.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_13.setText("")
        self.water_btn_13.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_12.setText("")
        self.water_btn_12.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_11.setText("")
        self.water_btn_11.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_10.setText("")
        self.water_btn_10.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_9.setText("")
        self.water_btn_9.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_8.setText("")
        self.water_btn_8.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sloupec 3:", None))
        self.stop_watering_col_3.setText(QCoreApplication.translate("MainWindow", u"Zastavit zal\u00e9v\u00e1n\u00ed", None))
        self.water_col_btn_3.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt sloupec", None))
        self.fill_column_btn_3.setText(QCoreApplication.translate("MainWindow", u"Nastavit sloupec", None))
        self.valve_state_lbl_21.setText("")
        self.water_btn_21.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_20.setText("")
        self.water_btn_20.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_19.setText("")
        self.water_btn_19.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_18.setText("")
        self.water_btn_18.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_17.setText("")
        self.water_btn_17.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_16.setText("")
        self.water_btn_16.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.valve_state_lbl_15.setText("")
        self.water_btn_15.setText(QCoreApplication.translate("MainWindow", u"Zal\u00edt", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Za\u010d\u00e1tek zal\u00e9v\u00e1n\u00ed:", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka zalit\u00ed:", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"\u010cas mezi zalit\u00edm:", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Konec zalev\u00e1n\u00ed:", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"\u010das", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"Vodivost:", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"ml", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"Vodivost \u010dasov\u00fd rozestup:", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"pH:", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"ml", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"pH \u010dasov\u00fd rozestup:", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"Nastaveno:", None))
        self.con_cod_lbl.setText(QCoreApplication.translate("MainWindow", u"XX", None))
        self.con_ph_lbl.setText(QCoreApplication.translate("MainWindow", u"XX", None))
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"Nastaveno:", None))
        self.con_ph_timer_lbl.setText(QCoreApplication.translate("MainWindow", u"XX", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"Nastaveno:", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"Nastaveno:", None))
        self.con_cod_timer_lbl.setText(QCoreApplication.translate("MainWindow", u"XX", None))
        self.save_sol_setting_btn.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit nastaven\u00ed", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cam_dir_btn.setText("")
        self.stop_saving_frames_btn.setText(QCoreApplication.translate("MainWindow", u"P\u0159estat ukl\u00e1dat", None))
        self.save_frame_btn.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit sn\u00edmek", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"\u010cas posledn\u00edho sn\u00edmku:", None))
        self.time_cam_lbl_1.setText("")
        self.cam_lbl_1.setText("")
        self.cam_lbl_2.setText("")
    # retranslateUi

