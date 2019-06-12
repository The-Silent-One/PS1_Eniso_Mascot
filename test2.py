import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT) #Right motor control
GPIO.setup(18,GPIO.OUT) #Right motor control
GPIO.setup(22,GPIO.OUT) #Left motor control
GPIO.setup(23,GPIO.OUT) #Left motor control
GPIO.setup(16,GPIO.OUT) #trigger
GPIO.setup(24,GPIO.IN)  #echo


def av1(x1,y1,x2,y2):     #Avancer un Pas
    #p=GPIO.PWM(x1,1)
    #p.start(20)
    GPIO.output(x1,1)
    GPIO.output(y1,0)
    GPIO.output(x2,1)
    GPIO.output(y2,0)
    time.sleep(1)
    stp(18,17,22,23)
    
def marche(ch):
    import RPi.GPIO as GPIO
    import time
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT) #Right motor control
    GPIO.setup(18,GPIO.OUT) #Right motor control
    GPIO.setup(22,GPIO.OUT) #Left motor control
    GPIO.setup(23,GPIO.OUT) #Left motor control
    #if(ch=='A'):
    if True:
        for i in range(1):
            av1(17,18,22,23)
        turnR(17,18,22,23)
        av1(17,18,22,23)
        stp(17,18,22,23)
        time.sleep(2)
        turnL(17,18,22,23)
        av1(17,18,22,23)
        turnL(17,18,22,23)
        for i in range(1):
            av1(17,18,22,23)
        for j in range(2):
            for i in range(4):
                av1(17,18,22,23)
                stp(17,18,22,23)
            turnR(18,17,22,23)
        for i in range(11):
            turnR(18,17,22,23)
    else:
        return 0
    
def turnR(x1,y1,x2,y2):     #tourner à Droite
    #p=GPIO.PWM(x1,1)
    #p.stop(0)
    GPIO.output(x1,1)
    GPIO.output(y1,0)
    GPIO.output(x2,1)
    GPIO.output(y2,0)
    time.sleep(1.1)
    stp(x1,y1,x2,y2)

def turnL(x1,y1,x2,y2):     #tourner à Gauche
    p=GPIO.PWM(x1,1)
    p.start(50)
    #GPIO.output(x1,1)
    GPIO.output(y1,0)
    GPIO.output(x2,0)
    GPIO.output(y2,1)
    time.sleep(0.5)
    stp(x1,y1,x2,y2)
    
def stp(x1,y1,x2,y2):      #Arrêt des moteurs
    #p=GPIO.PWM(x1,1)
    #p.stop()
    GPIO.output(x1, 0)
    GPIO.output(y1, 0)
    GPIO.output(x2, 0)
    GPIO.output(y2, 0)
    time.sleep(0.5)
    
def capt(trg,ech,t):      #Calculer la Distance du plus proche Obstacle
    GPIO.output(x1,0)
    time.sleep(0.1)
    GPIO.output(trg,1)
    time.sleep(0.00001)
    GPIO.output(trg,0)
    while GPIO.input(ech)==0:
        start=time.time()
    while GPIO.input(ech)==1:
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
    k=0
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
                        print("route bloquée")

def Advance_r(trg,ech,n,t):   #Avancer "n" Pas
    i=0
    k=0
    while (i<n):
        d=capt(trg,ech,t)
        if (d>25):
            av1_r(t[0],t[1],t[2],t[3])
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
                        print("route bloquée")

def Advance_l(trg,ech,n,t):   #Avancer "n" Pas
    i=0
    k=0
    while (i<n):
        d=capt(trg,ech,t)
        if (d>25):
            av1_l(t[0],t[1],t[2],t[3])
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
                        print("route bloquée")                        

 
def TEST(trg,ech,t):
    #aller au bloc B
    advance(trg,ech,5,t)
    turnL(18,17,22,23)
    advance(trg,ech,3,t)
    turnL(18,17,22,23)
    # pause
    #we can add a Speech like "Here is your destination"
    time.sleep(15)
    # retour a la position de départ
    turnL(18,17,22,23)
    advance(trg,ech,3,t)
    turnR(18,17,22,23)
    advance(trg,ech,5,t)
    #Appel à la Commande "Exit"
    
#marche('A')

#turnL(18,17,22,23)
    
GPIO.cleanup()