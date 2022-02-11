# lorinda.stacy.main.py
from _spy.vitollino.main import Cena,Elemento,Texto, Sala, Labirinto, STYLE
from _spy.vitollino.main import Inventario as inv
STYLE.update(width=1000, height="600px")
MARIA = "https://i.imgur.com/FukdPW2.jpg"
PROTEINA ="https://i.imgur.com/YKNLls2.png"
#GLICOSE = "https://i.imgur.com/YfSoVKE.png"
GLICOSE = "https://i.imgur.com/tGnLire.png"
CARBOIDRATO = "https://i.imgur.com/YfSoVKE.png"
CALCIO = "https://i.imgur.com/HtPw2D3.png"
MONTAGEM = "https://i.imgur.com/EObSdyR.png"
METACARBOIDRATO = "https://i.imgur.com/7C2PCQG.png"
SINLIPIDEO = "https://i.imgur.com/7sjUw3S.png"
FOSFOLIPIDEO = "https://i.imgur.com/UanOQDK.png"
LIPIDEO = "https://i.imgur.com/0LgQIIA.png"
IONSCALCIO = "https://i.imgur.com/PXkUsU4.png"
TOXICO = "https://i.imgur.com/qJfC3K0.png"

RETICULO = ["xMzJZEC wYdLfWl kVrzia6 6IHDCU9".split(), "V961vkS bo5bxUQ ySe17QP lv1Ga2i".split()]
IM = "https://i.imgur.com/{}.jpg"

class Reticulo:
    def __init__(self, *_):
        self.vai_reticulo()
    def vai_reticulo(self):
        sala_a = Sala(*[IM.format(lnk) for lnk in RETICULO[0]])
        sala_b_args = [IM.format(lnk) for lnk in RETICULO[1]]
        sala_b = Sala(*sala_b_args)
        lab0 = Labirinto(sala_a, sala_b, sala_b, sala_b, sala_b)
        lab1 = Labirinto(sala_b, sala_a, sala_a, sala_a, sala_a)
        self.oeste()
        self.norte()
        self.leste()
        self.sul()
        self.boeste()
        self.bnorte()
        self.bleste()
        self.bsul()
        sala_a.norte.vai()
    def oeste(self):
        Elemento(PROTEINA, x= 300, y=200, w=200, h=300, cena =sala_a.oeste)
        Elemento(GLICOSE, x= 500, y=200, w=200, h=300, cena =sala_a.oeste)
        Elemento(MARIA, x= 700, y=200, w=200, h=300, cena =sala_a.oeste)
        Elemento("https://i.imgur.com/EDgO8xF.png", x= 600, w=300, cena =sala_a.oeste)
        #Elemento("https://i.imgur.com/cTgMqWX.png", cena =sala_b.norte)
    def norte(self):
        Elemento(PROTEINA, x= 400, y=200, w=200, h=300, cena =sala_a.norte)
        Elemento(MARIA, x= 700, y=200, w=200, h=300, cena =sala_a.norte)
        Elemento("https://i.imgur.com/h6fl6wy.png", x= 600, w=300, cena =sala_a.norte)
    def leste(self):
        Elemento(PROTEINA, x= 400, y=200, w=200, h=300, cena =sala_a.leste)
        Elemento(MARIA, x= 700, y=200, w=200, h=300, cena =sala_a.leste)
        Elemento(MONTAGEM, x= 600, w=300, cena =sala_a.leste)
    def sul(self):
        Elemento(LIPIDEO, x= 400, y=200, w=200, h=300, cena =sala_a.sul)
        Elemento(MARIA, x= 700, y=200, w=200, h=300, cena =sala_a.sul)
        Elemento(FOSFOLIPIDEO, x= 600, w=300, cena =sala_a.sul)
    def boeste(self):
        Elemento(PROTEINA, x= 300, y=200, w=200, h=300, cena =sala_b.oeste)
        Elemento(GLICOSE, x= 500, y=200, w=200, h=300, cena =sala_b.oeste)
        Elemento(MARIA, x= 700, y=200, w=200, h=300, cena =sala_b.oeste)
        Elemento(TOXICO, x= 600, w=300, cena =sala_b.oeste)
        #Elemento("https://i.imgur.com/cTgMqWX.png", cena =sala_b.norte)
    def bnorte(self):
        Elemento(CALCIO, x= 400, y=200, w=200, h=300, cena =sala_b.norte)
        Elemento(MARIA, x= 700, y=200, w=200, h=300, cena =sala_b.norte)
        Elemento(IONSCALCIO, x= 600, w=300, cena =sala_b.norte)
    def bleste(self):
        Elemento(CARBOIDRATO, x= 400, y=200, w=200, h=300, cena =sala_b.leste)
        Elemento(MARIA, x= 700, y=200, w=200, h=300, cena =sala_b.leste)
        Elemento(METACARBOIDRATO, x= 600, w=300, cena =sala_b.leste)
    def bsul(self):
        Elemento(LIPIDEO, x= 400, y=200, w=200, h=300, cena =sala_b.sul)
        Elemento(MARIA, x= 700, y=200, w=200, h=300, cena =sala_b.sul)
        Elemento(SINLIPIDEO, x= 600, w=300, cena =sala_b.sul)


    
if __name__ == "__main__":
    Reticulo()
