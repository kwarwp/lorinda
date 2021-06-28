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
        
    def mover(self, ev=None):
        self.movente.x=800
        
Move()