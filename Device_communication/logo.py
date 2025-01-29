import struct
import time

from PySide6.QtCore import QThread, Signal
from snap7.logo import Logo
from time import sleep


class LogoControl(QThread):
    LOGO_DATA = Signal(list)
    VFD_CON = Signal(bool)

    def __init__(self, ip :str="192.168.1.3"):
        super().__init__()
        self.ip = ip
        self.port = 512
        self.vfd = bytearray(b'\x05')
        self.connected = False
        self.drivers_connected = False
        self.vfd_connected = False
        self.sending = False
        self.lasers = [0, 0, 0]

    def run(self):
        self._connect_to_logo()

    def _connect_to_logo(self):
        while not self.connected:
            try:
                self.logo = Logo()
                self.logo.connect(self.ip, 768, self.port)
                self.connected = True
                self._get_logo_data()
                break
            except Exception as e:
                print(e)
                sleep(10)

    def _get_logo_data(self):
        while self.connected:
            if not self.sending:
                self.sending = True
                green_wall_data = self.logo.db_read(0, 250, 6)
                byte_water_data = self.logo.db_read(0, 20, 12)
                self.sending = False
                green_wall_data = struct.unpack(">HHH", green_wall_data)
                water_data = struct.unpack(">HHHHHH", byte_water_data)

                logo_data = [green_wall_data[i]/10 if i<2 else green_wall_data[i] for i in range(len(green_wall_data))]
                logo_data.append(round(1.4 * water_data[0] / 100, 1)) # Ph
                logo_data.append(2 * water_data[1] / 100) # Oxygen
                logo_data.append(2 * water_data[2]) # Conductivity
                logo_data.append(2 * water_data[3]-1000) # Radox potential
                logo_data.append(water_data[5] / 10) # temperature
                self.LOGO_DATA.emit(logo_data) # 0-2 green wall info (temp, hum, co2), 3-7 general info (ph, O2, cond, radox, temp)
                sleep(0.1)
            else:
                sleep(0.05)

    def write_logo_ushort(self, pos: int, request: int):
        while self.connected:
            try:
                if not self.sending:
                    ushort_in_bytes = struct.pack('>H', request)
                    self.sending = True
                    self.logo.db_write(0, pos, bytearray(ushort_in_bytes))
                    self.sending = False
                    break
                else:
                    sleep(0.05)
            except Exception as e:
                print(e)

    def read_logo_config(self):
        while self.connected:
            if not self.sending:
                msg = self.logo.db_read(0, 312, 4)
                msg += self.logo.db_read(0, 352, 4)
                return struct.unpack( ">HHHH", msg)
            else:
                print("sending")
                time.sleep(0.05)

    def write_logo_byte(self, pos :int, logo_bytes: bytearray):
        while self.connected:
            if not self.sending:
                self.sending = True
                self.logo.db_write(0, pos, logo_bytes)
                self.sending = False
                break
            else:
                sleep(0.05)

    def disconnect(self):
        try:
            self.connected = False
            self.logo.db_write(0, 10, bytearray(b'\x00\x00'))
            sleep(0.2)
            self.logo.disconnect()
            self.quit()
        except Exception as e:
            print(e)
