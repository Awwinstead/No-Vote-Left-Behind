import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()
for i in range(15):
    try:
            
            id, text = reader.read()
            print(id)
            print(text)
    except:
            print("Oof")
    sleep(1)
GPIO.cleanup()