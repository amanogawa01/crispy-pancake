import json
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected to Mosquitto broker with result code {rc}")
    client.subscribe("frigate/#")


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"[{msg.topic}] Event: {payload}")
    except json.JSONDecodeError:
        print(f"[{msg.topic}] Raw message: {msg.payload.decode()}")


# Initialize with Callback API Version 2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to Mosquitto broker on localhost:1883...")
client.connect("127.0.0.1", 1883, 60)
client.loop_forever()