import re

class ProtocolMachine:
    def __init__(self, controller, lightsensor):
        self.controller = controller
        self.lightsensor = lightsensor
    
    def process_input(self, line, cl):
        if line == 'toggle':
            self.controller.toggle_light()
        elif line == 'automation':
            self.controller.enable_automation()
            cl.send(self.lightsensor.get_data_string() + '\n')
        elif re.match('^level', line):
            self.controller.set_trigger_level(line.split()[1])
        elif re.match('^startTime', line):
            self.controller.set_start_time(line.split()[1])
        elif re.match('^endTime', line):
            self.controller.set_end_time(line.split()[1])
        elif line == 'getData':
            cl.send(self.lightsensor.get_data_string() + '\n')