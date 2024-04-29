# Source: Electrocredible.com, Language: MicroPython

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


while True:
    pressure=bmp.pressure
    temp=bmp.temperature
    
    pressure2=bmp2.pressure
    temp2=bmp2.temperature
    
    
    
    
    print(f"Temperature: {temp} C")
    print(f"Pressure: {pressure} pa")
    print(f"Temperature2: {temp2} C")
    print(f"Pressure2: {pressure2} pa")
    
    
    
    
    time.sleep(2)