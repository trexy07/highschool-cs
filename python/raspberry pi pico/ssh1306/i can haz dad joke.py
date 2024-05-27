# get wifi
import network

import time

ssid = 'Fluffynet'
password = 'terrycarter'


def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip


try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()




### get joke
import urequests as requests

# format
def fix(word):
    return word.replace("\u2026","...").replace("\u2019","'").replace("\u2018","'").replace("\u201d",'"').replace("\u201c",'"')


final="012345678"

while len(final)>8:

    res=requests.get("https://icanhazdadjoke.com/",headers={"Accept": "application/json" })

    print(eval(res.text)["joke"])



    
    text=eval(res.text)["joke"].replace('\r\n',' ').replace('\r',' ').replace('\n',' ')



    text=text.split(' ')
    final=[""]

    firstSentence=True

    for word in text:
        
        
        if len(final[-1])+len(word)+1<=16:
            if len(final[-1])!=0:
                final[-1]+=' '
            final[-1]+=fix(word)
            
        else:
            final.append(fix(word))
            
            
        if ('.' in word or '?' in word) and firstSentence:
            if len(final)<5:
                while len(final)<5:
                    final.append("")
            else:
                if len(final)<7:
                    final.append("")
                final.append("")
            firstSentence=False
    while len(final)<8:
        final.append("")
    print(final)




#show
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 32, i2c)

i2c2=I2C(1,sda=Pin(2), scl=Pin(3), freq=400000)
oled2 = SSD1306_I2C(128, 32, i2c2)


for i in range(4):
    oled.text(final[i], 0, i*8)
    oled.show()
    
for i in range(4,8):
    oled2.text(final[i], 0, i*8-32)
    oled2.show()








