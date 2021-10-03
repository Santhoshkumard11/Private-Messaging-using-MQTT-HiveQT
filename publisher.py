import paho.mqtt.client as mqtt
from time import sleep
import sys
from dotenv import dotenv_values
config = dotenv_values(".env")      # load environment variables

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when we disconnect with the server.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
        
# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set(f'{config["username"]}', f'{config["password"]}')

# connect to HiveMQ Cloud on port 8883
client.connect("{your_uri}", 8883)

# publish your message
counter = 100

#send 100 messages with 2 seconds interval
while counter > 0:
    # sending 100 message in 2 sec interval
    client.publish("my/gf-1/{your_friends_name}", f"Hello Hello!!! gorgeous {counter}")
    sleep(2)
    client.publish("my/family/{family_member_name}", f"Hey Mom {counter}")
    sleep(2)
    counter -= 1
