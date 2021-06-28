# lorinda.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE.update(width=1000, height="600px")

class Move:
    def __init__(self):
        self.cena = Cena("https://i.imgur.com/sGoKfvs.jpg")
        self.cena.vai()
        self.movente = Elemento("https://i.imgur.com/slnDrGI.png", cena=self.cena,
            vai=self.mover, style={"transition": "left 2s"})
        
    def mover(self, ev=None):
        self.movente.x=800
        
Move()