# lorinda.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"
#quadro negro
BOTAO = "https://pngimage.net/wp-content/uploads/2018/05/bot%C3%A3o-power-png-7.png"
#saladeinformatica 1 CENA
SALA ="https://i.imgur.com/Z0jbt5J.png"
TELACOMPUTER = "https://i.imgur.com/307pZY8.png"

class oi:
    def __init__(self):
        self.sala1=Cena(img=SALA)
       
        
        self.botao=Elemento(img=BOTAO,tit="ligar",
        style=dict(left=330, top=230, width=80, heigth="2000000000px")) 
        self.botao.entra(self.sala1)
        self.computer=Cena(img = TELACOMPUTER)
        self.botao.vai=self.computer.vai
        #self.falamenino= Texto(self.sala1, "")
        #self.botao.vai=self.falamenino.vai
       
        self.sala1.vai()
oi()