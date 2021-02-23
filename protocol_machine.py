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
        elif re.match('^level', line):
            self.controller.set_trigger_level(line.split()[1])
        elif re.match('^startTime', line):
            self.controller.set_start_time(line.split()[1])
        elif re.match('^endTime', line):
            self.controller.set_end_time(line.split()[1])
        elif line == 'getData':
            list = []
            list.append(str(self.lightsensor.max_level))
            list.append(str(self.controller.trigger_value))
            list.append(str(self.controller.start_time))
            list.append(str(self.controller.end_time))
            list.append(self.lightsensor.get_data_array() + '\n')
            data = ' '.join(map(str, list))
            print(data)
            cl.send(data)