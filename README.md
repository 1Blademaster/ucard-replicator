# ucard-replicator
A small device meant to replicate CODE-39 barcodes on an e-ink display using a Raspberry Pi Pico

- - - 
*Using Pico-Go on VSCode 1.65.2*

*My E-Ink display*: https://www.waveshare.com/wiki/Pico-ePaper-2.66
*Docs*: https://www.waveshare.com/wiki/Pico-ePaper-2.66

### To run:

First transfer `epd.py` onto the Pico's filesystem, then you can run `main.py`.

Currently when `main.py` is ran on the Pico, you can input a UCard number and it will be shown as a code-39 barcode.

> I have not extensively tested the barcode printing functionality. It may not work on different screen sizes and edge cases have not been tested.

- - -

##### ToDo:
- Add another button to create custom barcodes
- Tidy up code
- Add a switch and connect the Pico to a small LiPo battery


- - -
Note: any misuse of this device/usage not allowed by the university is not my responsibility and will be your fault.
