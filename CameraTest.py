from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import MotionSensor
import pygame
#imports all necessary libraries

camera = PiCamera()
pir = MotionSensor(4)
pygame.mixer.init()
sound = pygame.mixer.Sound('/home/pi/414208__jacksonacademyashmore__airhorn.wav')
# establishes camera and motion sensor DIO output

while True:
    for i in range(50):
        pir.wait_for_motion()
        #records up to 50 10 second videos
        camera.start_preview()
        camera.start_recording('/home/pi/Desktop/Videos/' + str(i) + '_video_.h264')
        # begins a new recording
        sleep(5)
        sound.play()
        sleep(5)
        camera.stop_recording()
        camera.stop_preview()
        pir.wait_for_no_motion()
        #waits for motion to end
