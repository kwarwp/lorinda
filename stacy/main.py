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
        Elemento(PROTEINA, tit="PROTEÍNA", x= 300, y=200, w=200, h=300, cena =sala_a.oeste,
        texto="Aqui no rugoso também fazemos a glicosilação das proteínas, isto é vamos inserir glicose na molécula de proteína")
        Elemento(GLICOSE, tit="GLICOSE", x= 500, y=200, w=200, h=300, cena =sala_a.oeste,
        texto="pois é eu sou a glicose que vai ser usada para clicolisar a molécula de proteína")
        Elemento(MARIA, tit="MARIA", x= 700, y=200, w=200, h=300, cena =sala_a.oeste,
        texto="Glicolizar, que coisa complicada!")
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
        Elemento(PROTEINA, tit="PROTEÍNA POLIPEPTíDIO", x= 400, y=200, w=200, h=300, cena =sala_a.leste,
        texto="Aqui no retículo rugoso se faz a montagem de proteínas compridas, formando cadeias polipeptídicas, em especial as que vão sair da célula")
        Elemento(MARIA, tit="MARIA", x= 700, y=200, w=200, h=300, cena =sala_a.leste,
        texto="Certo, as proteínas montadas que vão sair da célula serão enviadas para o complexo de Golgi para empacotamento")
        Elemento(MONTAGEM, x= 600, w=300, cena =sala_a.leste)
    def sul(self):
        Elemento(LIPIDEO, tit="FOSFOLIPIDIO", x= 400, y=200, w=200, h=300, cena =sala_a.sul,
        texto="Oi gente eu sou um lipído, mais precisamente um fosfolipídio, essencial para construção da membrana celular")
        Elemento(MARIA, tit="MARIA", x= 700, y=200, w=200, h=300, cena =sala_a.sul,
        texto="Muito útil este retículo endoplasmático, os lipídios são os blocos de construção das estruturas celulares")
        Elemento(FOSFOLIPIDEO, x= 600, w=300, cena =sala_a.sul)
    def boeste(self):
        Elemento(ALCOOL, tit="ALCOOL", x= 300, y=200, w=200, h=300, cena =sala_b.oeste,
        texto="Hic! Acho que bebi demais! Hic!'")
        Elemento(ENZIMA, tit="ENZIMA", x= 500, y=200, w=200, h=300, cena =sala_b.oeste,
        texto="Eu sou a enzima desidrogenaze. Aqui no retículo liso eu vou desintoxicar o organismo quebrando as substâncias tóxicas")
        Elemento(MARIA, tit="MARIA", x= 700, y=200, w=200, h=300, cena =sala_b.oeste,
        texto="As pessoas não deveriam exagerar na bebida, vai ter que ter muito retículo liso para o detox!")
        Elemento(TOXICO, x= 600, w=300, cena =sala_b.oeste)
        #Elemento("https://i.imgur.com/cTgMqWX.png", cena =sala_b.norte)
    def bnorte(self):
        Elemento(CALCIO, tit="CALCIO", x= 400, y=200, w=200, h=300, cena =sala_b.norte,
        texto="Oi gente sou o Cálcio, eu ajudo na contração muscular e sou armazenado aqui no retículo endoplasmático liso")
        Elemento(MARIA, tit="MARIA", x= 700, y=200, w=200, h=300, cena =sala_b.norte,
        texto="É por isso que o retículo liso tem forma de tubos, serve para guardar coisas!")
        Elemento(IONSCALCIO, x= 600, w=300, cena =sala_b.norte)
    def bleste(self):
        Elemento(CARBOIDRATO, tit="CARBOIDRATO", x= 400, y=200, w=200, h=300, cena =sala_b.leste,
        texto="Aqui no retículo liso vai acontecer a minha metabolização, eu que sou o carboidrato")
        Elemento(GLICOSE, tit="GLICOSE", x= 500, y=200, w=200, h=300, cena =sala_a.oeste,
        texto="Eu sou a glicose resultante da metabolização do carboidrato")
        Elemento(MARIA, tit="MARIA", x= 700, y=200, w=200, h=300, cena =sala_b.leste,
        texto="O retículo liso é fundamental na formação de glicose por meio da hidrólise do glicogênio.")
        Elemento(METACARBOIDRATO, x= 600, w=300, cena =sala_b.leste)
    def bsul(self):
        Elemento(LIPIDEO, tit="LIPIDIO", x= 400, y=200, w=200, h=300, cena =sala_b.sul,
        texto="Oi gente eu sou um lipído, e seu produzido aqui no retículo endoplasmático liso")
        Elemento(MARIA, tit="MARIA", x= 700, y=200, w=200, h=300, cena =sala_b.sul,
        texto="Aqui no retículo liso, temos a síntese dos lipídios e também alguns hormônios")
        Elemento(SINLIPIDEO, x= 600, w=300, cena =sala_b.sul)


    
if __name__ == "__main__":
    Reticulo()
