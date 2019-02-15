from microbit import *
def printBin(i):
    b=bin(abs(i))[2:]
    b="0"*(25-len(b))+b
    s=list(b[0:5]+":"+b[5:10]+":"+b[10:15]+":"+b[15:20]+":"+b[20:25])
    #s=s[::-1]
    for i in range(len(s)):
        if s[i]=="1":
            s[i]="5"
    display.show(Image("".join(reversed(s))))
i=0
while 1:
    a=button_a.is_pressed()
    b=button_b.is_pressed()
    if a and b:
        sleep(1000)
        display.scroll("Menu")
        c=0
        i=0
        while c<25:
            a=button_a.is_pressed()
            b=button_b.is_pressed()
            if a:
                i+=2**c
                c+=1
                sleep(300)
            if b:
                c+=1
                sleep(300)
            printBin(i)

    elif a:
        i+=1
        printBin(i)
        sleep(200)
    elif b:
        i-=1
        printBin(i)
        sleep(200)