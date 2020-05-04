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
SALA4 = "https://i.imgur.com/fxMYKmc.png"

class oi:
    def __init__(self):
        self.um = um = Sala(n=SALA1, l=SALA2, s=SALA3, o= SALA4)
        self.um.oeste.vai
        
        Texto(self.um.norte, "Seja bem vindo, cientista! Hoje iremos aprender um pouquinho sobre biologia com o auxilio da nossa maravilhosa tecnologia. Vamos nessa?").vai()

        
        #self.botao=Elemento(img=BOTAO,tit="ligar",
        #style=dict(left=330, top=230, width=80, heigth="2px")) 
        self.botao=Elemento(img=BOTAO,tit="ligar", x=330, y=430, w=80) 
        self.botao.entra(um.norte)
        self.botao.vai=self.um.leste.vai
        

        
        self.voltar1=Elemento(img="https://image.flaticon.com/icons/png/512/74/74345.png", tit="desligar",
        style=dict(left=80, top=510, width=80, heigth="2000000000px")) 
        self.voltar1.entra(um.leste)
        self.voltar1.vai=self.um.norte.vai
        
        
        self.sistema = Elemento (img= "https://i.imgur.com/n4R7Cs6.png",
        style=dict(left=330, top=400, width=150, heigth="2px"))
        self.sistema.entra(um.leste)
        self.sistema.vai=self.um.sul.vai
        
        self.cadeia = Elemento (img = "https://i.imgur.com/a2E0TI7.png", tit= "senha",
        style=dict(left=730, top=400, width=150, heigth="2px"))
        self.cadeia.entra(um.leste)
        self.cadeia.vai
        
        
        self.somatico = Elemento (img = "https://i.imgur.com/V5RQYKz.png", tit ="senha",
        style=dict(left=530, top=400, width=150, heigth="2px"))
        self.somatico.entra(um.leste)
        self.somatico.vai

        self.pasta = Elemento (img="https://i.imgur.com/bPsIZws.png", tit = "pasta", 
        style=dict(left=320, top=200, width=100, heigth="2px")) 
        self.pasta.entra(um.sul)
        self.pasta.vai=self.um.oeste.vai

        Texto(self.um.oeste, "Como nada nessa vida é fácil, você precisará de uma senha para a proxima etapa. Há 4 códigos genéticos que estão embaralhados, você terá que desembaralhar todos e descobrir o 'nosso' aminoacido secreto. FIQUE ATENTO AS NOSSAS DICAS!! ").vai()
        self.aminoacido= Elemento(img= "https://i.imgur.com/YF2cXp3.png", tit ="Aminoácido",
        style=dict(left=780, top=200, width=300, heigth="2px")) 
        self.aminoacido.entra(um.oeste)
        self.falamido= Texto(um.oeste, "Muito obrigado, Senhora Neide")
        self.aminoacido.vai=self.falamido.vai

        
        self.um.norte.vai()
oi()