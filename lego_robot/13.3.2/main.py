#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from umqtt.robust import MQTTClient
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot=DriveBase(left_motor,right_motor,wheel_diameter=54,axle_track=105)

MQTT_ClientID='a'
MQTT_Broker='192.168.53.51'
MQTT_Topic_Status='Lego/Status'
client=MQTTClient(MQTT_ClientID,MQTT_Broker,1883)

def listen(topic,msg):
    if topic==MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))

UltraSensor=UltrasonicSensor(Port.S4)

while UltraSensor.distance() > 100:
    robot.drive(100, 0)
robot.stop()

client.connect()
time.sleep(0.5)
client.publish(MQTT_Topic_Status,'Drive forward!')
ev3.screen.print('Started')



while True:
    client.check_msg()
    time.sleep(0.5)
          






    


    
