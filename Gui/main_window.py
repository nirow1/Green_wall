import struct
from random import randrange

import cv2
from PySide6.QtWidgets import QMainWindow, QFileDialog, QLineEdit, QPushButton, QMessageBox, QLabel
from PySide6.QtCore import QPropertyAnimation, QTimer, Qt
from PySide6.QtGui import QIcon, QImage, QPixmap
from functools import partial

from Utils.number_validator import NumberValidator
from Device_communication.logo import LogoControl
from Device_communication.ip_camera import Camera
from Qt_files.ui_Green_wall import Ui_MainWindow
from Utils.time_validator import TimeValidator
from Gui.Charts.line_chart import LineChart


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_graphical_changes()

        # variables
        self.valve_byte_1 = bytearray(b'\x00\x00')
        self.valve_byte_2 = bytearray(b'\x00\x00')

        self.logo = LogoControl("192.168.1.10")
        self.logo_2 = LogoControl("192.168.1.11")
        self.cam = Camera("192.168.1.50", 10)
        self.cam_2 = Camera("192.168.1.51", 10)

        self.logo.start()
        self.logo_2.start()
        self.cam.start()
        self.cam_2.start()

        # cart initializations
        self.line_chart = LineChart("test", 200, (-100, 100), ["test_line", "test_line_2"], 2)
        self.line_chart_2 = LineChart("test2", 200, (-100, 100))
        self.ui.chart_1.addWidget(self.line_chart)
        self.ui.chart_2.addWidget(self.line_chart_2)

        self.setup_validators()

        self.side_panel_animation = QPropertyAnimation(self.ui.widget, b"maximumWidth")
        self.button_functions()
        self._handle_emits()

    def _init_graphical_changes(self):
        self.ui.expand_menu_btn.setIcon(QIcon("./App_data/ico.png"))
        self.ui.logo_4j_btn.setIcon(QIcon('./App_data/4j_logo_150x50.png'))
        self.ui.solution_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.cam_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.expand_wgt.setHidden(True)

        self.ui.stop_saving_btn.hide()
        self.ui.ph_off_btn.hide()
        self.ui.oxidation_off_btn.hide()
        self.ui.lights_off_btn.hide()

        self.setWindowIcon(QIcon("./App_data/ico.png"))
        self.setWindowTitle("Pěstevní stěna")
        self.setMinimumSize(1500, 900)
        self.ui.stackedWidget.setCurrentWidget(self.ui.watering_pg)
        self.showMaximized()

    def setup_validators(self):
        time_validator = TimeValidator()
        n3_validator = NumberValidator(3)
        n4_validator = NumberValidator(4)
        for i in range(1, 22):
            start: QLineEdit = self.ui.scrollArea.findChild(QLineEdit, f"water_start_le_{str(i)}")
            start.setValidator(time_validator)
            end: QLineEdit = self.ui.scrollArea.findChild(QLineEdit, f"water_end_le_{str(i)}")
            end.setValidator(time_validator)
            between: QLineEdit = self.ui.scrollArea.findChild(QLineEdit, f"water_interval_le_{str(i)}")
            between.setValidator(n3_validator)
            duration: QLineEdit = self.ui.scrollArea.findChild(QLineEdit, f"water_dur_le_{str(i)}")
            duration.setValidator(n3_validator)
        self.ui.lights_on_le.setValidator(time_validator)
        self.ui.lights_off_le.setValidator(time_validator)
        self.ui.ph_reg_le.setValidator(n4_validator)
        self.ui.oxygenation_reg_le.setValidator(n4_validator)
        self.ui.cond_reg_le.setValidator(n4_validator)
        self.ui.add_cond_solution_le.setValidator(n3_validator)
        self.ui.add_ph_solution_le.setValidator(n3_validator)


    def button_functions(self):
        self.ui.logo_4j_btn.clicked.connect(lambda: self._menu_animation(True))
        self.ui.expand_menu_btn.clicked.connect(lambda: self._menu_animation(False))

        self.ui.watering_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.watering_pg))
        self.ui.save_watering_setting_btn.clicked.connect(self._save_watering_data
                                                          )
        self.ui.solutio_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.solution_pg))
        self.ui.cams_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.camera_pg))
        self.ui.chart_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.chart_pg))

        self.ui.cam_dir_btn.clicked.connect(lambda: self._open_dir_dialog(self.ui.cam_dir_le))
        self.ui.solution_dir_btn.clicked.connect(lambda: self._open_dir_dialog(self.ui.solution_dir_le))

        self.ui.fill_column_btn_1.clicked.connect(lambda: self._fill_column(0))
        self.ui.fill_column_btn_2.clicked.connect(lambda: self._fill_column(1))
        self.ui.fill_column_btn_3.clicked.connect(lambda: self._fill_column(2))
        self._bind_watering_panel_btns()
        timer = QTimer(self)
        timer.timeout.connect(self._update_charts)
        timer.start(1000)

    def _handle_emits(self):
        self.cam.NEW_IMAGE.connect(lambda frame: self._update_cam_view("1", frame))
        self.cam_2.NEW_IMAGE.connect(lambda frame: self._update_cam_view("2", frame))

    def _bind_watering_panel_btns(self):
        for i in range(1, 22):
            water_btn: QPushButton = self.ui.scrollArea.findChild(QPushButton, f"water_btn_{i}")
            water_btn.clicked.connect(partial(self._start_watering, i=i))

        self.ui.pushButton_4.clicked.connect(lambda: print(f"{self.valve_byte_1}, {self.valve_byte_2}"))

    def _start_watering(self, i):
        if i <= 8:
            self.valve_byte_1 = self._on_off_bit(i, self.valve_byte_1)
            self.logo.write_logo_byte(1, self.valve_byte_1)
        else:
            self.valve_byte_2 = self._on_off_bit(i-8, self.valve_byte_2)
            self.logo_2.write_logo_byte(1, self.valve_byte_2)

    def _fill_column(self, col):
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

    def _menu_animation(self, state: bool):
        start = 180 if state else 0
        end = 0 if state else 180
        self.side_panel_animation.setDuration(200)
        self.side_panel_animation.setStartValue(start)
        self.side_panel_animation.setEndValue(end)
        self.side_panel_animation.finished.connect(lambda: self.ui.widget.setMaximumWidth(end))
        self.side_panel_animation.start()
        self.ui.expand_wgt.setHidden(not state)

    def _update_cam_view(self, i: str, frame):
        cam_display: QLabel= self.ui.widget_7.findChild(QLabel, f"cam_lbl_{i}")
        # Ensure correct color format
        h, w, ch = frame.shape
        window_width = cam_display.width()
        window_height = cam_display.height()

        aspect_ratio = w / h

        new_w = int(window_width)
        new_h = int(new_w / aspect_ratio)

        if new_h > window_height:
            new_h = window_height
            new_w = int(new_h * aspect_ratio)

        resized_frame = cv2.resize(frame, (new_w, new_h))

        bytes_per_line = ch * new_w
        q_image = QImage(resized_frame.data, new_w, new_h, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        cam_display.setPixmap(pixmap)
        cam_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def _update_charts(self):
        chart1 = randrange(0, 101)
        chart2 = randrange(-50, 50)
        self.line_chart.update_chart([chart1, chart2])
        self.line_chart_2.update_chart([chart2])

    def _save_watering_data(self):
        self.logo.write_logo_byte(400, self._data_to_bytearray(1, 17))
        self.logo_2.write_logo_byte(400, self._data_to_bytearray(17, 21))

    def _data_to_bytearray(self, start, end) -> bytearray:
        data_array = b''
        for i in range(start, end):
            data_array += self._time_to_hexa(self.ui.scrollArea.findChild(QLineEdit, f"water_start_le_{str(i)}").text())
            data_array += self._ushort_to_hexa(self.ui.scrollArea.findChild(QLineEdit, f"water_dur_le_{str(i)}").text())
            data_array += self._ushort_to_hexa(self.ui.scrollArea.findChild(QLineEdit, f"water_interval_le_{str(i)}").text())
            data_array += self._time_to_hexa(self.ui.scrollArea.findChild(QLineEdit, f"water_end_le_{str(i)}").text())
        return bytearray(data_array)

    @staticmethod
    def _on_off_bit(i :int, current_byte: bytearray):
        logo_byte = current_byte
        byte_index = (i - 1) // 8
        bit_index = (i - 1) % 8
        logo_byte[byte_index] ^= (1<< bit_index)
        return logo_byte

    @staticmethod
    def _ushort_to_hexa(value: str):
        if value == "":
            value = 0
        print(struct.pack('>H', int(value)))
        return bytearray(struct.pack('>H', int(value)))

    @staticmethod
    def _time_to_hexa(time: str):
        if time == "":
            time = "0000"
        return bytearray.fromhex(time.replace(':', ''))

    """string = self.ui.water_start_le_1.text().replace(':', '')
        hexa_array = [string[i:i+2]for i in range(0, len(string), 2)]
        my_bytearray = bytearray(int(pair, 16)for pair in hexa_array)"""
