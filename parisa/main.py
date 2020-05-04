# lorinda.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "600px"
#quadro negro
BOTAO = "https://pngimage.net/wp-content/uploads/2018/05/bot%C3%A3o-power-png-7.png"
#

#saladeinformatica 1 CENA
SALA1 ="https://i.imgur.com/bnapnxL.png"
  #teladocomputador
SALA2 = "https://i.imgur.com/307pZY8.png"
#tela das pastas
SALA3 = "https://i.imgur.com/uGG1xMk.png"
#mar
SALA4 = "https://www.brunobobone.com/wp-content/uploads/2018/07/economia-do-mar-Portugal-des%C3%ADgnio-nacional.jpg"

class oi:
    def __init__(self):
        self.um = um = Sala(n=SALA1, l=SALA2, s=SALA3, o= SALA4)
        self.um.oeste.vai
        

        self.botao=Elemento(img=BOTAO,tit="ligar",
        style=dict(left=330, top=230, width=80, heigth="2px")) 
        self.botao.entra(um.norte)
        self.botao.vai=self.um.leste.vai
        

        
        self.voltar1=Elemento(img="https://image.flaticon.com/icons/png/512/74/74345.png", tit="desligar",
        style=dict(left=80, top=510, width=80, heigth="2000000000px")) 
        self.voltar1.entra(um.leste)
        self.voltar1.vai=self.um.norte.vai
        
        self.pasta = Elemento (img="https://i.imgur.com/bPsIZws.png", tit = "pasta", 
        style=dict(left=330, top=230, width=80, heigth="2px")) 
        self.pasta.entra(um.sul)

        self.sistema = Elemento (img= "https://i.imgur.com/n4R7Cs6.png",
        style=dict(left=330, top=300, width=150, heigth="2px"))
        self.sistema.entra(um.leste)
        self.sistema.vai



        self.um.norte.vai()
oi()