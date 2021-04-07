# lorinda.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import Inventario as inv 
# salas do games da Angelica, lorinda-lisa-libby e kellee

MARIA = "https://imgur.com/OTFGXEr.png"
ROSALINDA = "https://imgur.com/0Dv7w29.png"
LABORATORIO = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_1 = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_2 = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_3 = "https://imgur.com/c71g0qt.jpg"
ESTRTURA= "https://imgur.com/iaGv545.png"
DNA= ""
NPC=""
class fase3():
    def __init__(self):
        self.laboratorio=Cena(img=LABORATORIO)
        self.maria=Elemento(img=MARIA, tit='oi,  Dr. Rosalinda sou sua fã, li todos os seus livros e seu artigo sobre "Direcionamento de Proteínas", ou seja, como as proteínas percorrem toda a célula')
        self.rosalinda=Elemento(img=ROSALINDA, tit="as proteínas são muito importantes, para a nossa saúde e beleza! Precismos estuda-las, para nos manter saudáveis, fortes e bonitas. ")
        self.maria.entra(self.laboratorio)
        self.rosalinda.entra(self.laboratorio)
        self.laboratorio.vai()
    
    def some (ev):
        self.rosalinda=-100000
        self.laboratorio_1 = Cena(img= LABORATORIO_1)
        self.laboratorio.direita=self.laboratorio_1
        self.laboratorio_1.esquerda=self.laboratorio
        self.rosalinda.entra(self.laboratorio_1)
        self.elt.onclick = some
        self.maria.entra(self.laboratorio_1)
        self.maria(tit=" Sim, elas são importantes.Então quer dizer que se eu não me alimentar bem, posso ter cabelos, unhas e pele feias?") 
        self.rosalinda(tit= "sim claro")
        #rosalinda some 
    
    def parte_2():
        self.laboratorio_2= Cena(img=LABORATORIO_2)
        self.laboratorio_1.direita=self.laboratorio_2
        self.laboratorio_2.esquerda=self.laboratorio_1
        self.maria.entra(self.laboratorio_2, tit= " Como ela desapareceu?")
        self.npc.entra(self.laboratorio_2)
        self.npc= Elemento(img=NPC, tit=" Você não deve esquecer do seu verdadeiro propósito buscar, desvendar um grande enigma celular. Você deve sempre lembrar que para uma célula funcionar, todas as suas organelas conectadas devem estar. Quando uma proteína conseguir transportar, livre você estará!")
    
    def parte_3():
        self.laboratorio_3=Cena(img=LABORATORIO_3)
        self.laboratorio_2.direita=self.laboratorio_3
        self.laboratorio_3.esquerda=self.laboratorio_2
        self.npc.entra(self.laboratorio_3, tit=" ele não é muito simpático")
        self.maria.entra(self.laboratorio_3, tit=" quem é você?")
        self.dna=Elemento(img= DNA)
        self.dna.entra(self.laboratorio_3, tit="COMO, VOCÊ NÃO SABE MEU NOME?DE QUE PLANETA VOCÊ É?EU SOU O MAIORAL! ")
    
    def parte_4():
        self.laboratorio_4=Cena(img=LABORATORIO_4)
        self.laboratorio_3.direita=self.laboratorio_4
        self.laboratorio_4.esquerda=self.laboratorio_3
        self.dna.entra(self.laboratorio_4, tit="vá estudar garota!")
        self.npc.entra(self.laboratorio_4,tit=" Responda o enigma: Sou constituído por letras, que se encaixam perfeitamente, seguindo uma determinada ordem. Quando tem algum erro, pode provocar uma doença ou mutação.")
        
fase3()