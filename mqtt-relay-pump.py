import paho.mqtt.client as mqtt
import time
import multiprocessing as mp
from Adafruit_IO import MQTTClient
import random
import json

ADAFRUIT_IO_USERNAME = "CSE_BBC1"
#"CSE_BBC1"      
#ankkubmt6"
ADAFRUIT_IO_KEY =    "aio_wXPC09rE51bD1CFHcZnaBmTzeFiW"
#"aio_wXPC09rE51bD1CFHcZnaBmTzeFiW" 
#aio_Pmws60DyhUCa26BjFbcj3YaWbLS2"


# Shared IO Feed
# Make sure you have read AND write access to this feed to publish.
IO_FEED = "bk-iot-relay"
# "bk-iot-relay"
#'test'

# IO Feed Owner's username

# Define callback functions which will be called when certain events happen.
def connected(client):
    """Connected function will be called when the client connects.
    """
    client.subscribe(IO_FEED)

def message(client, feed_id, payload):
    """Message function will be called when a subscribed feed has a new value.
    The feed_id parameter identifies the feed, and the payload parameter has
    the new value.
    """
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    

client = MQTTClient(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
# client.on_connect = on_connect
client.on_connect    = connected
client.on_message    = message

client.connect()


client.loop_background()


print('Publishing a new message every 5 seconds (press Ctrl-C to quit)...')
while True:
    value = random.randint(0, 1)
    data = {"id":"11","name":"RELAY","data":value,"unit":""}
    print('Publishing {0} to {1}.'.format(data, IO_FEED))
    client.publish(IO_FEED,json.dumps(data))
    time.sleep(5)
