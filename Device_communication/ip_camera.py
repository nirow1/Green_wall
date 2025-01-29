import time
from asyncio import timeout
from turtledemo.penrose import start

import numpy as np
import cv2

from PySide6.QtCore import QThread
from PySide6.QtCore import Signal
from threading import Thread
from time import sleep


class Camera(QThread):
    NEW_IMAGE = Signal(object)
    def __init__(self, ip: str, interval = 30):
        super().__init__()
        self.ip = ip
        self.screenshot_interval = interval
        self.status: bool= False
        self.frame= None
        self.capture: cv2.VideoCapture | None = None
        self.connected = False

        self.thread = Thread(target=self.grab_image)

    def run(self):
        while not self.connected:

            self.capture = cv2.VideoCapture(f"rtsp://admin:4Jtech.pristup@{self.ip}/1")
            self.connected = self.capture.isOpened()
            if self.connected:
                self.thread.start()
                self._update_image()
                break

            sleep(600)

    def _update_image(self):
        while self.connected:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def grab_image(self):
        while self.connected:
            sleep(self.screenshot_interval)
            if self.status:
                self.NEW_IMAGE.emit(self.frame)

    def disconnect(self):
        self.connected = False
        self.capture.release()