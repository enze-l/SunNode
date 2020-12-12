from networking import Networking
from light_sensor import LightSensor
from controller import Controller

print("Starting Controller...")
controller = Controller()
print("Controller started")

print("Starting Lightmodule...")
lightsensor = LightSensor(controller)
print("Lightmodule started")

print("Starting Server...")
networking = Networking(controller, lightsensor)
print("Networking started")
