# lorinda.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"
#quadro negro
BOTAO = "https://pngimage.net/wp-content/uploads/2018/05/bot%C3%A3o-power-png-7.png"
#
FOCO = "https://i.imgur.com/6e096Va.png"
#saladeinformatica 1 CENA
SALA1 ="https://i.imgur.com/bnapnxL.png"
  #teladocomputador
SALA2 = "https://i.imgur.com/307pZY8.png"
#tela das pastas
SALA3 = "https://i.imgur.com/uGG1xMk.png"
#codon embaralhado
SALA4 = "https://i.imgur.com/fxMYKmc.png"
# codon AUU (uau) TIROSINA
SALA5 = "https://i.imgur.com/mLC28Jx.png"
# codon GUA(agu) SERINA
SALA6 = "https://i.imgur.com/AdIuakb.png"
# codon AAU(aua) ISOLEUCINA
SALA7 = " https://i.imgur.com/Ey3Gccw.png"
#codon GAU (aug) metionina
SALA8 = "https://i.imgur.com/9ZxVZDJ.png"
class oi:
    def __init__(self):
        self.um = um = Sala(n=SALA1, l=SALA2, s=SALA3, o= SALA4)
        self.um.oeste.vai
        
        self.uma= uma = Sala(o= SALA4, s= SALA5, l= SALA6, n= SALA1)
        
        self.dois = dois = Sala (n=Sala1, s= SALA7, l= SALA8, o= SALA4)
        
        Texto(self.um.norte, "Seja bem vindo, cientista! Hoje iremos aprender um pouquinho sobre biologia com o auxilio da nossa maravilhosa tecnologia. Vamos nessa?").vai()

        
        #self.botao=Elemento(img=BOTAO,tit="ligar",
        #style=dict(left=330, top=230, width=80, heigth="2px")) 
        self.botao=Elemento(img=BOTAO,tit="ligar",
        style=dict(left=350,top=270,width=30,height="30px")) 
        self.botao.entra(um.norte)
        self.botao.vai=self.um.leste.vai
        

        
        self.voltar1=Elemento(img="https://image.flaticon.com/icons/png/512/74/74345.png", tit="desligar",
        style=dict(left=200, top=550, width=60, height="50px")) 
        self.voltar1.entra(um.leste)
        self.voltar1.vai=self.um.norte.vai
        
        
        self.sistema = Elemento (img= "https://i.imgur.com/n4R7Cs6.png",
        style=dict(left=330, top=400, width=150, maxHeight = "90000000px"))
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
        style=dict(left=1000, top=100, width=90, height="90px")) 
        self.aminoacido.entra(um.oeste)
        self.falamido= Texto(um.oeste, "Uma grande parte dos nossos células, músculos e tecido é constituído por aminoácidos, o que significa que realizar muitas funções importantes do corpo, tais como as células dando a sua estrutura. Eles também desempenham um papel chave no transporte e armazenamento de nutrientes.")
        self.aminoacido.vai=self.falamido.vai

        self.dica=Elemento(img= "https://i.imgur.com/J5A0Jdo.png", tit = "dica!!",
        style=dict(left=530, top=500, width=80, heigth="80px"))
        self.dica.entra(um.oeste)
        self.faladica= Texto(um.oeste, "Met(metionina)")
        self.dica.vai=self.faladica.vai

        auu = Elemento(FOCO, x=190, y=320, w=150, h=80, cena=self.um.oeste, style={"opacity": 0}, vai=self.uma.sul.vai)
        gua = Elemento(FOCO, x=400, y=320, w=150, h=80, cena=self.um.oeste, style={"opacity": 0}, vai=self.uma.leste.vai)
        aau = Elemento(FOCO, x=590, y=320, w=150, h=80, cena=self.um.oeste, style={"opacity": 0}, vai=self.dois.sul.vai)
        gau = Elemento(FOCO, x=800, y=320, w=150, h=80, cena=self.um.oeste, style={"opacity": 0}, vai=self.dois.leste.vai)
        self.um.norte.vai()
oi()