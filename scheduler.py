from time import sleep
import utime
import ntptime
import _thread

class Scheduler:
    def __init__(self, controller):
        self.controller = controller
        _thread.start_new_thread(self.time_event, ())
            
    def time_event(self):
        while True:
            self.controller.check_time(utime.localtime())
            sleep(1)