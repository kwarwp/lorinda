# lorinda.danae.main.py
from _spy.vitollino.main import Cena, Sala, STYLE
STYLE.update(width=900, height="650px")
CENAS = "CkepkCR XXQmytH".split()
CENA = "https://i.imgur.com/%s.jpg"
PROP = "hB7FFDO"

class TheCave:
    def __init__(self):
        cena = Cena(CENA % CENAS)
        sala = Sala(*[CENA % parede for parede in CENAS]) 
        #cena.vai()
        sala.norte.vai()
        
        
if __name__ == "__main__":
    TheCave()