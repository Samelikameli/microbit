from microbit import *
with open("passcode") as passcode:
    code=passcode.read()
display.scroll(code)
def password():
    display.clear()
    for i in range(5):
        display.set_pixel(i,1,2)
        display.set_pixel(i,3,2)
    c=0
    pc=[]
    while button_a.is_pressed() or button_b.is_pressed():
        sleep(10)
    while c<5:
        a=button_a.is_pressed()
        b=button_b.is_pressed()
        if a or b:
            if a:
                pc.append(True)
                display.set_pixel(c,2,9)
                c+=1
                while button_a.is_pressed():
                    sleep(10)
            else:
                pc.append(False)
                display.set_pixel(c,2,9)
                c+=1
                while button_b.is_pressed():
                    sleep(10)
    display.clear()
    return pc==[True,True,False,True,True]
display.clear()
while 1:
    #alku
    a=button_a.is_pressed()
    b=button_b.is_pressed()
    if a or b:
        if password():
            display.show(Image.HAPPY)
        else:
            display.show(Image.ANGRY)
        sleep(1000)
    sleep(10)