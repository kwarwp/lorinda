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
from collections import namedtuple
"""Usa o timer do navegador para dar um tempinho inicial"""
Rosa = namedtuple("Rosa", "norte leste sul oeste")
STYLE.update(width=1350, height="600px")
SF = {"transition": "left 3s, top 3s"}
J = Jogo()
"""Usa o recurso novo do Vitollino Jogo. Jogo.c é Cena, Jogo.a é Elemento, Jogo.n é Texto"""
SF = {"font-size":"30px", "transition": "left 1s, top 1s"}
"""Dá o tamanho da letra da legenda e faz a legenda se movimentar suavemente quando inicia e acerta"""
VAZIO = "https://i.imgur.com/npb9Oej.png"
BORDA = "https://i.imgur.com/npb9Oej.png"
KNOB  = "https://i.imgur.com/v8Lqqpt.png"
ROSA = Rosa((0, -1), (1, 0), (0, 1), (-1, 0))
CIS = {ROSA.norte: ROSA.leste, ROSA.leste: ROSA.norte, ROSA.sul: ROSA.oeste, ROSA.oeste: ROSA.sul}
TRS = {ROSA.norte: ROSA.oeste, ROSA.leste: ROSA.sul, ROSA.sul: ROSA.leste, ROSA.oeste: ROSA.norte}
SWP = {0: CIS, 90:TRS}
GAP = 60

