import struct

from PySide6.QtCore import QThread, Signal
from snap7.logo import Logo
from time import sleep


class LogoControl(QThread):
    LOGO_DATA = Signal(list)
    VFD_CON = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ip = "192.168.1.3"
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
                self._get_current_velocity()
                break
            except Exception as e:
                print(e)
                sleep(5)

    def _get_current_velocity(self):
        while self.connected:
            if not self.sending:
                self.sending = True
                logo_data = self.logo.db_read(0, 14, 4)
                logo_data = struct.unpack(">I", logo_data)
                self.sending = False
                self.LOGO_DATA.emit(logo_data)
                sleep(0.1)
            else:
                sleep(0.05)

    def write_requested_velocity(self, velocity: int):
        while self.connected:
            if not self.sending:
                velocity_in_bytes = struct.pack('>H', velocity)
                self.sending = True
                success = self.logo.db_write(0, 12, bytearray(velocity_in_bytes))
                print(f"sending velocity: {velocity}, in bytes: {velocity_in_bytes}, result: {success} ")
                self.sending = False
                break
            else:
                sleep(0.05)

    def switch_lasers(self, laser_pos):
        if self.lasers[laser_pos] == 0:
            if laser_pos == 0:
                self.lasers[laser_pos] = 1
                on_off = True
            elif laser_pos == 1:
                on_off = True
                self.lasers[laser_pos] = 2
            else:
                on_off = True
                self.lasers[laser_pos] = 4
        else:
            on_off = False
            self.lasers[laser_pos] = 0

        self._set_lasers()
        return on_off

    def _set_lasers(self):
        byte_lasers = bytearray(sum(self.lasers).to_bytes(1))
        while self.connected:
            if not self.sending:
                self.sending = True
                self.logo.db_write(0, 2, byte_lasers)
                self.sending = False
                break
            else:
                sleep(0.05)

    def connect_to_vfd(self):
        while self.connected:
            if not self.sending:
                self.sending = True
                if not self.vfd_connected:
                    self.logo.db_write(0, 10, bytearray(b'\x00\x01'))
                else:
                    self.logo.db_write(0, 10, bytearray(b'\x00\x00'))
                self.sending = False
                self.vfd_connected = not self.vfd_connected
                break
            else:
                sleep(0.05)

    def connect_to_drivers(self):
        while self.connected:
            if not self.sending:
                self.sending = True
                if not self.drivers_connected:
                    self.logo.db_write(0, 34, bytearray(b'\x07'))
                else:
                    self.logo.db_write(0, 34, bytearray(b'\x00'))
                self.sending = False
                self.drivers_connected = not self.drivers_connected
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
