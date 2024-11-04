import paho.mqtt.client as mqtt
import time

# Define MQTT broker details
broker = 'localhost'
port = 1883
topic = 'test/topic'
client_id = 'publisher'

# Create MQTT client and connect to the broker
client = mqtt.Client(client_id)
client.connect(broker, port)

# Publish messages asynchronously
for i in range(1000000):
    message = f"Message {i}"
    client.publish(topic, message)
    if i % 10000 == 0:  # Log every 10,000 messages
        print(f"Published {i} messages")
   # time.sleep(0.001)  # A short delay to avoid overwhelming the broker
client.disconnect()