class Droner:
    """ Jogo que direciona drones para atingir alvos
    """
    CENA ="https://i.imgur.com/AD1wScZ.jpg"
    CELULA = "https://i.imgur.com/tcCj6nw.png"
    DRONE = "https://i.imgur.com/XDuFNZw.png"
    KNOBS = 30
    def __init__(self, cena):

        class Drone(J.a):
            """ Um drone que desvia para esquerda ou direita ao chocar com o anteparo

            As legendas aparecem inicialmente no local certo e depois de um intervalo vão para o canto esquerdo

            :param    x: a posição horizontal do anteparo
            :param    y: a posição vertical do anteparo
            :param jogo: o jogo que este anteparo aparece
            :param cena: a cena onde o anteparo aparece
            :param img: imagem de fundo do anteparo
            """
            def __init__(self, index, cena, jogo, img=self.DRONE):
                pw = ph = Droner.KNOBS
                print ("Drone.__init__", index, cena, jogo, img)

        class Anteparo(J.a):
            """ Um bloqueio que desvia o drone para esquerda ou direita

            Qualquer anteparo clicado gira todos os anteparos, mudando de esqurda para direita e vice-versa.

            :param    x: a posição horizontal do anteparo
            :param    y: a posição vertical do anteparo
            :param jogo: o jogo que este anteparo aparece
            :param cena: a cena onde o anteparo aparece
            :param img: imagem de fundo do anteparo
            """
            def __init__(self, x, y, cena, jogo, img=KNOB):
                pw = ph = Droner.KNOBS*2
                self.jogo = jogo
                super().__init__(img, x=x, y=y, w=pw, h=ph, cena=cena)
                self.elt.onclick = self.rodar
                self.rotate = self.jogo.rotate

            def rodar(self, ev=None, nome=None):
                """Quando o jogador clica, gira os anteparos"""
                self.jogo.rotate = self.rotate = (self.rotate+90) % 180
                self.jogo.rodar(self.rotate)
                self.elt.style.transform = f"rotate({self.rotate}deg)"

            def localiza(self):
                """retorna a posição do anteparo corrente e o azimuth indicado para drone"""
                return self.x, self.y, None

            def roda(self, rodado=0):
                """Gira o anteparo para a rotação dada"""
                self.rotate = rodado
                self.elt.style.transform = f"rotate({self.rotate}deg)"
                
        class Borda(Anteparo):
            """ Um bloqueio que para o drone e o relocaliza para uma outra borda aleatória.

            Qualquer anteparo clicado gira todos os anteparos, mudando de esqurda para direita e vice-versa.

            :param    x: a posição horizontal do anteparo
            :param    y: a posição vertical do anteparo
            :param jogo: o jogo que este anteparo aparece
            :param cena: a cena onde o anteparo aparece
            :param img: imagem de fundo do anteparo
            """
            def __init__(self, x, y, cena, jogo):
                super().__init__(x=x, y=y, jogo=jogo, cena=cena, img=BORDA)
            def rodar(self, ev=None, nome=None):
                pass
            def roda(self, rodado=0):
                pass

            def localiza(self):
                """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
                from random import choice, randint
                x, y = randint(1,10), randint(1,4)
                ax, ay = azimuth = choice(list(ROSA))
                cx, cy = [0, x, 10][ax+1], [0, y, 5][ay+1]
                print("localiza", cx, cy, azimuth)
                return cx, cy, azimuth

        class Drone_(J.a):
            """ Um drone que desvia para esquerda ou direita ao chocar com o anteparo

            As legendas aparecem inicialmente no local certo e depois de um intervalo vão para o canto esquerdo

            :param    x: a posição horizontal do anteparo
            :param    y: a posição vertical do anteparo
            :param jogo: o jogo que este anteparo aparece
            :param cena: a cena onde o anteparo aparece
            :param img: imagem de fundo do anteparo
            """
            def __init__(self, index, cena, jogo, img=self.DRONE):
                pw = ph = Droner.KNOBS
                print ("Drone.__init__", index, cena, jogo, img)
                self.jogo = jogo
                x, y, _ = self.jogo.localiza(index)
                print ("Drone.__init__", x, y, _)
                x, y, _ = [(coor + GAP//4) if isinstance(int,coor) else coor for coor in self.jogo.localiza(index)]
                print (x, y, _)
                super().__init__(img, x=x, y=y, w=pw, h=ph, style=SF, cena=cena)
                # self.elt.style.transition = "left 1s top 1s"
                self.elt.ontransitionend = self.rodar
                self.rotate = 0
                self.azimuth = ROSA.oeste
                self.index = index

            def rodar(self, ev=None, nome=None):
                """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
                dx, dy = self.azimuth = SWP[self.jogo.rotate][self.azimuth]
                print(" end", self.x, self.y, dx, dy, self.azimuth)
                self.x, self.y, az = [(coor + GAP//4) if isinstance(int,coor) else coor for coor in self.jogo.localiza(index)]
                self.azimuth = az or self.azimuth

            def inicia(self, ev=None, nome=None):
                """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
                dx, dy = self.azimuth
                #self.x = self.x + dx*GAP*2
                #self.y = self.y + dy*GAP*2
                self.x, self.y, _ = [(coor + GAP//4) if isinstance(int,coor) else coor for coor in self.jogo.localiza(index)]

    
        self.cena = cena
        self.rotate = 0
        self.w = 11
        # Anteparo(200, 75, cena, self)
        self.anteparos = [self.cria(index) for index in range(self.w*6)]
        #self.drone = Drone(int(1.25*GAP), int(1.75*GAP), cena, self)
        self.drone = Drone(self.w, cena, self)
        #set_timeout(self.inicia, "1000")
        
    def cria(self, index):
        w = self.w
        x, y = (index%w), (index//w)
        good = 0 < x < 10 and 0 < y < 5
        x, y = GAP+2*GAP*x, int(-0.5*GAP)+2*GAP*y
        return Anteparo(x, y, cena, self) if good else Borda(x, y, cena, self) 
        
    def inicia(self, _=0):
        self.drone.inicia()
        
    def localiza(self, index, dx=0, dy=0):
        index = index + dx + self.w*dy
        print("localiza", index)
        return self.anteparos[index].localiza()
        
    def rodar(self, rodado=0):
        """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
        self.rotate = rodado
        [anteparo.roda(rodado) for anteparo in self.anteparos]
        

def main():
    # Associa()
    cena = J.c(Droner.CENA)
    Droner(cena)
    cena.vai()
    
main()