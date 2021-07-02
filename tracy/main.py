# lorinda.tracy.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, JOGO
from _spy.vitollino.main import Inventario as inv 
from anastasia.main import Associa, SF
# salas do games da Angelica, lorinda-lisa-libby e kellee
STYLE.update(width=600, height="600px")

MARIA = "https://i.imgur.com/FukdPW2.png"
ROSALINDA = "https://imgur.com/0Dv7w29.png"
LABORATORIO = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_1 = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_2 = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_3 = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_4 = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_5 = "https://imgur.com/c71g0qt.jpg"
ESTRTURA= "https://imgur.com/iaGv545.png"
DNA= "https://i.imgur.com/khPaSvV.png"
NPC="https://i.imgur.com/hU2mulx.png"
ENIGMA= "https://i.imgur.com/pwI7UL8.png"
NUCLEO="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
PAREDE="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
ORGANELA="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
COMPLEXOG="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
RNA= "https://i.imgur.com/khPaSvV.png" # trocar essa imagem


class Personagem(Elemento):
    def __init__(self, img=MARIA, x=300, y=400, w=180, h=200, texto="", responde=None):
        super().__init__(img=img, x=x, y=y, w=w, h=h)
        self.texto = texto
        self.responde = responde
        
    def fala(self, cena, responde=None, texto=""):
        Texto(cena, texto if texto else self.texto, foi=responde if responde else self.responde).vai()



class Fase3():
    def __init__(self):
        self.laboratorio=Cena(img=LABORATORIO)
        def rosalinda_fala(_=0):
            rosalinda = ("Rosalinda: As proteínas são muito importantes, para a nossa saúde e beleza!"
            " Precismos estuda-las, para nos manter saudáveis, fortes e bonitas. ")
            Texto(self.laboratorio, rosalinda, foi=self.some).vai()
            
        self.maria = Personagem()
        fala = ('Maria: Oi,  Dr. Rosalinda sou sua fã, li todos os seus livros e seu artigo'
        ' sobre "Direcionamento de Proteínas", ou seja, como as proteínas percorrem toda a célula')
        self.maria.fala(self.laboratorio, responde=rosalinda_fala, texto=fala)
        #self.maria=Elemento(img=MARIA, x=300, y=400, w=180, h=200, tit='oi,  Dr. Rosalinda sou sua fã, li todos os seus livros e seu artigo sobre "Direcionamento de Proteínas", ou seja, como as proteínas percorrem toda a célula')
        self.rosalinda=Elemento(img=ROSALINDA, x=100, y=400, w=180, h=200, tit="as proteínas são muito importantes, para a nossa saúde e beleza! Precismos estuda-las, para nos manter saudáveis, fortes e bonitas. ")
        self.maria.entra(self.laboratorio)
        self.rosalinda.entra(self.laboratorio)
        self.laboratorio_1 = Cena(img= LABORATORIO_1)
        # self.laboratorio.direita=self.laboratorio_1
        self.laboratorio.direita=Cena(vai=self.some)
        self.laboratorio.vai()
    
    def some (self, ev=0):
        def sumir(ev=0):
            self.rosalinda.x=-100000
        self.laboratorio_1.vai()
        self.laboratorio_1.esquerda=self.laboratorio
        self.rosalinda.entra(self.laboratorio_1)
        fala_rosalinda = "sim claro"
        self.rosalinda.vai = Texto(self.laboratorio_1, fala_rosalinda, foi=sumir).vai
        #self.elt.onclick = some
        self.maria.entra(self.laboratorio_1)
        maria_texto=("Maria: Sim, elas são importantes. Então quer dizer que se eu não me alimentar bem,"
        " posso ter cabelos, unhas e pele feias?") 
        self.maria.fala(self.laboratorio_1,responde=self.parte_2, texto= maria_texto) 
        self.rosalinda.tit= ""
        self.laboratorio_1.direita=Cena(vai=self.parte_2)
        #rosalinda some 
    
    def parte_2(self, ev=0):
        self.laboratorio_2= Cena(img=LABORATORIO_2)
        texto = ("Roboide: Você não deve esquecer do seu verdadeiro propósito buscar,"
                 " desvendar um grande enigma celular. Você deve sempre lembrar que para uma célula funcionar,"
                 " todas as suas organelas conectadas devem estar. Quando uma proteína conseguir transportar,"
                 " livre você estará!")
        #self.laboratorio_1.direita=self.laboratorio_2
        self.laboratorio_2.vai()
        self.laboratorio_2.esquerda=self.laboratorio_1
        self.maria.entra(self.laboratorio_2)
        maria_texto= "Maria:  Como ela desapareceu?"
        self.npc= Personagem(img=NPC,y=400,w=160,h=160, texto=texto)
        self.maria.fala(self.laboratorio_2,responde=self.npc.fala, texto=maria_texto) 
        
        self.npc.entra(self.laboratorio_2)
        self.laboratorio_2.direita=Cena(vai=self.parte_3)
    
    def parte_3(self):
        self.laboratorio_3=Cena(img=LABORATORIO_3)
        self.laboratorio_3.vai()
        #self.laboratorio_2.direita=self.laboratorio_3
        self.laboratorio_3.esquerda=self.laboratorio_2
        self.npc.entra(self.laboratorio_3)
        self.maria.entra(self.laboratorio_3)
        self.npc.texto = "Roboide: ele não é muito simpático"
        maria_texto= "Maria:   quem é você?"
        self.dna=Personagem(img= DNA, y=450,x=200, responde=self.npc.fala, texto="COMO, VOCÊ NÃO SABE MEU NOME? DE QUE PLANETA VOCÊ É?EU SOU O MAIORAL! ")
        self.maria.fala(self.laboratorio_3,responde=self.dna.fala, texto=maria_texto) 
        self.dna.entra(self.laboratorio_3)
        self.laboratorio_3.direita=Cena(vai=self.parte_4)

    def parte_4(self):
        self.laboratorio_4=Cena(img=LABORATORIO_4)
        self.laboratorio_4.vai()
        self.laboratorio_4.esquerda=self.laboratorio_3
        self.dna.entra(self.laboratorio_4)
        self.npc.entra(self.laboratorio_4)
        self.dna.tit="vá estudar garota!"
        self.npc.tit=" Responda o enigma: Sou constituído por letras, que se encaixam perfeitamente, seguindo uma determinada ordem. Quando tem algum erro, pode provocar uma doença ou mutação."
        self.laboratorio_4.direita=Cena(vai=self.parte_5)
        
        #GABARITO DNA  (ácido dexoxirribonucleico) COMO PODEMOS COLOCAR ISSO ??

    def parte_5(self):
        from anastasia.main import Swap
        self.laboratorio_5=Cena(img=LABORATORIO_5)
        self.laboratorio_5.vai()
        Swap(JOGO,ENIGMA,self.laboratorio_5, x=50, y=50, w=500,h=500)
        

if __name__ == "__main__":
    Fase3()
