import json
import paho.mqtt.client as mqtt
from app.state import data

def on_connect(client,userdata,flags,rc):
    print("Connected to MQTT")
    client.subscribe("iot/data")

def on_message(client,userdata,msg):
    print("Raw:",msg.payload)

    payload = json.loads(msg.payload.decode())
    print("Parsed:",payload)
    data["ec"] = payload.get("ec",0)
    data["ph"]= payload.get("ph",0)
    data["relay"] = payload.get("relay","OFF")

    print("DATA:",data)

def start_mqtt():
    client = mqtt.Client()
    client.on_connect=on_connect
    client.on_message=on_message

    client.connect("broker.hivemq.com",1883,60)
    client.loop_start()