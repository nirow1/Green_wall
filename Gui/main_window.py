from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize
from functools import partial

from Qt_files.ui_Green_wall import Ui_MainWindow
from Device_communication.logo import LogoControl


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_graphical_changes()
        self.logo = LogoControl()
        #self.logo.start()

        self.button_functions()

    def _init_graphical_changes(self):
        self.ui.logo_4j_lbl.setPixmap(QPixmap('./App_data/4j_logo_150x50.png'))
        self.ui.solution_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.solution_dir_btn.setIconSize(QSize(54, 30))
        self.ui.cam_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.cam_dir_btn.setIconSize(QSize(54, 30))

        self.setWindowIcon(QIcon("./App_data/ico.png"))
        self.setWindowTitle("Pneu Friction")
        self.setMinimumSize(1500, 900)
        self.ui.stackedWidget.setCurrentWidget(self.ui.watering_pg)
        self.showMaximized()

    def button_functions(self):
        self.ui.watering_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.watering_pg))
        self.ui.solutio_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.solution_pg))
        self.ui.cams_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.camera_pg))
        self.ui.chart_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.chart_pg))
