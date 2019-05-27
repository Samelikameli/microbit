from microbit import *
from random import randint

while 1:
    choice=randint(0,1)
    sleep(randint(500,10000))
    fail=button_a.is_pressed() or button_b.is_pressed()
    t1=running_time()
    display.set_pixel(4*choice,2,5)
    while 1:
        if button_a.is_pressed():
            press="a"
            break
        elif button_b.is_pressed():
            press="b"
            break
    t2=running_time()  
    if choice:
        if press!="b":
            fail=True
    else:
        if press!="a":
            fail=True
    if fail:
        display.show(Image.NO)
        sleep(200)
    else:
        display.show(Image.YES)
        sleep(200)
        display.scroll(str(t2-t1))
    display.clear()
