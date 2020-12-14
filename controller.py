from machine import Pin

class Controller:
    
    def __init__(self):
        self.automation = False
        self.trigger_value = 1000
        self.residents_present = True
        self.sun = Pin(2,Pin.OUT)
        self.sun.value(False)
        self.start_time = '8:00'
        self.end_time = '22:00'
        
    def enable_automation(self):
        self.automation = True
        
    def toggle_light(self):
        self.automation = False
        self.sun.value(not self.sun.value())
        
    def set_trigger_level(self, level):
        self.trigger_value = int(level)
        
    def set_residents_present(self, present):
        self.residents_present = present
        
    def notify_light_level(self, level):
        if self.automation:
            if level <= self.trigger_value:
                self.sun.value(True)
            else:
                self.sun.value(False)
                
    def set_start_time(self, time):
        self.start_time = time
        
    def set_end_time(self, time):
        self.end_time = time
        
    def check_time(self, time):
        print(time)
                
            