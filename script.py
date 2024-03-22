import time
from machine import Pin

led = Pin("PE3", Pin.OUT)
    
while True:
    led.on()
    time.sleep_ms(250)
    led.off()
    time.sleep_ms(250)