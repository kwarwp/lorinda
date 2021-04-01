# lorinda.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import Inventario as inv 


MARIA = "https://imgur.com/OTFGXEr"
ROSALINDA = "https://imgur.com/0Dv7w29"
LABORATORIO = "https://imgur.com/c71g0qt"
LABORATORIO_1 = "https://imgur.com/c71g0qt"
LABORATORIO_2 = "https://imgur.com/c71g0qt"
LABORATORIO_3 = "https://imgur.com/c71g0qt"
ESTRTURA= "https://imgur.com/iaGv545"
class fase3():
    def __init__(self):
    self.laboratorio=Cena(img=LABORATORIO)
    self.maria=Elemento(img=MARIA, tit="oi,  Dr. Rosalinda sou sua fã, li todos os seus livros e seu artigo sobre "Direcionamento de Proteínas", ou seja, como as proteínas percorrem toda a célula")
    self.rosalinda=Elemento(img=ROSALINDA, tit="as proteínas são muito importantes, para a nossa saúde e beleza! Precismos estuda-las, para nos manter saudáveis, fortes e bonitas. ")
    self.maria.entra(self.laboratorio)
    self.rosalinda.entra(self.laboratorio)
    
    def some (ev):
        self.rosalinda=-100000
    self.laboratorio_1 = Cena(img= LABORATORIO)
    self.laboratorio.direita=self.laboratorio_1
    self.laboratorio_1.esquerda=self.laboratorio
    self.rosalinda.entra(self.laboratorio_1)
    self.elt.onclick = some
    self.maria.entra(self.laboratorio_1)
    self.maria(tit=" Sim, elas são importantes.Então quer dizer que se eu não me alimentar bem, posso ter cabelos, unhas e pele feias?") 
    self.rosalinda(tit= "sim claro")
    #rosalinda some 
    
    self.laboratoria_2= Cena(img=LABORATORIO)
    self.laboratorio_1.direita=self.laboratorio_2
    self.laboratorio_1.esquerda=self.laboratorio_1
    self.maria.entra(self.laboratorio_2, tit= " Como ela desapareceu?")
    self.npc.entra(self.laboratorio_2)
    self.npc= Elemento(img=NPC, tit " Você não deve esquecer do seu verdadeiro propósito buscar, desvendar um grande enigma celular. Você deve sempre lembrar que para uma célula funcionar, todas as suas organelas conectadas devem estar. Quando uma proteína conseguir transportar, livre você estará!")
    
    