from machine import Pin

class Controller:
    
    def __init__(self):
        self.automation = False
        self.trigger_value = 1000
        self.last_value = 0
        self.sun = Pin(2,Pin.OUT)
        self.sun.value(False)
        self.start_time = '8:00'
        self.end_time = '22:00'
        self.last_time = None
        self.working_time = False
        
    def enable_automation(self):
        self.automation = True
        self.notify_light_level(self.last_value)
        
    def toggle_light(self):
        self.automation = False
        self.sun.value(not self.sun.value())
        
    def set_trigger_level(self, level):
        self.trigger_value = int(level)
        self.notify_light_level(self.last_value)
        
    def notify_light_level(self, level):
        self.last_value = level
        if self.automation:
            if self.working_time and level <= self.trigger_value:
                self.sun.value(True)
            else:
                self.sun.value(False)
                
    def set_start_time(self, time):
        self.start_time = time
        self.trigger_time_change()        
        
    def set_end_time(self, time):
        self.end_time = time
        self.trigger_time_change()
        
    def trigger_time_change(self):
        self.check_time(self.last_time)
        self.notify_light_level(self.last_value)
        
    def check_time(self, time):
        self.last_time = time;
        current = int(time.replace(':', ''))
        start = int(self.start_time.replace(':', ''))
        end = int(self.end_time.replace(':', ''))
        if start <= current and current < end:
            self.working_time = True
        else:
            self.working_time = False
            