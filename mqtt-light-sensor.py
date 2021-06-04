import paho.mqtt.client as mqtt
import time,threading
import multiprocessing as mp
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_USERNAME ="CSE_BBC1"
ADAFRUIT_IO_KEY = "aio_wXPC09rE51bD1CFHcZnaBmTzeFiW"

FEED_ID = 'bk-iot-light'

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))


# def on_message(client,userdata,message):
#     print("Received message: " + str(message.payload.decode("utf-8")))
def connected(client):
    client.subscribe(FEED_ID)


client = MQTTClient(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
# client.on_connect = on_connect
client.on_connect    = connected
client.on_message    = message

client.connect()

# client.loop_start()

client.loop_blocking()
