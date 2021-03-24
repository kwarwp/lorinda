# lorinda.anastasia.main.py
from _spy.vitollino.main import Jogo, STYLE
from browser.timer import set_interval
STYLE.update(width=1350, height="600px")
J = Jogo()

class Associa:
    CENA ="https://i.imgur.com/AD1wScZ.jpg"
    CELULA = "https://i.imgur.com/tcCj6nw.png"
    VAZIO = "https://i.imgur.com/2moCwSz.png"
    VAZIO = "https://i.imgur.com/npb9Oej.png"
    class Nome:

        def __init__(self, cena):
            self.nome = J.a(Associa.VAZIO, x=400, y=50, w=120, h=30, o=0.9, style={"font-size":"30px"}, cena=cena)
            self.nome.elt.html = "&nbsp;&nbsp;mitocôndria"

    
    def __init__(self, j):
        self.cena = J.c(self.CENA)
        self.celula = J.a(self.CELULA, x=300, y=50, w=600, h=500, cena=self.cena)
        self.mito = self.Nome(self.cena)
        self.cena.vai()

def main():
    Associa(j = Jogo())
    
main()