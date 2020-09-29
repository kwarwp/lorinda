# lorinda.danae.main.py
from _spy.vitollino.main import Cena, Sala, Labirinto, STYLE
STYLE.update(width=900, height="650px")
CENAS = "CkepkCR XXQmytH nnBZp4Y 1ZCmVlf".split()
INTER = "1ZCmVlf UGVhUV6"
SANCT = ""
CENA = "https://i.imgur.com/%s.jpg"
PROP = "hB7FFDO"

class TheCave:
    def __init__(self):
        cena = Cena(CENA % CENAS)
        
        sala = Sala(*[CENA % parede for parede in CENAS]) 
        atrio = Sala(*[CENA % parede for parede in INTER]) 
        sanct = Sala(*[CENA % parede for parede in SANCT]) 
        #cena.vai()
        cave = Labirinto(c=atrio,n=sanct, s=sala)
        sala.norte.vai()
        
        
if __name__ == "__main__":
    TheCave()