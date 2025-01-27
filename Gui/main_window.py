import time
from threading import Thread

import numpy as np
import csv
import cv2
import os

from PySide6.QtWidgets import QMainWindow, QFileDialog, QLineEdit, QPushButton, QMessageBox, QLabel
from PySide6.QtCore import QPropertyAnimation, QTimer, Qt
from PySide6.QtGui import QIcon, QImage, QPixmap
from datetime import datetime
from functools import partial

from Utils.static_methods import dict_to_bytearray, time_to_hexa, ushort_to_hexa
from Utils.number_validator import NumberValidator
from Device_communication.logo import LogoControl
from Device_communication.ip_camera import Camera
from Qt_files.ui_Green_wall import Ui_MainWindow
from Utils.time_validator import TimeValidator
from Gui.Charts.line_chart import TimedLineChart


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_graphical_changes()

        # variables
        self.valve_byte_1 =  {i: False for i in range(1, 17)}
        self.valve_byte_2 = {i: False for i in range(1, 17)}
        self.cond_byte = {i: False for i in range(1, 9)}
        self.ph_byte = {i: False for i in range(1, 9)}
        self.oxyd_byte = {i: False for i in range(1, 9)}

        self.environmental_data = []
        self.water_data = []
        self.save_file_path: str= ""
        self.saving: bool= False
        self.dir_name: str= ""

        self.logo = LogoControl("192.168.1.10")
        self.logo_2 = LogoControl("192.168.1.11")
        self.cam = Camera("192.168.1.50", 10)
        self.cam_2 = Camera("192.168.1.51", 10)
        self.pictures = [[], []]

        self.logo.start()
        self.logo_2.start()
        self.cam.start()
        self.cam_2.start()

        # cart initializations
        self.line_chart = TimedLineChart("test", 10, (-10, 10), [], 5)
        self.line_chart_2 = TimedLineChart("test2", 400, (-100, 100))
        self.line_chart_3 = TimedLineChart("test3", 86400, (-100, 100))
        self.line_chart_4 = TimedLineChart("test4", 86400, (-100, 100))
        self.line_chart_5 = TimedLineChart("test5", 86400, (-100, 100))
        self.ui.chart_1.addWidget(self.line_chart)
        self.ui.chart_2.addWidget(self.line_chart_2)
        self.ui.chart_3.addWidget(self.line_chart_3)
        self.ui.chart_4.addWidget(self.line_chart_4)
        self.ui.chart_5.addWidget(self.line_chart_5)

        environment_update = QTimer(self)
        environment_update.timeout.connect(self.environmental_data_update)
        environment_update.start(3000)#180000)

        water_update = QTimer(self)
        water_update.timeout.connect(self.water_data_update)
        water_update.start(1000)#30000)

        self._setup_validators()

        self.side_panel_animation = QPropertyAnimation(self.ui.widget, b"maximumWidth")
        self._button_functions()
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
        self.ui.cond_reg_off_btn.hide()

        self._switch_all_leds("grey")

        self.setWindowIcon(QIcon("./App_data/ico.png"))
        self.setWindowTitle("Pěstební stěna")
        self.setMinimumSize(1500, 900)
        self.ui.stackedWidget.setCurrentWidget(self.ui.watering_pg)
        self.showMaximized()

    def _setup_validators(self):
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

    def _button_functions(self):
        self.ui.logo_4j_btn.clicked.connect(lambda: self._menu_animation(True))
        self.ui.expand_menu_btn.clicked.connect(lambda: self._menu_animation(False))

        self.ui.watering_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.watering_pg))
        self.ui.save_watering_setting_btn.clicked.connect(self._save_watering_data)
        self.ui.current_settings_btn.clicked.connect(self._load_valve_settings)

        self.ui.solutio_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.solution_pg))
        self.ui.cams_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.camera_pg))
        self.ui.chart_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.chart_pg))
        self.ui.solution_config_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.solution_config_pg))

        self.ui.dir_name_btn.clicked.connect(self._set_dir_mame)
        self.ui.start_saving_btn.clicked.connect(lambda: self._set_saving(True))
        self.ui.stop_saving_btn.clicked.connect(lambda: self._set_saving(False))

        self.ui.save_frame_btn.clicked.connect(self._save_current_frame)

        self.ui.cam_dir_btn.clicked.connect(lambda: self._open_dir_dialog(self.ui.cam_dir_le))
        self.ui.solution_dir_btn.clicked.connect(lambda: self._open_dir_dialog(self.ui.solution_dir_le))

        self.ui.cond_reg_on_btn.clicked.connect(lambda: self._regulate_conductivity(True))
        self.ui.cond_reg_off_btn.clicked.connect(lambda: self._regulate_conductivity(False))

        self.ui.ph_on_btn.clicked.connect(lambda: self._regulate_ph(True))
        self.ui.ph_off_btn.clicked.connect(lambda: self._regulate_ph(False))

        self.ui.oxidation_on_btn.clicked.connect(lambda: self._regulate_oxidation(True))
        self.ui.oxidation_off_btn.clicked.connect(lambda: self._regulate_oxidation(False))
        self.ui.pump_chb.clicked.connect(self.switch_pump)

        self.ui.lights_on_btn.clicked.connect(lambda: self._switch_lights(True))
        self.ui.lights_off_btn.clicked.connect(lambda: self._switch_lights(False))
        self.ui.save_lights_btn.clicked.connect(self._save_lights)

        self.ui.water_all_btn.clicked.connect(lambda: self._manage_all(True, "green"))
        self.ui.stop_watering_btn.clicked.connect(lambda: self._manage_all(False, "grey"))

        self.ui.stop_watering_col_1.clicked.connect(lambda: self._manage_col(1, False))
        self.ui.stop_watering_col_2.clicked.connect(lambda: self._manage_col(2, False))
        self.ui.stop_watering_col_3.clicked.connect(lambda: self._manage_col(3, False))
        self.ui.water_col_btn_1.clicked.connect(lambda: self._manage_col(1, True))
        self.ui.water_col_btn_2.clicked.connect(lambda: self._manage_col(2, True))
        self.ui.water_col_btn_3.clicked.connect(lambda: self._manage_col(3, True))
        self.ui.fill_column_btn_1.clicked.connect(lambda: self._fill_column(0))
        self.ui.fill_column_btn_2.clicked.connect(lambda: self._fill_column(1))
        self.ui.fill_column_btn_3.clicked.connect(lambda: self._fill_column(2))

    def _handle_emits(self):
        self.cam.NEW_IMAGE.connect(lambda frame: self._update_cam_view("1", frame))
        self.cam_2.NEW_IMAGE.connect(lambda frame: self._update_cam_view("2", frame))
        self.logo.LOGO_DATA.connect(lambda data: self._add_data_to_gui(data))
        self.logo_2.LOGO_DATA.connect(lambda data: self._add_data_to_gui_2(data))

    def _bind_watering_panel_btns(self):
        for i in range(1, 22):
            water_btn: QPushButton = self.ui.scrollArea.findChild(QPushButton, f"water_btn_{i}")
            water_btn.clicked.connect(partial(self._open_valve, i=i))

    def _open_valve(self, i):
        if i <= 8:
            self.valve_byte_1[i] = not self.valve_byte_1[i]
            self.logo.write_logo_byte(1, dict_to_bytearray(self.valve_byte_1))
            self._switch_led(i, "green" if self.valve_byte_1[i] else "grey")
        else:
            self.valve_byte_2[i-8] = not self.valve_byte_2[i-8]
            self.logo_2.write_logo_byte(1, dict_to_bytearray(self.valve_byte_2))
            self._switch_led(i, "green" if self.valve_byte_2[i-8] else "grey")

    def _manage_col(self, col: int, state: bool):
        if col == 1:
            for i in range(1, 8):
                self.valve_byte_1[i] = state
                self._switch_led(i, "green" if state else "grey")
            self.logo.write_logo_byte(1, dict_to_bytearray(self.valve_byte_1))
        elif col == 2:
            self.valve_byte_1[8] = state
            self._switch_led(8,  "green" if state else "grey")
            for i in range(1, 7):
                self.valve_byte_2[i] = state
                self._switch_led(i + 8, "green" if state else "grey")
            self.logo.write_logo_byte(1, dict_to_bytearray(self.valve_byte_1))
            self.logo_2.write_logo_byte(1, dict_to_bytearray(self.valve_byte_2))
        else:
            for i in range(7, 14):
                self.valve_byte_2[i] = state
                self._switch_led(i + 8, "green" if state else "grey")
            self.logo_2.write_logo_byte(1, dict_to_bytearray(self.valve_byte_2))

    def _fill_column(self, col):
        alert = QMessageBox.question(self.ui.scrollArea,
                                    "Pěstební stěna",
                                    "Chcete nastavit sloupec podle první hodnoty?")
        pos = col*7+7
        le_names = ["water_start_le_", "water_dur_le_", "water_interval_le_", "water_end_le_"]
        le_values = []
        if alert == QMessageBox.StandardButton.Yes:
            for name in le_names:
                le_values.append(self.ui.scrollArea.findChild(QLineEdit, name+str(pos)).text())
            print(le_values)
            for i in range(pos, pos-7, -1):
                print(i)
                for j, name in enumerate(le_names):
                    start_le: QLineEdit = self.ui.scrollArea.findChild(QLineEdit, name + str(i))
                    start_le.setText(le_values[j])

    def _manage_all(self, state: bool, color: str):
        for i in range(1, 9):
            self.valve_byte_1[i] = state
        self.logo.write_logo_byte(1, dict_to_bytearray(self.valve_byte_1))
        for i in range(1, 16):
            self.valve_byte_2[i] = state
        self.logo_2.write_logo_byte(1, dict_to_bytearray(self.valve_byte_2))
        self._switch_all_leds(color)

    def _regulate_conductivity(self, state: bool):
        self.ui.cond_reg_on_btn.setHidden(state)
        self.ui.cond_reg_off_btn.setHidden(not state)
        self.cond_byte[1] = state
        self.cond_byte[2] = state
        self.cond_byte[4] = state
        if state:
            self.logo.write_logo_byte(300, dict_to_bytearray(self.cond_byte))
            self.logo.write_logo_ushort(322, int(self.ui.cond_ratio_le.text()))
            self.logo.write_logo_ushort(302, int(self.ui.cond_reg_le.text())) #  d2 aka cond regulation 2 is 320 and 322

    def _regulate_oxidation(self, state: bool):
        self.ui.oxidation_on_btn.setHidden(state)
        self.ui.oxidation_off_btn.setHidden(not state)
        self.ui.pump_chb.setEnabled(not state)
        self.oxyd_byte[2] = state
        self.oxyd_byte[4] = state
        if state:
            self.logo.write_logo_byte(360, dict_to_bytearray(self.oxyd_byte))
            self.logo.write_logo_ushort(362, int(self.ui.cond_reg_le.text()))

    def switch_pump(self):
        self.oxyd_byte[3] = self.ui.pump_chb.isChecked()
        print(dict_to_bytearray(self.oxyd_byte))
        self.logo.write_logo_byte(360, dict_to_bytearray(self.oxyd_byte))

    def _regulate_ph(self, state: bool):
        self.ui.ph_on_btn.setHidden(state)
        self.ui.ph_off_btn.setHidden(not state)
        self.ph_byte[1] = state
        self.ph_byte[2] = state
        self.ph_byte[4] = state
        if state:
            self.logo.write_logo_byte(340, dict_to_bytearray(self.ph_byte))
            self.logo.write_logo_ushort(342, int(self.ui.cond_reg_le.text()))

    def _switch_lights(self, state: bool):
        self.ui.lights_on_btn.setHidden(state)
        self.ui.lights_off_btn.setHidden(not state)
        self.logo.write_logo_byte(374, bytearray(b'\x01') if state else bytearray(b'\x00'))
        self.logo.write_logo_byte(2, bytearray(b'\x01'))

    def _save_lights(self):
        self.lights_thread = Thread(target=self._check_lights)
        self.lights_thread.start()
        self.lights_time = [datetime.strptime(self.ui.lights_on_le.text(), "%H:%M").time(),
                            datetime.strptime(self.ui.lights_off_le.text(), "%H:%M").time()]
        self.logo.write_logo_byte(374, bytearray(b'\x00'))
        self.logo.write_logo_byte(2, bytearray(b'\x01'))
        self.logo_2.write_logo_byte(440, time_to_hexa(self.ui.lights_on_le.text()))
        self.logo_2.write_logo_byte(442, time_to_hexa(self.ui.lights_off_le.text()))

    def _check_lights(self):
        while True:
            if self.lights_time[0] <= datetime.now().time() <= self.lights_time[1]:
                self._switch_lights(True)
            else:
                self._switch_lights(False)
            time.sleep(10)

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

    def _add_data_to_gui(self, data):
        self.environmental_data = data
        self.ui.wall_tep_lbl.setText(str(data[0]))
        self.ui.wall_hum_lbl.setText(str(data[1]))
        self.ui.wall_co2_lbl.setText(str(data[2]))

    def _add_data_to_gui_2(self, data):
        self.water_data = data
        self.ui.water_ph_lbl.setText(str(data[3]))
        self.ui.water_oxyd_lbl.setText(str(data[4]))
        self.ui.water_cond_lbl.setText(str(data[5]))
        self.ui.water_redox_lbl.setText(str(data[6]))
        self.ui.water_temp_lbl.setText(str(data[7]))

    def _update_cam_view(self, i: str, frame):
        self.ui.time_cam_lbl_1.setText(f"{datetime.now():%d.%m. %H:%M}")
        self.pictures[int(i)-1] = frame

        cam_display: QLabel= self.ui.widget_7.findChild(QLabel, f"cam_lbl_{i}")
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

    def _save_current_frame(self):
        name = "snímek obrazovky" + datetime.now().strftime("%Y-%m-%d_%H%M")

        if self.ui.cam_dir_le.text() != "":
            path = f"{self.ui.cam_dir_le.text()}/{name}"
        else:
            path = f"./{name}"

        cv2.imwrite(f"{path}_1.png", np.array(self.pictures[0]))
        cv2.imwrite(f"{path}_2.png", np.array(self.pictures[1]))

    def _save_watering_data(self):
        with open("./App_data/valve_settings.csv", 'w') as f:
            pass
        self.logo.write_logo_byte(400, self._data_to_bytearray(1, 17))
        self.logo_2.write_logo_byte(400, self._data_to_bytearray(17, 22))

    def _data_to_bytearray(self, start, end) -> bytearray:
        data_array = b''
        for i in range(start, end):
            start_time = self.ui.scrollArea.findChild(QLineEdit, f"water_start_le_{str(i)}").text()
            duration = self.ui.scrollArea.findChild(QLineEdit, f"water_dur_le_{str(i)}").text()
            pause = self.ui.scrollArea.findChild(QLineEdit, f"water_interval_le_{str(i)}").text()
            end_time = self.ui.scrollArea.findChild(QLineEdit, f"water_end_le_{str(i)}").text()
            data_array += time_to_hexa(start_time)
            data_array += ushort_to_hexa(duration)
            data_array += ushort_to_hexa(pause)
            data_array += time_to_hexa(end_time)
            with open("./App_data/valve_settings.csv", 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([f"v{i}", start_time, duration, pause, end_time])

        return bytearray(data_array)

    def _load_valve_settings(self):
        with open("./App_data/valve_settings.csv", 'r') as f:
            reader = list(csv.reader(f))
            le_names = ["water_start_le_", "water_dur_le_", "water_interval_le_", "water_end_le_"]
            for i in range(22):
                for name in range(4):
                    line: QLineEdit= self.ui.scrollArea.findChild(QLineEdit, le_names[name] + str(i+1))
                    line.setText(reader[i][name+1])

    def _set_dir_mame(self):
        self.dir_name = self.ui.dir_name_le.text()

    def _set_saving(self, state):
        self.saving = state
        self.ui.start_saving_btn.setHidden(state)
        self.save_file_path = self.ui.solution_dir_le.text()
        self.ui.dir_name_btn.setEnabled(not state)
        self.ui.stop_saving_btn.setHidden(not state)

    def environmental_data_update(self):
        self.line_chart_2.update_chart(self.environmental_data)
        if self.saving:
            self._save_data(self.environmental_data, "Okolí_pes_ste")

    def water_data_update(self):
        self.line_chart.update_chart(self.water_data)
        if self.saving:
            self._save_data(self.water_data, "parametry_vody")

    def _save_data(self, data: list, name: str):
        water_header = ["čas","pH","Okysličení", "Vodivost", "Redox", "Teplota"]
        environment_header = ["čas","Teplota", "Vlhkost", "CO2"]

        current_time = datetime.now().time()
        data.insert(0, current_time)

        self.write_csv_line(data, water_header if name == "parametry_vody" else environment_header, name)

    def write_csv_line(self, data, header, name):
        full_path = (f"{self.save_file_path if self.save_file_path != "" else "./"}"
                     f"/{name}_{self.dir_name}.csv")
        file_is_empty = not os.path.exists(full_path) or os.stat(full_path).st_size == 0

        with open(full_path, 'a', newline="") as f:
            writer = csv.writer(f)
            if file_is_empty:
                writer.writerow(header)
            writer.writerow(data)

    def _switch_led(self, led, color):
        led: QLabel = self.ui.scrollArea.findChild(QLabel, f"valve_state_lbl_{led}")
        led.setPixmap(QPixmap(f'./App_data/{color}_led_15.png'))

    def _switch_all_leds(self, color: str):
        led = f'./App_data/{color}_led_15.png'

        for i in range(1,8):
            valve_state: QLabel = self.ui.col_wg_1.findChild(QLabel, f"valve_state_lbl_{i}")
            valve_state.setPixmap(QPixmap(led))
        for i in range(8,15):
            valve_state: QLabel = self.ui.col_wg_2.findChild(QLabel, f"valve_state_lbl_{i}")
            valve_state.setPixmap(QPixmap(led))
        for i in range(15,22):
            valve_state: QLabel = self.ui.col_wg_3.findChild(QLabel, f"valve_state_lbl_{i}")
            valve_state.setPixmap(QPixmap(led))
