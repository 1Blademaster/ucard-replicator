from epd import EPD_2in66
import utime
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


if __name__ == '__main__':
    ucard_number = input('Enter a UCard number: ')

    epd = EPD_2in66()
    epd.Clear(0xff)
    epd.fill(0xff)

    x = 246

    asterix = 'nsnwwn'

    numbers = [
        'nnswwn', 'wnsnnw', 'nwsnnw', 'wwsnnn', 'nnswnw', 'wnswnn', 'nwswnn',
        'nnsnww', 'wnsnwn', 'nwsnwn'
    ]

    code = asterix

    for n in ucard_number:
        code += numbers[int(n)]

    code += asterix

    drawBarcode(code, x)

    epd.text(ucard_number, 38, 15, 0x00)

    epd.display(epd.buffer)
