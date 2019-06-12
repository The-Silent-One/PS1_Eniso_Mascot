from tkinter import *
import pygame
import pygame.locals
import time
import webbrowser
from test2 import marche


def Dtxt(screen,ft,ch,x,y):
    screen.blit(ft.render(ch,True,(0,0,0)),(x,y))
    pygame.display.update()

def Butt(screen,elt,t):
    return pygame.draw.rect(screen,elt,t)

def cal():
    r=pygame.mixer.Sound('BB8 Loading Data.wav')
    r.play()
    time.sleep(5)
    r=pygame.mixer.Sound('BB8 Follow me!.wav')
    r.play()
    time.sleep(3)
    r=pygame.mixer.Sound('BB8 Walking.wav')
    r.play()
    
def fr():
    r=pygame.mixer.Sound('BB8 Frustration.wav')
    r.play()
    time.sleep(3)
 
def main():
    root=Tk()
    x,y=root.winfo_screenwidth(),root.winfo_screenheight()
    root.destroy()
    pygame.init()
    screen=pygame.display.set_mode((x,y))
    pygame.display.set_caption("Welcome")

    v=True
    BAc=(95,158,160)
    BBc=(30,144,255)
    BRc=(0,191,255)
    Bamphic=(100,149,237)
    Bexitc=(230,0,0)
    bx,by=x/4,y/5.5

    pygame.mixer.init()
    hello=pygame.mixer.Sound("BB8-Hello.wav")
    hello.play()
    time.sleep(2.5)
    text=['Bloc A','Bloc B','Bloc R','Amphi','exit']
    pygame.font.init()
    screen.fill((255,255,255))
    im=pygame.image.load("enisologo.png").convert()
    screen.blit(im,(0,50))
    ft=pygame.font.SysFont("comicsansms",int(by*2/3))
    BA=Butt(screen,BAc,(x-bx,0,bx,by))
    BB=Butt(screen,BBc,(x-bx,by+2,bx,by))
    BR=Butt(screen,BRc,(x-bx,2*(by+2),bx,by))
    Bamphi=Butt(screen,Bamphic,(x-bx,3*(by+2),bx,by))
    Bexit=Butt(screen,Bexitc,(x-bx,4*(by+2),bx,by))
    bnewsc=(39, 96, 136)
    ftn=pygame.font.SysFont("comicsansms",int(by/6))
    bnews=Butt(screen,bnewsc,(0,0,bx/4,by/4))
    Dtxt(screen,ftn,"NEWS",5,5)
    pygame.display.flip()
    for i in range(5):
        Dtxt(screen,ft,text[i],x-bx*5/6,10*i*by/10)
    dep=time.time()
    while v:
        for i in pygame.event.get():
            if (i.type==pygame.MOUSEBUTTONDOWN):
                mouse=pygame.mouse.get_pos()
                if BA.collidepoint(mouse):
                    cal()
                    marche('A')
                if BB.collidepoint(mouse):
                    cal()
                    marche('B')
                if BR.collidepoint(mouse):
                    cal()
                    marche('R')
                if Bamphi.collidepoint(mouse):
                    cal()
                    marche('amphi')
                if bnews.collidepoint(mouse):
                    webbrowser.open('http://www.eniso.info/')
                if (Bexit.collidepoint(mouse))or(i.type==pygame.QUIT):
                    v=False
            if (time.time()-dep>=60):
                v=False
    pygame.quit()
main()