import time
import paho.mqtt.client as paho
broker="192.168.0.13"
broker="192.168.0.13"
publicMessage = None
#define callback
def on_message(client, userdata, message):
    global publicMessage
    publicMessage = message.payload.decode("utf-8")

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing")
if publicMessage is None:
  print("waiting for response. CAN BE LONG PLEASE WAIT...")
while(publicMessage is None):
  client.subscribe("messageClient")
#subscribe
print(publicMessage)
client.disconnect() #disconnect
client.loop_stop()#stop loop
