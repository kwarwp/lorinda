# lorinda.danae.main.py
from _spy.vitollino.main import Cena, Sala, Labirinto, Elemento, Texto, STYLE
STYLE.update(width=900, height="650px")
CENAS = "CkepkCR nnBZp4Y 1ZCmVlf W5Q3VcS".split()
INTER = "XXQmytH UGVhUV6 dIPsMeh bi4tHyr".split()  #
SANCT = "5kwiit6 Bip0ltd jKNasd1 Ac7LD9Z".split()
CENA = "https://i.imgur.com/%s.jpg"
CAPEL = "XJTHqUW iiiorD4".split()
PROP = "S2td4Uk i2jZEzM WwNrwlJ u1bDkus cEJbS0C".split()  # hB7FFDO RO0oeZI
MPROP = "Fxc4cCK 4yxhrO0".split()
JEROM = "https://i.imgur.com/IGFstQy.png"
SONHO = "https://i.imgur.com/uHw57i1.jpg"
MARCA = "https://i.imgur.com/2moCwSz.png"
class TheCave:
    def __init__(self):
        cena = Cena(CENA % CENAS)
        self.jero, self.placa, self.cruz , self.grego , self.vulgata = [
            CENA % obj for obj in PROP]
        self.pano, self.livro = [
            CENA % obj for obj in MPROP]
        
        self.capel = capel = [Cena(CENA % parede) for parede in CAPEL]
        self.sala = sala = Sala(*[CENA % parede for parede in CENAS]) 
        self.atrio = atrio = Sala(*[CENA % parede for parede in INTER]) 
        sanct = Sala(*[CENA % parede for parede in SANCT]) 
        #cena.vai()
        cave = Labirinto(c=atrio,n=sanct, s=sala)
        # capel[0].meio = capel[1]
        capel[0].meio = Cena(vai=self.sao_jeronimo)
        capel[1].meio = capel[1].esquerda = capel[1].direita = sala.norte
        capel[0].vai()
        #atrio.leste.vai()
        #sanct.leste.vai()
        self.e_placa = Elemento(self.placa, x=510, y=210, w=280, cena=atrio.leste)
        self.e_jero = Elemento(self.jero, x=360, y=214, w=147, h=250, cena=sanct.leste)
        self.e_jero = Elemento(self.pano, x=360, y=212, w=150, h=250, cena=sanct.leste)
        self.e_jerom = Elemento(JEROM, x=0, y=400, w=150, h=250, cena=sanct.leste)
        self.e_vecruz = Elemento(MARCA, x=480, y=100, w=150, h=250, o=0.1, cena=capel[0],
            vai= self.sao_jeronimo)
        self.e_vecruz.o = 0.2
        
    def sao_jeronimo(self, *_):
        self.capel[1].vai()
        self.e_vecruz.x = 800
        busca = Texto(self.capel[1], "Visite a gruta e toque em um crucifixo iluminado",
            foi=lambda *_: self.e_vecruz.entra(self.sala.sul))
        fala = Texto(self.capel[1], "Que bom você me visitar, aprenda meu caminho para santidade", foi=busca.vai)
        self.e_jerom.vai = fala.vai
        visao = Texto(self.capel[1], "Você se ajoelha e faz uma oração, São Jerônimo aparece numa visão",
        foi=lambda *_: self.e_jerom.entra(self.capel[1]))
        Texto(self.capel[1], "Você veio conhecer a gruta onde São Jerônimo traduziu a Bíblia", foi=visao.vai).vai()
        
        
if __name__ == "__main__":
    TheCave()