# lorinda.courtney.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE.update(width=600, height="600px")

class Mochila:
    MOCHILA = "https://i.imgur.com/N8eUQ2S.png"
    ATP = "https://i.imgur.com/k0Az1Ts.png"
    def __init__(self):
        self.mochila = Cena(self.MOCHILA)
        self.mochila.vai()
        self.atp = Elemento(self.ATP, cena=self.mochila)
        
        
if __name__ == "__main__":
    Mochila()