# lorinda.anastasia.droner.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo de direcionamento de drones.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    21.03
        Classe Droner.

"""
from _spy.vitollino.main import Jogo, STYLE
from browser.timer import set_timeout
"""Usa o timer do navegador para dar um tempinho inicial"""

STYLE.update(width=1350, height="600px")
J = Jogo()
"""Usa o recurso novo do Vitollino Jogo. Jogo.c é Cena, Jogo.a é Elemento, Jogo.n é Texto"""
SF = {"font-size":"30px", "transition": "left 1s, top 1s"}
"""Dá o tamanho da letra da legenda e faz a legenda se movimentar suavemente quando inicia e acerta"""
VAZIO = "https://i.imgur.com/npb9Oej.png"
KNOB  = "https://i.imgur.com/v8Lqqpt.png"

class Droner:
    """ Jogo que direciona drones para atingir alvos
    """
    CENA ="https://i.imgur.com/AD1wScZ.jpg"
    CELULA = "https://i.imgur.com/tcCj6nw.png"
    DRONE = "https://i.imgur.com/XDuFNZw.png"
    KNOBS = 50
    
    class Anteparo(J.a):
        """ Um bloqueio que desvia o drone para esquerda ou direita
        
        As legendas aparecem inicialmente no local certo e depois de um intervalo vão para o canto esquerdo
        
        :param    x: a posição horizontal do anteparo
        :param    y: a posição vertical do anteparo
        :param jogo: o jogo que este anteparo aparece
        :param cena: a cena onde o anteparo aparece
        :param img: imagem de fundo do anteparo
        """
        def __init__(self, x, y, cena, jogo, img=KNOB):
            pw = ph = Droner.KNOBS
            super().__init__(img, x=x, y=y, w=pw, h=ph, cena=cena)
            self.elt.onclick = self.rodar
            self.rotate = 0
            
        def rodar(self, ev=None, nome=None):
            """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
            self.rotate = (self.rotate+90) % 180
            self.elt.style.transform = f"rotate({self.rotate}deg)"

    
    def __init__(self, cena):
        self.cena = cena
        Droner.Anteparo(100, 100, cena, self)
        

def main():
    # Associa()
    cena = J.c(Droner.CENA)
    Droner(cena)
    cena.vai()
    
main()