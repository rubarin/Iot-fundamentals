#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot=DriveBase(left_motor,right_motor,wheel_diameter=54,axle_track=105)
TSensor=TouchSensor(Port.S2)
time_end = time.time() + 5
count = 0 

while time.time() < time_end:
    if TSensor.pressed():
        count+=1
        time.sleep(0.25)


ev3.screen.print(count)
for i in range(count):
    ev3.speaker.beep()
    time.sleep(1)
    
