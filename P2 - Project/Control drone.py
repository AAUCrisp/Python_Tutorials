import pygame, threading, socket, sys, platform, time
from pygame.locals import * 
from djitellopy import Tello

# Start pygame
pygame.init()

done = False



# Initialize the joysticks.
pygame.joystick.init()

host = ''
port = 9000
locaddr = (host,port) 

tello = Tello()
tello.connect()
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)


def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

recvThread = threading.Thread(target=recv)
recvThread.start()



# -------- Main Program Loop -----------
while not done:

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            tello.send_rc_control(0,0,0,0)
            if event.button == 0:
                print("Button A has been pressed")
            if event.button == 1:
                print("Button B has been pressed")
            if event.button == 2:
                print("Button x has been pressed")
            if event.button == 3:
                print("Button y has been pressed")
                done = True
                tello.send_rc_control(0,0,0,0)
                tello.land()
                quit()
            if event.button == 7:
                print("start has been pressed")
                tello.takeoff()
            if event.button == 6:
                tello.send_rc_control(0,0,0,0)
                tello.land()
                print("select has been pressed")
        if event.type == JOYAXISMOTION:
            if (joystick.get_axis(0) > 0.5):
                print("left thumbstick is moving right")
                print(" ")
                tello.send_rc_control(10,0,0,0)
            if (joystick.get_axis(0) < -0.5):
                print("left thumbstick is moving left")  
                print(" ")
                tello.send_rc_control(-10,0,0,0)
            if (joystick.get_axis(1) > 0.5):
                print("left thumbstick is moving down")
                print(" ")
                tello.send_rc_control(0,10,0,0)
            if (joystick.get_axis(1) < -0.5):
                print("left thumbstik is moving up")
                print(" ")
                tello.send_rc_control(0,-10,0,0)
            if (joystick.get_axis(3) > 0.5):
                print("right thumbstick is moving right")
                print(" ")
                tello.send_rc_control(0,0,0,10)
            if (joystick.get_axis(3) < -0.5):
                print("Right thumbstick is moving left")
                print(" ")
                tello.send_rc_control(0,0,0,-10)
            if (joystick.get_axis(4) > 0.5):
                print("right thumbstick is moving down")
                print(" ")
            if (joystick.get_axis(4) < -0.5):
                print("right thumbstick is moving up")
                print(" ")
            if (joystick.get_axis(5) > 0.2):
                print("Right Bumper")
                print(" ")
                tello.send_rc_control(0,0,-10,0)
            if (joystick.get_axis(2) > 0.2):
                print("Left Bumper")
                print(" ")
                tello.send_rc_control(0,0,10,0)
        if event.type == JOYHATMOTION:
            if joystick.get_hat(0)==(0,0):
                tello.send_rc_control(0,0,0,0)
            if joystick.get_hat(0)==(-1,0):
                tello.send_rc_control(-10,0,0,0)
            if joystick.get_hat(0)==(1,0):
                tello.send_rc_control(10,0,0,0)
            if joystick.get_hat(0)==(0,-1):
                tello.send_rc_control(0,10,0,0)
            if joystick.get_hat(0)==(0,1):
                tello.send_rc_control(0,-10,0,0)

