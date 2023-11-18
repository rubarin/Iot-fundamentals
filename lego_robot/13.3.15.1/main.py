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



#MQTT setup
MQTT_ClientID = 'testmqtt'
MQTT_Broker = '172.20.10.4'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

#cqllbqck
def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))
        robotName = 'B' #here you can change the name of the robot
        arrayNote = str(msg.decode()).split(',')
        if(arrayNote[0] == robotName):
            ev3.light.on(Color.RED)
            tailleNote = arrayNote[1]
            noteAjouer = robotName + '4/' + tailleNote
            ev3.speaker.play_notes([noteAjouer])
            resulting_string = ','.join(arrayNote[2:])
            client.publish(MQTT_Topic_Status, resulting_string)
        else:
            ev3.light.on(Color.GREEN)


# Write your program here.


# Write your program here.
client.connect() 
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)
ev3.speaker.beep()

while True:
    client.check_msg()



