# lorinda.danae.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE.update(width=900, height="650px")
CENA = "https://i.imgur.com/CkepkCR.jpg"


class TheCave:
    def __init__(self):
        cena = Cena(CENA)
        cena.vai()
        
        
if __name__ == "__main__":
    TheCave()