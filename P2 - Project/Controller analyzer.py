import pygame
from pygame.locals import *
import time


# Start pygame
pygame.init()

done = False

# Initialize the joysticks.
pygame.joystick.init()


# -------- Main Program Loop -----------
while not done:

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            if event.button == 0:
                print("Button A has been pressed")
            if event.button == 1:
                print("Button B has been pressed")
            if event.button == 2:
                print("Button x has been pressed")
            if event.button == 3:
                print("Button y has been pressed")
                done = True
                quit()
            if event.button == 6:
                print("start has been pressed")
                
            if event.button == 7:
                print("select has been pressed")
        if event.type == JOYAXISMOTION:
            if (joystick.get_axis(0) > 0.5) or (joystick.get_axis(0) < -0.5):
                print("left thumbstock is moving left and right")
                print(" ")
            if (joystick.get_axis(1) > 0.5) or (joystick.get_axis(1) < -0.5):
                print("left thumbstick is moving up and down")
                print(" ")
            if (joystick.get_axis(2) > 0):
                print("Left Bumper")
                print(" ")
            if (joystick.get_axis(3) > 0.5) or (joystick.get_axis(3) < -0.5):
                print("right thumbstick is moving left and right")
                print(" ")
            if (joystick.get_axis(4) > 0.5) or (joystick.get_axis(4) < -0.5):
                print("right thumbstick is moving up and down")
                print(" ")
            if (joystick.get_axis(5) > 0):
                print("Right Bumper")
                print(" ")


