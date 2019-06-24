from microbit import *
import neopixel
import math
num_of_pix = 24
np = neopixel.NeoPixel(pin0, num_of_pix)
p = 0
l=0
np.clear()
t=0

def printN(n):
    b=bin(n)[2:]
    b="0"*(5*5-len(b))+b
    for y in range(5):
        for x in range(5):    
            display.set_pixel(x,y,(b[y*5+x]=="1")*5)


def pulse(period,r,g,b):
    for t in range(period):
        printN(t)
        bright=((-math.cos(t*2*math.pi/period)+1)*0.5)
        for i in range(24):
            R=math.floor(bright*r*0.4)
            G=math.floor(bright*g*0.5)
            B=math.floor(bright*b)
            np[i]=(R,G,B)
        np.show()
    np.clear()

colors=[(255,0,0),(255,127,0),(255,255,0),(0,255,0),(0,0,255),(39,0,51),(139,0,255)]
while True:
    for color in colors:
        r=color[0]
        g=color[1]
        b=color[2]
        pulse(25,r,g,b)
    for color in colors[-2:0:-1]:
        r=color[0]
        g=color[1]
        b=color[2]
        pulse(25,r,g,b)
