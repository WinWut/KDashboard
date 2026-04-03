from fastapi import FastAPI
from app.state import data
from app.mqtt_client import start_mqtt
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
start_mqtt()

@app.get("/")
def root():
    return {"status":"running"}

@app.get("/data")
def get_data():
    return data