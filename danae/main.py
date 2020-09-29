# lorinda.danae.main.py
from _spy.vitollino.main import Cena, Sala, Labirinto, STYLE
STYLE.update(width=900, height="650px")
CENAS = "CkepkCR nnBZp4Y 1ZCmVlf W5Q3VcS".split()
INTER = "XXQmytH UGVhUV6 1ZCmVlf Ac7LD9Z".split()
SANCT = "5kwiit6 Bip0ltd jKNasd1"
CENA = "https://i.imgur.com/%s.jpg"
PROP = "hB7FFDO i2jZEzM".split()

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