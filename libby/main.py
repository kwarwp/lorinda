# lorinda.libby.main.
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv 
from anastasia.main import Associa, SF
from courtney.main import MOCHILA
SF.update({"font-size":"20px", "transition": "left 1s, top 1s"})
STYLE.update(width=1000, height="600px")
#bacteriaCerto
CELULA_1 = "https://i.imgur.com/eBUMZZE.png"
#protozoarioCERTO
CELULA_2 = "https://i.imgur.com/rjEEZ5R.png"
#vegetalCERTO
CELULA_3 = "https://img2.gratispng.com/20180602/bga/kisspng-plant-cell-cl-lula-eucariota-cl-lula-animal-animal-cell-5b1365ea94c884.3552609815279979306094.jpg"
#espermatozoide
CELULA_4 = "https://i.imgur.com/pHmxGpO.png" 
#espermatozoide
CELULA_5 = "https://i.imgur.com/ByzUX4t.jpg"
#nervosa neuronio
CELULA_6 = "https://static.biologianet.com/conteudo/images/os-neuronios-sao-constituidos-basicamente-por-um-corpo-celular-dendritos-axonio-5b3b696bc348e.jpg"
MOEDAS = "https://i.imgur.com/VfyiFmY.png"
CICLONE = "https://static.todamateria.com.br/upload/55/65/556506fa96eca-ciclone.jpg"
MEMBRANA = "https://i.imgur.com/RRqQzXR.jpg"
NPC = "https://i.imgur.com/pgk5Kk0.png"
A = ""
B = ""
C = ""
D = "" 
class Fase2():
    def __init__(self):
        #self.npc= Elemento(img= NPC)
        def some(ev):
            self.celula_1.x = -10000
        self.ciclone= Elemento(img= CICLONE)
        self.celula_1= Elemento(img= CELULA_1,x=450,y=50, vai=self.acertou)
        self.celula_1.elt.onclick = some  #Sair dessa sala e ir para a sala kelle, depois que acertar
        self.celula_2= Elemento(img= CELULA_2,x=750,y=50, vai=self.errou)
        self.celula_3= Elemento(img= CELULA_3,x=450,y=150, vai=self.errou)
        self.celula_4= Elemento(img= CELULA_4,x=750,y=150, vai=self.errou)
        self.celula_5= Elemento(img= CELULA_5,x=450,y=250, vai=self.errou)
        self.celula_6= Elemento(img= CELULA_6,x=750,y=250, vai=self.errou)
        self.membrana= Cena(img= MEMBRANA)
        self.membrana.vai()
        #self.jogo = Associa(self.membrana, caixa=300, borda=20, acertou=self.acertou, acertos=6)
        self.celula_1.entra(self.membrana)
        self.celula_2.entra(self.membrana)
        self.celula_3.entra(self.membrana)
        self.celula_4.entra(self.membrana)
        self.celula_5.entra(self.membrana)
        self.celula_6.entra(self.membrana)
        self.npc=Elemento(img=NPC, x=900,y=350)
        
        """self.jogo.nome(nome="1-Meu núcleo é espalhado", tit=0, x=450, y=50)
        self.jogo.nome(nome="2-Citoplasma, membrana, núcleo", tit=1, x=750, y=50)
        self.jogo.nome(nome="3-Citoplasma, membrana, núcleo", tit=2, x=450, y=150)
        self.jogo.nome(nome="4-Citoplasma, membrana, núcleo", tit=3, x=850, y=150)
        self.jogo.nome(nome="5-Citoplasma, membrana, núcleo", tit=4, x=450, y=250)
        self.jogo.nome(nome="6-Citoplasma, membrana, núcleo", tit=5, x=750, y=250)
        self.jogo.nome(nome= "Para sair desse mundo você precisa achar o protozoário",tit=6,x=1000,y=350)# como fazer para aparecer tudo ?"""
    
    def acertou(self):
        Texto(self.membrana, "Você acertou tudo! Parabéns! Você ganhou cinco ATP, veja sua mochila",
        foi=MOCHILA.mostra_mochila).vai()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()

    def errou(self):
        Texto(self.membrana, "poxa , não sou  , pois eu tenho Citoplasma, membrana, núcleo ").vai()
       
        #self.npc.entra(self.celula,Tit = "Observe atentamente essas imagens e coloque as letras correspondentes."
        #"Cada imagem terá apenas três letras, arraste para a área correspondente da célula")    #não temos ainda a imagem da célula
        #self.npc.entra(self.membrana,Tit = "Você precisa de moedas de ATP para sair dessa dimenção, para isso, precisamos excluir a célula procarionte")
        
"""class celulas():
    def __init__(self):
        self.a= Elemento(img= A)
        self.b= Elemento(img= B)
        self.c= Elemento(img= C)
        self.d= Elemento(img= D)
        self.celula_1.entra(self.celula,x=50,y=50,z=50)
        self.celula_2.entra(self.celula,x=60,y=60,z=60)
        self.celula_3.entra(self.celula,x=70,y=70,z=70)
        self.celula_4.entra(self.celula,x=80,y=80,z=80)
        self.celula_5.entra(self.celula,x=90,y=90,z=90)
        self.celula_6.entra(self.celula,x=100,y=100,z=100)
        self.a.entra(self.celula,x=200,y=50,z=50,Tit= "Eu sou a membrana plasmatica")
        self.b.entra(self.celula,x=250,y=60,z=60,Tit= "Eu sou um citoplasma")
        self.c.entra(self.celula,x=300,y=70,z=70,Tit= "Eu sou o nucleo")
        self.d.entra(self.celula,x=350,y=80,z=80,Tit= "Eu sou o material do nucleo espalhado no citoplasma")
    
    """
    
if __name__ == "__main__":
    Fase2()
    
    