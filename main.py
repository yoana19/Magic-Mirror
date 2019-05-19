import requests, os, sys
from picamera import PiCamera
from time import sleep
import pygame
from gpiozero import Button

button=Button(3)

pygame.init()

shirt = pygame.mixer.Sound('shirt2.wav')
shoes = pygame.mixer.Sound('shoes2.wav')
luggage = pygame.mixer.Sound('luggageandbags2.wav')
dress = pygame.mixer.Sound('dress2.wav')
t_shirt = pygame.mixer.Sound('tshirt2.wav')
skirt = pygame.mixer.Sound('skirt2.wav')
coat = pygame.mixer.Sound('coat2.wav')
jeans = pygame.mixer.Sound('jeans2.wav')
beep = pygame.mixer.Sound('beep-01a.wav')


camera = PiCamera()

while True:
    
    model_id = '91b79f93-6365-4d62-b023-da62d5d1b6b9'
    api_key = '5ruwcBCMTfRRzb2666dUTvVVucSXr1ej'
    image_path = '/home/pi/Desktop/MagicMirror/currentimage.jpg'

    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/LabelFile/'

    data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}


    button.wait_for_press()
    print("The button was pressed!")
    sleep(5)
    camera.resolution = (3280,2464)
    camera.capture("/home/pi/Desktop/MagicMirror/currentimage.jpg")
    beep.play()

    response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

    response_text = response.text
    #print(response_text)

    #Coat Footwear Luggage Shoes Skirt T-Shirt Dress Jeans Shirt

    type_index = response_text.find("label") + 8
    clothing = response_text[type_index:type_index+3]

    if (clothing == "Shi"):
        shirt.play()
        print("9")
    elif (clothing == "Foo"):
        shoes.play()
        print("8")
    elif (clothing == "Lug"):
        luggage.play()
        print("7")
    elif (clothing == "Sho"):
        shoes.play()
        print("6")
    elif (clothing == "Ski"):
        skirt.play()
        print("5")
    elif (clothing == "T-S"):
        t_shirt.play()
        print("4")
    elif (clothing == "Dre"):
        dress.play()
        print("3")
    elif (clothing == "Jea"):
        jeans.play()
        print("1")
    elif (clothing == "Coa"):
        coat.play()
        print("2")
    else: print("error")

    sleep(5)
