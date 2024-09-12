from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QPixmap
from functools import partial
from PIL import Image

from Qt_files.ui_untitled import Ui_MainWindow
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

        self.setWindowIcon(QIcon("./App_data/ico.png"))
        self.setWindowTitle("Pneu Friction")
        self.setMinimumSize(1500, 800)
        self.showMaximized()

    def button_functions(self):
        pass

