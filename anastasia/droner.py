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
SF = {"transition": "left 8s, top 8s"}
J = Jogo()
"""Usa o recurso novo do Vitollino Jogo. Jogo.c é Cena, Jogo.a é Elemento, Jogo.n é Texto"""
SF = {"font-size":"10px", "transition": "left 5s, top 5s"}
"""Dá o tamanho da letra da legenda e faz a legenda se movimentar suavemente quando inicia e acerta"""
VAZIO = "https://i.imgur.com/npb9Oej.png"
BORDA = "https://i.imgur.com/npb9Oej.png"
KNOB  = "https://i.imgur.com/v8Lqqpt.png"
ROSA = Rosa((0, -1), (1, 0), (0, 1), (-1, 0))
CIS = {ROSA.norte: ROSA.leste, ROSA.leste: ROSA.norte, ROSA.sul: ROSA.oeste, ROSA.oeste: ROSA.sul}
TRS = {ROSA.norte: ROSA.oeste, ROSA.leste: ROSA.sul, ROSA.sul: ROSA.leste, ROSA.oeste: ROSA.norte}
SWP = {0: CIS, 90:TRS}
GAP = 60

class A:
    def __init__(self, *args):
        pass

class Droner:
    """ Jogo que direciona drones para atingir alvos
    """
    CENA ="https://i.imgur.com/AD1wScZ.jpg"
    CELULA = "https://i.imgur.com/tcCj6nw.png"
    DRONE = "https://i.imgur.com/ZfrJcyE.jpg"  # https://i.imgur.com/XDuFNZw.png"
    KNOBS = 30
    def __init__(self, cena):

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
                self.index = x + y * 11
                x, y = GAP+2*GAP*x, int(-0.5*GAP)+2*GAP*y

                super().__init__(img, x=x, y=y, w=pw, h=ph, cena=cena)
                self.elt.onclick = self.rodar
                # self.elt.html = f"{x};{y}"
                self.rotate = self.jogo.rotate

            def rodar(self, ev=None, nome=None):
                """Quando o jogador clica, gira os anteparos"""
                self.jogo.rotate = self.rotate = (self.rotate+90) % 180
                self.jogo.rodar(self.rotate)
                self.elt.style.transform = f"rotate({self.rotate}deg)"

            def localiza(self):
                """retorna a posição do anteparo corrente e o azimuth indicado para drone"""
                return self.index, self.x, self.y, None

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
                ax, ay = azimuth = (0, 1) #choice(list(ROSA))
                cx, cy = [10, x, 0][ax+1], [0, y, 5][ay+1]
                cy = 0
                index = cx + cy*11
                cx, cy = GAP+2*GAP*cx, int(-0.5*GAP)+2*GAP*cy

                # print("localiza", cx, cy, azimuth)
                self.elt.html = f"{ax};{ay}|{cx}:{cy}"
                #self.jogo.start()
                self.jogo.drone.seguir()
                return index, cx, cy, azimuth

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
                #print ("Drone.__init__", index, cena, jogo, img)
                self.jogo = jogo
                self.index, x, y = 0, 0, 0 #self.jogo.localiza(index)
                #print ("Drone.__init__", self.index,x, y, azimuth)
                # x, y, _ = [(coor + GAP//4) if isinstance(int,coor) else coor for coor in self.jogo.localiza(index)]
                x, y = [(coor + GAP//4)  for coor in (x, y)]
                #print (x, y, _)
                super().__init__(img, x=x, y=y, w=pw, h=ph, style=SF, cena=cena)
                # self.elt.style.transition = "left 1s top 1s"
                self.elt.ontransitionend = self.rodar
                self.rotate = 0
                self.azimuth = ROSA.oeste
                self.roda = self._rodar
                # self.index = index

            def rodar(self, ev=None):
                """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
                self.roda()
                # print(" end", self.x, self.y, dx, dy, self.azimuth)
                #  self.x, self.y, az = [(coor + GAP//4) if isinstance(int,coor) else coor for coor in self.jogo.localiza(index)]
                # self.azimuth = az or self.azimuth

            def _rodar(self):
                """Quando o drone esbarra em um anteparo muda sua direção"""
                azimuth = SWP[self.jogo.rotate][self.azimuth]
                self.inicia(az=azimuth)
                # print(" end", self.x, self.y, dx, dy, self.azimuth)
                #  self.x, self.y, az = [(coor + GAP//4) if isinstance(int,coor) else coor for coor in self.jogo.localiza(index)]
                # self.azimuth = az or self.azimuth

            def seguir(self):
                """Quando o drone bate na borda ele segue o azimuth sorteado"""
                self.roda = self._seguir

            def _seguir(self):
                """Quando o drone bate na borda ele segue o azimuth sorteado"""
                self.inicia()
                self.roda = self._rodar
                # print(" end", self.x, self.y, dx, dy, self.azimuth)
                #  self.x, self.y, az = [(coor + GAP//4) if isinstance(int,coor) else coor for coor in self.jogo.localiza(index)]
                # self.azimuth = az or self.azimuth

            def inicia(self, ev=None, az=None):
                """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
                self.o = 1
                dx, dy = az or self.azimuth
                self.index, x, y, azn = self.jogo.localiza(self.index, dx, dy)
                # = self.index + dx + dy*11
                #self.x = self.x + dx*GAP*2
                #self.y = self.y + dy*GAP*2
                self.x, self.y = [(coor + GAP//4) for coor in (x, y)]
                self.azimuth = azn or az or self.azimuth
                self.elt.html = f">{self.index}|{self.azimuth}"

    
        self.cena = cena
        self.rotate = 0
        self.w = 11
        # Anteparo(200, 75, cena, self)
        self.drone = Drone(0, cena, self)
        self.anteparos = [self.cria(index) for index in range(self.w*6)]
        #self.drone = Drone(int(1.25*GAP), int(1.75*GAP), cena, self)
        #self.drone = Dro(self.w, cena, self)
        self.start()
        
    def start(self):
        self.drone.o = 0.3
        set_timeout(self.inicia, "1000")
        pass

        
    def cria(self, index):
        w, cena = self.w, self.cena
        x, y = (index%w), (index//w)
        good = 0 < x < 10 and 0 < y < 5
        return Anteparo(x, y, cena, self) if good else Borda(x, y, cena, self) 
        
    def inicia(self, _=0):
        self.drone.inicia()
        
    def localiza(self, index, dx=0, dy=0):
        index = index + dx + self.w*dy
        # print("localiza", index)
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