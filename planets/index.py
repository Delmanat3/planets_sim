from cgitb import grey
from operator import truediv
from pickle import TRUE
import pygame
import math
pygame.init()
WIDTH,HEIGHT=800,800
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("KSP wannabe")

WHITE=(255,255,255)
YELLOW=(255,255,0)
BLUE=(65,105,225)
RED=(188,39,50)
GREY=(80,78,80)

class Planet:
    au = 149.6e6 * 1000   # au km to meters 
    grav=6.67428e-11
    scale=120/au #1 au is 100 px
    time_scale=3600*24 #day in sec

    def __init__(self,x,y,radius,color,mass):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.mass=mass
        self.sun=False
        self.dist_sun=0
        self.orbit=[]
        self.x_vel=0
        self.y_vel=0


    def draw(self,win):
        x=self.x*self.scale+WIDTH/2
        y=self.y*self.scale+HEIGHT/2
        pygame.draw.circle(win,self.color,(x,y),self.radius)


        
def main():
    run=True
    clock=pygame.time.Clock()

    sun=Planet(0,0,30,YELLOW,1.98892*10**30) #kg
    sun.sun=TRUE
    #distsun x,y color, mass
    earth=Planet(-1*Planet.au,0,16,BLUE,5.9742*10**24 )
    mars=Planet(-1.5424*Planet.au,0,12,RED,6.39*10**23 )
    mercury=Planet(0.387*Planet.au,0,8,GREY,0.30*10**24 )
    venus=Planet(0.723*Planet.au,0,14,WHITE,4.8685*10**24 )
    # saturn=Planet(0.723*Planet.au,0,14,WHITE,4.8685*10**24 )
    # jupiter=Planet(0.723*Planet.au,0,14,WHITE,4.8685*10**24 )
    #F=G*(Mm)/(r**2) const val 6.674×10−11      g=(G*M)/(r**2)  kappa ={\frac {8\pi G}{c^{2}}}\approx 1.866\times 10^{-26}\mathrm {\,m{\cdot }kg^{-1}} ein-tens



    planets=[sun,earth,mars,mercury,venus]

    while run:
        clock.tick(60)
        # win.fill(WHITE)
        # pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        for planet in planets:
            planet.draw(win)
        pygame.display.update()

    pygame.quit()

main()