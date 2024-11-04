import paho.mqtt.client as mqtt

broker = 'localhost'
port = 1883
topic = 'test/topic'
client_id = 'subscriber'
message_count = 0

def on_message(client, userdata, message):
    global message_count
    message_count += 1
    if message_count % 10000 == 0:
        print(f"Received {message_count} messages")

client = mqtt.Client(client_id)
client.connect(broker, port)
client.subscribe(topic)
client.on_message = on_message

client.loop_forever()
