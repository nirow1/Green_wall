from random import randrange

from PySide6.QtWidgets import QMainWindow, QFileDialog, QLineEdit, QBoxLayout, QSizePolicy, QPushButton, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QPropertyAnimation, QTimer
from functools import partial

from Qt_files.ui_Green_wall import Ui_MainWindow
from Device_communication.logo import LogoControl
from Gui.Charts.line_chart import LineChart


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_graphical_changes()
        self.logo = LogoControl()
        #self.logo.start()
        self.line_chart = LineChart("test", 200, (-100, 100), ["test_line", "test_line_2"], 2)
        self.line_chart_2 = LineChart("test2", 200, (-100, 100))
        self.ui.chart_1.addWidget(self.line_chart)
        self.ui.chart_2.addWidget(self.line_chart_2)


        self.button_functions()

    def _init_graphical_changes(self):
        self.ui.expand_menu_btn.setIcon(QIcon("./App_data/ico.png"))
        self.ui.logo_4j_btn.setIcon(QIcon('./App_data/4j_logo_150x50.png'))
        self.ui.solution_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.cam_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.expand_wgt.setHidden(True)

        self.setWindowIcon(QIcon("./App_data/ico.png"))
        self.setWindowTitle("Pěstevní stěna")
        self.setMinimumSize(1500, 900)
        self.ui.stackedWidget.setCurrentWidget(self.ui.watering_pg)
        self.showMaximized()

    def button_functions(self):
        self.ui.logo_4j_btn.clicked.connect(lambda: self.menu_animation(True))
        self.ui.expand_menu_btn.clicked.connect(lambda: self.menu_animation(False))

        self.ui.watering_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.watering_pg))
        self.ui.solutio_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.solution_pg))
        self.ui.cams_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.camera_pg))
        self.ui.chart_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.chart_pg))

        self.ui.cam_dir_btn.clicked.connect(lambda: self._open_dir_dialog(self.ui.cam_dir_le))
        self.ui.solution_dir_btn.clicked.connect(lambda: self._open_dir_dialog(self.ui.solution_dir_le))

        self.ui.fill_column_btn_1.clicked.connect(lambda: self.fill_column(0))
        self.ui.fill_column_btn_2.clicked.connect(lambda: self.fill_column(1))
        self.ui.fill_column_btn_3.clicked.connect(lambda: self.fill_column(2))
        self.bind_waterinG_panel_btns()
        timer = QTimer(self)
        timer.timeout.connect(self.update_charts)
        timer.start(1000)

    def bind_waterinG_panel_btns(self):
        for i in range(1, 22):
            water_btn: QPushButton = self.ui.scrollArea.findChild(QPushButton, f"water_btn_{i}")

            water_btn.clicked.connect(partial(self.start_watering, i=i))

    def start_watering(self, i):
        water: QLineEdit = self.ui.scrollArea.findChild(QLineEdit, f"water_start_le_{i}")
        print(water.text())

    def fill_column(self, col):
        alert = QMessageBox.question(self.ui.scrollArea,
                                    "Pěstevní stěna",
                                    "chcete nastavit sloupec podle první hodnoty?")
        pos = col*7+1
        le_names = ["water_start_le_", "water_dur_le_", "water_interval_le_", "water_end_le_"]
        le_values = []
        if alert == QMessageBox.StandardButton.Yes:
            for name in le_names:
                le_values.append(self.ui.scrollArea.findChild(QLineEdit, name+str(pos)).text())
            for i in range(pos+1, pos+7):
                for j, name in enumerate(le_names):
                    start_le: QLineEdit = self.ui.scrollArea.findChild(QLineEdit, name + str(i))
                    start_le.setText(le_values[j])

    def _open_dir_dialog(self, lineedit: QLineEdit):
        options = QFileDialog(self).options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        lineedit.setText(folder_path)

    def menu_animation(self, state: bool):
        start = 180 if state else 0
        end = 0 if state else 180
        self.animation = QPropertyAnimation(self.ui.widget, b"maximumWidth")
        self.animation.setDuration(200)
        print("start: "+ str(start))
        print("end: "+ str(end))
        self.animation.setStartValue(start)
        self.animation.setEndValue(end)
        self.animation.finished.connect(lambda: self.ui.widget.setMaximumWidth(end))
        self.animation.start()
        self.ui.expand_wgt.setHidden(not state)

    def update_charts(self):
        chart1 = randrange(0, 101)
        chart2 = randrange(-50, 50)
        self.line_chart.update_chart([chart1, chart2])
        self.line_chart_2.update_chart([chart2])
