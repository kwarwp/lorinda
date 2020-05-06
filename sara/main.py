# lorinda.sara.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"

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
        self.frida.norte.vai()
        
        Texto(frida.norte, "Olá, você está no centro de pesquisa. Encaminhe- se a direita ").vai()
        
        auu = Elemento(FOCO, x=190, y=320, w=150, h=80, cena=self.um.oeste, style={"opacity": 40}, vai=self.frida.sul.vai)
        Texto(frida.leste, "Vá para a sala do Dr. Zuckman").vai()
naosei()