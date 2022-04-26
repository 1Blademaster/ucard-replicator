from machine import Pin
import time
import utime

led = Pin(25, Pin.OUT)
btn = Pin(14, Pin.IN, Pin.PULL_UP)

btn_last_pressed = time.ticks_ms()

current_index = 0

arr = [1, 2, 3, 4, 5]

def btnHandler(pin):
    global led, btn_last_pressed, arr, current_index
    if time.ticks_diff(time.ticks_ms(), btn_last_pressed) > 500:
        print('Button pressed')
        led.toggle()

        print(arr[current_index % len(arr)])
        current_index += 1

        btn_last_pressed = time.ticks_ms()


btn.irq(trigger=Pin.IRQ_RISING, handler=btnHandler)

# while True:
#     led.value(1)
#     utime.sleep(0.5)
#     led.value(0)
#     utime.sleep(0.5)
