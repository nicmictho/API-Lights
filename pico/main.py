import machine
import neopixel
from time import sleep
import network
import urequests
from settings import ssid, password
import math


p = 28
n = 30

old_lights = [(0,0,0) for i in range(n)]
new_lights = [(0,0,0) for i in range(n)]

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


try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()

print(ip)

def fade(old_lights, new_lights):
    global n
    steps = 50
    step = 0
    current = [0,0,0]
    while step <= steps:
        for LEDno in range(n): # For each LED
            for colourno in range(3): # For each colour component
                old_led, new_led = (old_lights[LEDno], new_lights[LEDno]) # For LED, get old and new values
                current[colourno] = round((new_led[colourno] - old_led[colourno]) * ((math.atan(0.1*(step - steps/2)) + math.pi/2) / math.pi) + old_led[colourno])
            np[LEDno] = tuple(current)
        np.write()
        step += 1
    return
    

np = neopixel.NeoPixel(machine.Pin(p),n)

while True:
    response = urequests.get('http://192.168.1.89:8080/API')
    data = response.json()
    print(data)
    for i in data:
        new_lights[int(i)] = data[i]
    fade(old_lights, new_lights)
    # for i in data:
    #     np[int(i)] = tuple(new_lights[int(i)])
    # np.write()
    old_lights = new_lights.copy()
