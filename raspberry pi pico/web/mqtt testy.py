import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Fluffynet","terrycarter")
time.sleep(5)
print(wlan.isconnected())

sensor = Pin(16, Pin.IN)

mqtt_server = 'mqtt-dashboard.com'
client_id = 'bigles'
topic_pub = b'TomsHardware'
topic_msg = b'Movement Detected'

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
while True:
    print(sensor.value())
    if sensor.value() == 0:
        client.publish(topic_pub, topic_msg)
        time.sleep(3)
    else:
        pass
    
    
    time.sleep(1)