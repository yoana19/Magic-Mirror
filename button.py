from gpiozero import Button
from time import sleep

button=Button(3)

while True:
    button.wait_for_press()
    print("The button was pressed!")
    sleep(1)
