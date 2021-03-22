import paho.mqtt.client as mqtt
from time import sleep
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
client.username_pw_set("{your_username}", "{your_password}")

# connect to HiveMQ Cloud on port 8883
client.connect("{your_uri}", 8883)

# publish your message
counter = 100
#send 100 messages with 2 seconds interval
while counter > 0:

    client.publish("my/gf-1/name", f"Hello Hello!!! gorgeous {counter}")
    sleep(2)
    client.publish("my/gf-2/name", f"Hey Darls {counter}")
    sleep(2)
    counter -= 1