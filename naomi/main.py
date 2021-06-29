# lorinda.naomi.main.py
from _spy.vitollino.main import Cena, Elemento,Texto, STYLE
STYLE.update(width=1000, height="600px")

class Move:
    def __init__(self):
        PROTEINA = "https://i.imgur.com/slnDrGI.png"
        self.parede = Cena("https://i.imgur.com/sGoKfvs.jpg")
        self.parede.vai()
        self.movente = Elemento(img=PROTEINA, cena=self.parede,
            style={"transition": "left 2s"})
        Texto(self.parede, "veja a proteina chegar na parede", foi=self.mover).vai()
        self.pergunta()
        self.acabou = 2
    def pergunta(self, ev=None):
        if self.acabou:
            return
        self.acabou -= 1
        self.multi = Texto(self.parede, "processos corretos?",
                           foi=self.resposta, A= "a b", B= "b c", C= "c d", D= "b d").vai()

    def mover(self, ev=None):
        self.movente.x=800
        
    def resposta(self, rep):
        if rep == "A":
            Texto(self.parede, "ganhou um ATP!").vai()
        else:
            Texto(self.parede, "Ops não acertou", foi=self.pergunta).vai()
            
            
        
Move()