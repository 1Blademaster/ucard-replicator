import time
import utime

from machine import Pin

from epd import EPD_2in66

'''

(y, x)
0, 296  ------ 0, 0
                USB ->
122, 296 --- 152, 0

0xff = white
0x00 = black

fill_rect(y, x, h, w)

n = narrow
w = wide
s = space

'''

Y_START = 25
Y_END = 100
THIN_BAR = 1
WIDE_BAR = 3

ASTERIX = 'nsnwwn'

NUMBERS = [
    'nnswwn', 'wnsnnw', 'nwsnnw', 'wwsnnn', 'nnswnw', 'wnswnn', 'nwswnn',
    'nnsnww', 'wnsnwn', 'nwsnwn'
]

UCARDS = [
    '001760667',
    '001760668',
    '001760669',
    '001713214',
]

btn = Pin(14, Pin.IN, Pin.PULL_UP)

btn_last_pressed = time.ticks_ms()

current_index = 0

def drawBarcode(letter, x):
    for idx, b in enumerate(letter):
        if b == 'n':
            epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
            if idx + 1 < len(letter) and letter[idx + 1] == 'w':
                x -= 4
            else:
                x -= 2
        elif b == 'w':
            epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
            if idx + 1 < len(letter) and letter[idx + 1] == 'n':
                x -= 2
            else:
                x -= 4
        elif b == 's':
            if idx - 1 > -1 and idx + 1 < len(letter) and (
                (letter[idx - 1] == 'n' and letter[idx + 1] == 'n') or
                (letter[idx - 1] == 'w' and letter[idx + 1] == 'w') or
                (letter[idx - 1] == 'w' and letter[idx + 1] == 'n')):
                x -= 2
            else:
                x -= 4

def displayUcard(ucard_number):
    epd.Clear(0xff)
    epd.fill(0xff)

    x = 246

    code = ASTERIX

    for n in ucard_number:
        code += NUMBERS[int(n)]

    code += ASTERIX

    drawBarcode(code, x)

    epd.text(ucard_number, 38, 15, 0x00)

    epd.display(epd.buffer)

def btnHandler(pin):
    global btn_last_pressed, UCARDS, current_index
    if time.ticks_diff(time.ticks_ms(), btn_last_pressed) > 1000:
        displayUcard(UCARDS[current_index % len(UCARDS)])

        current_index += 1

        btn_last_pressed = time.ticks_ms()

if __name__ == '__main__':
    # ucard_number = input('Enter a UCard number: ')

    epd = EPD_2in66()

    btn.irq(trigger=Pin.IRQ_RISING, handler=btnHandler)

    # displayUcard(ucard_number)
