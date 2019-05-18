from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=14, trigger=15)

while True:
    print(sensor.distance * 100)
    sleep(1)
