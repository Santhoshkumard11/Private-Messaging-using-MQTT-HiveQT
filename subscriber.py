import paho.mqtt.client as mqtt
from datetime import datetime
from dotenv import dotenv_values
config = dotenv_values(".env")  # load environment variables


class Subscriber:
    def __init__(self) -> None:
        pass

    def get_now_datetime(self):
        """Get the time to pretty print the time"""
        return datetime.now().strftime("%a %I:%M %p")
    
    def on_connect(self, client, userdata, flags, rc):
        """The callback for when the client receives a CONNACK response from the server."""
        print(("Connected successfully") if not rc else 
            ("Connect returned result code: " + str(rc)))
    
    def on_message(self, client, userdata, msg):
        """The callback for when a PUBLISH message is received from the server."""
        username = userdata["username"]
        datenow = self.get_now_datetime()
        print(f"{username}:  " + msg.payload.decode("utf-8") +f"\n{datenow}\n")

    def on_disconnect(client, userdata, rc):
        """The callback for when we disconnect with the server."""
        if rc:
            print("Unexpected disconnection.")

# Create the client and Subscriber
client, subscriber = mqtt.Client(), Subscriber()
client.on_connect = subscriber.on_connect
client.on_message = subscriber.on_message
client.on_disconnect = subscriber.on_disconnect


# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set(f'{config["username"]}', f'{config["password"]}')
# send your username to keep track of who sends the message
client.user_data_set({"username":config["username"]})

# connect to HiveMQ Cloud on port 8883
client.connect("{your_uri}", 8883)

# subscribe to the a topic
client.subscribe("my/gf-1/{someones_name}")
client.subscribe("my/family/{someones_name}")

# send some text to test the application
# client.publish("my/text/message", "Hello")

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()
