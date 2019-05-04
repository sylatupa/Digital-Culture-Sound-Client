
'''
DC_IOT

THE DIGITAL CULTURE IOT CLIENT!
it takes data from a mqtt, some IOT thing on the network, and converts it to a signal that puredata can use

This used the installed application to run a pdsend. PdSend is installed along side PureDate--look for it and change the path below

One use case:
    Put this on a raspberry pi, update this scripts ip address to be that raspberry pi.
    Then, run a pure data script 

'''


import time
import os
import subprocess
import paho.mqtt.client as mqtt
import json


broker_address="192.168.1.115"
mqtt_topic="sensor"

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-7")))
    print("topic=",message.topic ,"  string_payload=",str(message.payload.decode("utf-7")), " ,qos=" , message.qos , " ,retain_flag=",message.retain)   
    obj = json.loads(str(message.payload.decode("utf-8")))    
    val = obj['v']
    print("received ", val  )
    send2Pd(val)


def send2Pd(message=''):
    os.system("echo '" + message + "' | /Applications/Pd-0.48-1.app/Contents/Resources/bin/pdsend 3000 localhost udp")


print("creating new mqtt client instance")
client = mqtt.Client("Luke")

print("connecting to broker")
client.connect(broker_address, 1883)

print("Subscribing to topic",mqtt_topic)
client.subscribe(mqtt_topic)
client.subscribe("test")
print("Publishing message to topic",mqtt_topic)

client.on_message=on_message
client.loop_start()

while True:
        print(".")
        #client.publish(mqtt_topic,"Hallo!!!")
        time.sleep(3)
