from networking import Networking
from light_sensor import LightSensor
from controller import Controller
from protocol_machine import ProtocolMachine

print("Starting Controller...")
controller = Controller()
print("Controller started")

print("Starting Lightmodule...")
lightsensor = LightSensor(controller)
print("Lightmodule started")

print("Creating ProtocolMachine...")
protocol_machine = ProtocolMachine(controller, lightsensor)
print("ProtocolMachine created")

print("Starting Server...")
networking = Networking(protocol_machine)
print("Networking started")
