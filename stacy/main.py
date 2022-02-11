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
ENZIMA = "https://imgur.com/v3jd24d.png"
ALCOOL = "https://i.imgur.com/a3uJqr5.png"

RETICULO = ["xMzJZEC wYdLfWl kVrzia6 6IHDCU9".split(), "V961vkS bo5bxUQ ySe17QP lv1Ga2i".split()]
IM = "https://i.imgur.com/{}.jpg"


class Personagem(Elemento):
    def __init__(self, img=MARIA, tit='', x=300, y=400, w=180, h=200, afala="", responde=None, **kwargs):
        super().__init__(img=img, tit=tit, x=x, y=y, w=w, h=h, **kwargs)
        self.afala = afala
        self.responde = responde
        
    def fala(self, cena=None, responde=None, texto=""):
        Texto(self.cena, texto if texto else self.afala, foi=responde if responde else self.responde).vai()

class Reticulo:
    def __init__(self, *_):
        self.vai_reticulo()
    def vai_reticulo(self):
        self.sala_a = sala_a = Sala(*[IM.format(lnk) for lnk in RETICULO[0]])
        sala_b_args = [IM.format(lnk) for lnk in RETICULO[1]]
        self.sala_b = sala_b = Sala(*sala_b_args)
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
        def dica(*_):
            Texto(self.sala_a.norte, "depois de clicar nos dois personagens, vá para outra sala clicando na esquerda, direita ou topo").vai()
        Personagem(PROTEINA, tit="PROTEÍNA", x= 400, y=200, w=200, h=300, cena =sala_a.norte,
        texto="Aqui os ribossomas fabricam a mim, PROTEíNA, me despejando nesta parte do retículo rugoso")
        Personagem(MARIA, tit="MARIA", x= 700, y=200, w=200, h=300, cena =sala_a.norte, foi=dica,
        texto="Entendi, o retículo parece rugoso aqui pois está cheio destas bolinhas, os ribossomas")
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
        Elemento(ALCOOL, x= 300, y=200, w=200, h=300, cena =sala_b.oeste)
        Elemento(ENZIMA, x= 500, y=200, w=200, h=300, cena =sala_b.oeste)
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
