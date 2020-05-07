# lorinda.alexa.main.py
#TASSIA- 3001 isabelle
from _spy.vitollino.main import Cena, Elemento, Labirinto
from _spy.vitollino.main import INVENTARIO as inv
#fase2
CIENTISTA="https://3.bp.blogspot.com/_YaD6P9li0m0/SOp_1mDcfPI/AAAAAAAAAHk/wGNocvYRjbY/s320/222px-Professor_Frink.png"
ESCADA="https://i.pinimg.com/originals/77/83/aa/7783aae2cd02f662c3344824ecd43287.jpg"
PRATELEIRA=""
CAMERA=""
SETAS=""
PORTA=""
LABORATORIO=""
#fase2

class OVINHO():
    def __init__ (self):
    cientista= Elemento (img=CIENTISTA)
    sala1= Cena (img=ESCADA)
    sala2=Cena (img=PRATELEIRA)
    sala3=Cena (img=CAMERA)
    setas=Elemento (img= SETAS)
    sala4=Cena (img=PORTA)
    sala5=Cena (img=LABORATORIO)
    haha=Labirinto (norte=sala1,leste=sala2,oeste=sala3,sul=sala4)
    cientista.entra(haha.norte)
    haha.norte.vai()
    
OVINHO()