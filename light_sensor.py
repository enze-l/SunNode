from machine import Pin, SoftI2C
from bh1750 import BH1750
from time import sleep
import utime
import _thread

class LightSensor:
    
    def __init__(self):
        self.sensor = BH1750(SoftI2C(scl=Pin(22), sda=Pin(21)))
        self.max_level = 500
        self.last_day_list = None
        self.list = []
        self.last_measurement_time = 0
        self.get_level()

    def get_level(self):
        level = int(self.sensor.luminance(BH1750.ONCE_HIRES_1))
        print(level)
        self.list.append(level)
        if self.is_new_day():
            self.last_day_list = self.list
            self.list = []
        if level > self.max_level:
            self.max_level = level
        return level
            
    def is_new_day(self):
        time = utime.localtime()[3]
        if self.last_measurement_time > time:
            self.last_measurement_time = time
            print('New Day!')
            return True
        else:
            self.last_measurement_time = time
            return False
    
    def get_data(self):
        return self.list
    
    def get_data_array(self):
        if self.last_day_list != None:
            return ' '.join(map(str, self.last_day_list))
        return ' '.join(map(str, self.list))
    
    def get_max_level(self):
        return self.max_level
