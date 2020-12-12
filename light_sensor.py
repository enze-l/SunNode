from machine import Pin, I2C
from bh1750 import BH1750
from time import sleep
import _thread

class LightSensor:
    def __init__(self, controller):
        self.sensor = BH1750(I2C(scl=Pin(22), sda=Pin(21)))
        self.list = []
        self.listen()
        self.controller = controller
        
    def listen(self):
        _thread.start_new_thread(self.report_level, ())

    def report_level(self):
        while True:
            level = self.sensor.luminance(BH1750.ONCE_HIRES_1)
            self.controller.notify_light_level(level)
            self.list.append(level)
            if len(self.list) > 25:
                self.list.pop(0)
            sleep(1)
            
    def get_data(self):
        return self.list
    
    def get_data_string(self):
        return ' '.join(map(str, self.list))