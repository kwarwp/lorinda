# lorinda.sara.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"
#papel amassado
PAPEL= "https://i.imgur.com/SmuKKmZ.jpg"
FOCO = "https://i.imgur.com/6e096Va.png"
# laboratorio
SALA1 = "https://i.imgur.com/D0zlOOx.jpg"
#corredor
SALA2 = "https://i.imgur.com/E3rZxCK.jpg"
#paisagem
SALA3= "https://i.imgur.com/75heQSu.png"
#HOSPITAL
SALA4 = "https://i.imgur.com/jAWWom2.jpg"
class naosei:
     def __init__(self):
        self.frida = frida = Sala(n=SALA1, l=SALA2, s=SALA3, o= SALA4)
        #self.frida.norte.vai()
        
        Texto(frida.norte, "Olá, você está no centro de pesquisa. Encaminhe- se a direita ").vai()
        Texto(frida.leste, "Vá para a sala do Dr. Zuckman").vai()
        
        self.foco=Elemento(img= FOCO)
        
        viu = Elemento(FOCO, x=830, y=200, w=30, h=200, tit= "porta", cena=self.frida.leste, style={"opacity": 0})# vai=self.frida.sul.vai)
        self.falaporta= Texto(frida.leste, "A porta está trancada")
        self.foco.vai=self.falaporta.vai
        
        self.papel=Elemento(img="https://i.imgur.com/SmuKKmZ.jpg", tit= "desenho", x=830, y=200, w=30, h=200)
        self.papel.entra(frida.leste)
naosei()