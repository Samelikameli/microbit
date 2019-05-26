from microbit import *
import neopixel
import math
num_of_pix = 24
np = neopixel.NeoPixel(pin0, num_of_pix)

for i in range(24):
    np[i]=(32,32,32)
    sleep(100)
    np.show()
