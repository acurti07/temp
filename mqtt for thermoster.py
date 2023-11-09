WIFI_SSID= "Tufts_Secure"
WIFI_PASSWORD=""

import network
from time import sleep
from machine import Pin
import ntptime

sleep(1)
wlan = None
while not wlan or wlan.status() !=3:
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    
    while True:
        print(wlan)
        #led.toggle()
        sleep(0.2)
        if wlan.status() in [-1, -2, -3]:
            break
        
ntptime.settime()