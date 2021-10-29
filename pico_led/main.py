from machine import Pin
import time

p25 = Pin(25,Pin.OUT)
while True:
    p25.on()
    time.sleep(1)
    p25.off()
    time.sleep(1)