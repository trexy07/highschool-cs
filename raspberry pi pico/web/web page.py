import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

import time

from machine import Pin,I2C
from bmp280 import *
import time

bus = I2C(0,scl=Pin(1),sda=Pin(0),freq=200000)
bmp = BMP280(bus)

bmp.use_case(BMP280_CASE_INDOOR)
time.sleep(1)

bus2 = I2C(1,scl=Pin(3),sda=Pin(2),freq=200000)
bmp2 = BMP280(bus2)

bmp2.use_case(BMP280_CASE_INDOOR)



ssid = 'Fluffynet'
password = 'terrycarter'


def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip






def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection





def webpage(temperature, state,now,temp1,p1,temp2,p2):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <form action="./lighton">
            <input type="submit" value="Light on" />
            </form>
            <form action="./lightoff">
            <input type="submit" value="Light off" />
            </form>
            <p>LED is {state}</p>
            <p>Board Temperature is {temperature}</p>
            <p>time is {now}</p>
            <p>temp1 is {temp1}</p>
            <p>pressure1 is {p1}</p>
            <p>temp2 is {temp2}</p>
            <p>pressure2 is {p2}</p>
            
            </body>
            </html>
            """
    return str(html)



def serve(connection):
    #Start a web server
    state = 'OFF'
    pico_led.off()
    temperature = 0
    now=0
    
    p1=0
    temp1=0
    p2=0
    temp2=0
    
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            pico_led.on()
            state = 'ON'
        elif request =='/lightoff?':
            pico_led.off()
            state = 'OFF'
        temperature = pico_temp_sensor.temp
        
        now=time.time()
        
        p1=bmp.pressure
        temp1=bmp.temperature
        p2=bmp2.pressure
        temp2=bmp2.temperature
        
        
        
        
        html = webpage(temperature, state,now,temp1,p1,temp2,p2)
        client.send(html)
        client.close()


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()


