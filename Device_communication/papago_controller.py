from time import sleep
from PySide6.QtCore import QThread, Signal
from Utils.static_methods import combine_to_float
from pymodbus.client import ModbusTcpClient as ModbusClient

class PapagoController(QThread):
    PAPAGO_DATA = Signal(list)

    def __init__(self):
        super().__init__()
        self.ip = "192.168.0.253"
        self.port = 502
        self.client: ModbusClient | None = None
        self.connected: bool= False

    def run(self):
        self._connect_to_drivers()

    def _connect_to_drivers(self):
        while not self.connected:
            try:
                self.client = ModbusClient(self.ip, port=self.port)
                self.connected = self.client.connect()
                if self.connected:
                    self._read_papago_data()
                else:
                    sleep(5)
            except Exception as e:
                print(e)
                print("papago reading data error")

    def _read_papago_data(self):
        while self.connected:
            temp = self.client.read_input_registers(12, count=2, slave=1)
            hum = self.client.read_input_registers(22, count=2, slave=1)
            co2 = self.client.read_input_registers(102, count=2, slave=1)
            if not temp.isError() and not hum.isError():
                temp_float = round(combine_to_float(temp.registers), 1)
                hum_float = round(combine_to_float(hum.registers), 1)
                co2_float = round(combine_to_float(co2.registers), 1)
                self.PAPAGO_DATA.emit([temp_float, hum_float, co2_float])

if __name__ == '__main__':
    papago = PapagoController()
    papago.run()