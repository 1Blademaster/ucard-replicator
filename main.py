from epd import EPD_2in66
import utime

Y_START = 25
Y_END = 100
THIN_BAR = 1
WIDE_BAR = 3

def draw(char, x, nextN=None):
    if char == '*':
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00) # thin black
        # wide white
        # gap 4
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00) #thin black
        # thin white
        # gap 4
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00) # wide black
        # thin white
        # gap 4
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00) # wide black
        # # thin white
        # # gap 2 ?
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00) # thin black
    elif char == '0':
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 6
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        if nextN in ['1', '3', '5', '8']:
            x -= 2
    elif char == '1':
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
    elif char == '2':
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
    elif char == '3':
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
    elif char == '4':
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 6
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
    elif char == '5':
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 6
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
    elif char == '6':
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 6
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
    elif char == '7':
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
    elif char == '8':
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
    elif char == '9':
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)
        x -= 4
        epd.fill_rect(Y_START, x, Y_END, WIDE_BAR, 0x00)
        x -= 2
        epd.fill_rect(Y_START, x, Y_END, THIN_BAR, 0x00)

    return x - 2

'''

(y, x)
0, 296  ------ 0, 0
                USB ->
122, 296 --- 152, 0

0xff = white
0x00 = black

fill_rect(y, x, h, w)

'''

if __name__ == '__main__':
    ucard_number = '*' + input('Enter a UCard number: ') + '*'

    epd = EPD_2in66()
    epd.Clear(0xff)
    epd.fill(0xff)

    x = 236

    for idx, n in enumerate(ucard_number):
        try:
            x = draw(n, x, ucard_number[idx+1])
        except IndexError:
            x = draw(n, x)

    epd.text(ucard_number.replace('*', ''), 38, 15, 0x00)
            
    epd.display(epd.buffer)
