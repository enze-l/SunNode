from time import sleep
import utime
import ntptime
import _thread

class Scheduler:
    def __init__(self, controller, networking):
        self.networking = networking
        self.controller = controller
            
