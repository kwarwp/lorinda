# lorinda.danae.main.py
from _spy.vitollino.main import Cena, Sala, Labirinto, STYLE
STYLE.update(width=900, height="650px")
CENAS = "CkepkCR nnBZp4Y 1ZCmVlf W5Q3VcS".split()
INTER = "XXQmytH UGVhUV6 1ZCmVlf bi4tHyr".split()
SANCT = "5kwiit6 Bip0ltd jKNasd1 Ac7LD9Z".split()
CENA = "https://i.imgur.com/%s.jpg"
CAPEL = "XJTHqUW iiiorD4".split()
PROP = "hB7FFDO i2jZEzM WwNrwlJ u1bDkus cEJbS0C 4yxhrO0".split()

class TheCave:
    def __init__(self):
        cena = Cena(CENA % CENAS)
        self.jero, self.placa, self.cruz , self.grego , self.vulgata , self.livro = [
            CENA % obj for obj in PROP]
        
        capel = [Cena(CENA % parede) for parede in CAPEL]
        sala = Sala(*[CENA % parede for parede in CENAS]) 
        atrio = Sala(*[CENA % parede for parede in INTER]) 
        sanct = Sala(*[CENA % parede for parede in SANCT]) 
        #cena.vai()
        cave = Labirinto(c=atrio,n=sanct, s=sala)
        capel[0].meio = capel[1]
        capel[1].meio = capel[1].esquerda = capel[1].direita = sala.norte
        capel[0].vai()
        self.e_placa = Elemento(self.placa, cena=sanct.leste)
        
        
if __name__ == "__main__":
    TheCave()