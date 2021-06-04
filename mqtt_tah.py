import paho.mqtt.client as mqtt
import time,threading
import multiprocessing as mp
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_USERNAME ="CSE_BBC"
ADAFRUIT_IO_KEY = "aio_aaXQ56Mtv3RWWwps1wWDPCWdq8S6"

FEED_ID = 'bk-iot-temp-humid'

def message(client, feed_id, payload):

    print('Feed {0} received new value: {1}'.format(feed_id, payload))


def connected(client):
    client.subscribe(FEED_ID)


client = MQTTClient(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
# client.on_connect = on_connect
client.on_connect    = connected
client.on_message    = message

client.connect()


client.loop_blocking()

