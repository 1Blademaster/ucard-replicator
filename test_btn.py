from machine import Pin
import time
import utime

led = Pin(25, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_UP)

btn_last_pressed = time.ticks_ms()


def btnHandler(pin):
    print('Button pressed')
    global led, btn_last_pressed
    if time.ticks_diff(time.ticks_ms(), btn_last_pressed) > 500:
        print('Button pressed')
        led.toggle()
        btn_last_pressed = time.ticks_ms()


btn.irq(trigger=Pin.IRQ_RISING, handler=btnHandler)

# while True:
#     led.value(1)
#     utime.sleep(0.5)
#     led.value(0)
#     utime.sleep(0.5)
