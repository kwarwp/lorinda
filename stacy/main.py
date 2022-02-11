# lorinda.stacy.main.py
from _spy.vitollino.main import Cena,Elemento,Texto, Sala, Labirinto, STYLE
from _spy.vitollino.main import Inventario as inv
STYLE.update(width=1000, height="600px")
MARIA = "https://i.imgur.com/FukdPW2.jpg"

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
        Elemento("https://i.imgur.com/YfSoVKE.png", x= 400, y=200, w=200, h=300, cena =sala_a.oeste)
        Elemento("https://i.imgur.com/YKNLls2.png", x= 600, y=200, w=200, h=300, cena =sala_a.oeste)
        Elemento(MARIA, x= 800, y=200, w=200, h=300, cena =sala_a.oeste)
        Elemento("https://i.imgur.com/EDgO8xF.png", x= 600, w=300, cena =sala_a.oeste)
        #Elemento("https://i.imgur.com/cTgMqWX.png", cena =sala_b.norte)
        Elemento("https://i.imgur.com/YKNLls2.png", x= 500, y=200, w=200, h=300, cena =sala_a.norte)
        Elemento(MARIA, x= 800, y=200, w=200, h=300, cena =sala_a.norte)
        sala_a.norte.vai()
        Elemento("https://i.imgur.com/h6fl6wy.png", x= 600, w=300, cena =sala_a.norte)


    
if __name__ == "__main__":
    Reticulo()
