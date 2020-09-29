# lorinda.danae.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE.update(width=900, height="650px")
CENAS = "CkepkCR"
CENA = "https://i.imgur.com/%s.jpg"


class TheCave:
    def __init__(self):
        cena = Cena(CENA % CENAS)
        cena.vai()
        
        
if __name__ == "__main__":
    TheCave()