class Controller:
    
    def __init__(self, light_sensor):
        self.light_sensor = light_sensor
        self.automation = False
        self.light_on = False
        self.trigger_value = 15000
        self.residents_present = True
        
    def toggle_automation(self):
        self.automation = True
        
    def toggle_light(self):
        self.automation = False
        self.light_on = not self.light_on
        
    def set_trigger_level(self, level):
        self.trigger_value = level
        
    def set_residents_present(self, present):
        self.trigger_value = present
    
    