import struct

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
                sleep(5)

    def _get_logo_data(self):
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

    def write_logo_ushort(self, pos: int, request: int):
        while self.connected:
            if not self.sending:
                ushort_in_bytes = struct.pack('>H', request)
                self.sending = True
                self.logo.db_write(0, pos, bytearray(ushort_in_bytes))
                self.sending = False
                break
            else:
                sleep(0.05)

    def write_logo_byte(self, pos :int, logo_bytes: bytearray):
        while self.connected:
            if not self.sending:
                self.sending = True
                print(f"{pos}, {logo_bytes}")
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
