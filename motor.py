import time
import RPi.GPIO as GPIO

    
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(16,GPIO.OUT) #trigger
GPIO.setup(24,GPIO.IN) #echo



def marche(ch):
    if(ch=='A'):
        print("A")
    elif(ch=='B'):
        print("B")
    elif(ch=='R'):
        print("R")
    elif(ch=='amphi'):
        print("amphi")


    
def mav(t):
    GPIO.output(t[0],True)
    GPIO.output(t[1],False)
    GPIO.output(t[2],True)
    GPIO.output(t[3],False)
    time.sleep(5)

def mac(x1,y1,t,c=0):
    i=capt(x1,y1)
    if (c==5):
        fr()
        return 0
    if (i>25): 
        mav(t)
        return 1
    else:
        stp(t[0],t[1],t[2],t[3])
        time.sleep(2)
        mac(x1,y1,t,c+1)
        
def mar(x1,y1,x2,y2):
    GPIO.output(x1, False)
    GPIO.output(y1, True)
    GPIO.output(x2, False)
    GPIO.output(y2, True)
    time.sleep(5)

def stp(x1,y1,x2,y2):
    GPIO.output(x1, False)
    GPIO.output(y1, False)
    GPIO.output(x2, False)
    GPIO.output(y2, False)
    time.sleep(1)

def turnR(x1,y1,x2,y2):
    GPIO.output(x1,0)
    GPIO.output(y1,1)
    GPIO.output(x2,1)
    GPIO.output(y2,0)
    time.sleep(2.5)
    
def turnL(x1,y1,x2,y2):
    GPIO.output(x1,1)
    GPIO.output(y1,0)
    GPIO.output(x2,0)
    GPIO.output(y2,1)
    time.sleep(2.5)

def capt(x1,y1):
    GPIO.output(x1,False)
    time.sleep(1)
    GPIO.output(x1,True)
    time.sleep(0.00001)
    GPIO.output(x1,False)
    while GPIO.input(y1)==0:
        start=time.time()
    while GPIO.input(y1)==1:
        end=time.time()
    dur=end - start
    d=(331/2)*dur*100
    print (d)
    return d

def testR(trg,ech,t):
    turnR(t[0],t[1],t[2],t[3])
    d=capt(trg,ech,t)
    if (d>30):
        av1(t[0],t[1],t[2],t[3])
        turnL(t[0],t[1],t[2],t[3])
        d=capt(trg,ech,t)
        if (d>30):
            av1(t[0],t[1],t[2],t[3])
            i+=1
            turnL(t[0],t[1],t[2],t[3])
            d=capt(trg,ech,t)
            if (d>30):
                av1(t[0],t[1],t[2],t[3])
                turnR(t[0],t[1],t[2],t[3])
                return(1)
            else: 
                turnL(t[0],t[1],t[2],t[3])
                av1(t[0],t[1],t[2],t[3])
                turnR(t[0],t[1],t[2],t[3])
                av1(t[0],t[1],t[2],t[3])
                turnR(t[0],t[1],t[2],t[3])
                return(0)
                    
        else:
            turnL(t[0],t[1],t[2],t[3])
            av1(t[0],t[1],t[2],t[3])
            turnR(t[0],t[1],t[2],t[3])
            return(0)
    else:
        turnL(t[0],t[1],t[2],t[3])
        return(0)

def testL(trg,ech,t):
    turnL(t[0],t[1],t[2],t[3])
    d=capt(trg,ech,t)
    if (d>30):
        av1(t[0],t[1],t[2],t[3])
        turnR(t[0],t[1],t[2],t[3])
        d=capt(trg,ech,t)
        if (d>30):
            av1(t[0],t[1],t[2],t[3])
            i+=1
            turnR(t[0],t[1],t[2],t[3])
            d=capt(trg,ech,t)
            if (d>30):
                av1(t[0],t[1],t[2],t[3])
                turnL(t[0],t[1],t[2],t[3])
                return(1)
            else: 
                turnR(t[0],t[1],t[2],t[3])
                av1(t[0],t[1],t[2],t[3])
                turnL(t[0],t[1],t[2],t[3])
                av1(t[0],t[1],t[2],t[3])
                turnL(t[0],t[1],t[2],t[3])
                return(0)
                    
        else:
            turnR(t[0],t[1],t[2],t[3])
            av1(t[0],t[1],t[2],t[3])
            turnL(t[0],t[1],t[2],t[3])
            return(0)
    else:
        turnR(t[0],t[1],t[2],t[3])
        return(0)

def Advance(trg,ech,n,t):   #Avancer "n" Pas
    i=0
    while (i<n):
        d=capt(trg,ech,t)
        if (d>25):
            av1(t[0],t[1],t[2],t[3])
            stp(x1,y1,x2,y2)
            i+=1
        else:
            stp(t[0],t[1],t[2],t[3])
            time.sleep(3) 
            k+=1
            if (k>=4):
                if(testR(trg,ech,t)):
                    i+=1
                else:
                    if (testL(trg,ech,t)):
                        i+=1
                    else:
                        printf("route bloquée")
mav((17,18,22,23))
stp(17,18,22,23)
#mar(17,18,22,23)
#stp(17,18,22,23)
#turnL(17,18,22,23)
#stp(17,18,22,23)
#turnR(17,18,22,23) 
    
GPIO.cleanup()