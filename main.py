from networking import Networking
from light_sensor import LightSensor
from controller import Controller


print("Starting Lightmodule...")
lightsensor = LightSensor()
print("Lightmodule started")

print("Starting Controller...")
controller = Controller(lightsensor)
print("Controller started")

print("Starting Server...")
networking = Networking(lightsensor)
print("Networking started")
