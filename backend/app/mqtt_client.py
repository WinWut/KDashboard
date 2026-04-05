import json
import paho.mqtt.client as mqtt
from app.state import data

broker_ip="broker.hivemq.com"
port=1883

def on_connect(client,userdata,flags,rc):
    print("Connected to MQTT")
    client.subscribe("iot/data")

def on_message(client,userdata,msg):
    print("Raw:",msg.payload)

    payload = json.loads(msg.payload.decode())
    print("Parsed:",payload)
    data["ec"] = payload.get("ec",0)
    data["ph"]= payload.get("ph",0)
    data["humidity"] = payload.get("humidity",0)
    data["airtemp"] = payload.get("airtemp",0)
    data["watertemp"] = payload.get("watertemp",0)

    print("DATA:",data)

def start_mqtt():
    client = mqtt.Client()
    client.on_connect=on_connect
    client.on_message=on_message
    
    client.connect(broker_ip,port,60)
    client.loop_start()