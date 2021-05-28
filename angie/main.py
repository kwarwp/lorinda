# lorinda.angie.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from math import sin, cos, pi
D30 = pi/6
D90 = pi/2
SUJ = "https://i.imgur.com/84sRLl2.jpg"
STYLE.update(width=1200, height="650px")
c = Cena("https://i.imgur.com/ECVki8P.jpg")
roda = Elemento("https://i.imgur.com/84sRLl2.jpg", x=200, y=100, w=400, h=400, cena=c)
#suj1 = Elemento(SUJ, x=175, y=10, w=50, h=50, cena=roda)
#suj2 = Elemento(SUJ, x=200+ 165*cos(D30), y=200-190*sin(D30), w=50, h=50, cena=roda)
#suj3 = Elemento(SUJ, x=200+ 165*cos(2*D30), y=200-190*sin(2*D30), w=50, h=50, cena=roda)
'''
suj2 = Elemento(SUJ, x=int(200+ 175*cos(D30-D90))-25, y=int(200-175*sin(D30-D90)), w=50, h=50, cena=roda)
suj3 = Elemento(SUJ, x=int(200+ 175*cos(2*D30-D90))-25, y=int(200-175*sin(2*D30-D90)), w=50, h=50, cena=roda)
suj4 = Elemento(SUJ, x=int(200+ 175*cos(3*D30-D90))-25, y=int(200-175*sin(3*D30-D90)), w=50, h=50, cena=roda)
suj5 = Elemento(SUJ, x=int(200+ 175*cos(4*D30-D90))-25, y=int(200-175*sin(4*D30-D90)), w=50, h=50, cena=roda)
suj6 = Elemento(SUJ, x=int(200+ 175*cos(5*D30-D90))-25, y=int(200-175*sin(5*D30-D90)), w=50, h=50, cena=roda)
suj7 = Elemento(SUJ, x=int(200+ 175*cos(6*D30-D90))-25, y=int(200-175*sin(6*D30-D90)), w=50, h=50, cena=roda)
'''
dims = dict( w=50, h=50, cena=roda)
suj = [Elemento(SUJ, x=int(200+ 170*cos(tt*D30-D90))-25, y=int(200-170*sin(tt*D30-D90))-25,
        style=dict(transform=f"rotate({-tt*30}deg)"), **dims)
        for tt in range(12)]
#suj3 = Elemento(SUJ, x=int(200+ 165*0.86), y=int(200-190*0.5), w=50, h=50, cena=roda)
#print(190*cos(D30-D90),200-190*sin(D30-D90))
#print(200+ 190*cos(D30),200-190*sin(D30))
#print(200+ 190*cos(2*D30),200-190*sin(2*D30))
#suj2.elt.style.transform = "rotate(30deg)"
#roda.elt.style.transform = "rotate(30deg)"
c.vai()