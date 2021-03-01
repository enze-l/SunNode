from time import sleep
import utime
import ntptime
import _thread

class Scheduler:
    def __init__(self, controller, light_sensor):
        self.controller = controller
        self.light_sensor = light_sensor
        _thread.start_new_thread(self.time_event, ())
            
    def time_event(self):
        while True:
            time = None
            if utime.localtime()[4] < 10:
                time = str(utime.localtime()[3]) + ':0' + str(utime.localtime()[4])
            else:
                time = str(utime.localtime()[3]) + ':' + str(utime.localtime()[4])
            if utime.localtime()[4] % 15 == 0 and utime.localtime()[5] == 0:
                level = self.light_sensor.get_level()
                self.controller.notify_light_level(level)
            self.controller.check_time(time)
            sleep(1)