# lorinda.stacy.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
from _spy.vitollino.main import Inventario as inv

RETICULO = ["f1dGlgQ wYdLfWl kVrzia6 6IHDCU9".split(), "f1dGlgQ wYdLfWl kVrzia6 6IHDCU9".split()]
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
        sala_b.norte.vai()


    
if __name__ == "__main__":
    Reticulo()
