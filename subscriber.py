import paho.mqtt.client as mqtt
from datetime import datetime
def get_now_datetime():
    return datetime.now().strftime("%a %I:%M %p")

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    username = userdata["username"]
    datenow = get_now_datetime()
    print(f"{username}:  " + msg.payload.decode("utf-8") +f"\n{datenow}\n")

# The callback for when we disconnect with the server.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("{your_username}", "{your_password}")
# send your username to keep track of who sends the message
client.user_data_set({"username":"Santhosh"})

# connect to HiveMQ Cloud on port 8883
client.connect("{your_uri}", 8883)

# subscribe to the a topic
client.subscribe("my/gf-1/{someones_name}")
client.subscribe("my/family/{someones_name}")

# send some text to test the application
# client.publish("my/text/message", "Hello")

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()