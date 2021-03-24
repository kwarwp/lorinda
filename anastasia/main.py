# lorinda.anastasia.main.py
from _spy.vitollino.main import Jogo, STYLE
from browser.timer import set_timeout
STYLE.update(width=1350, height="600px")
J = Jogo()
"""Usa o recurso novo do Vitollino Jogo. Jogo.c é Cena, Jogo.a é Elemento, Jogo.n é Texto"""
SF = {"font-size":"30px", "transition": "left 1s, top 1s"}
"""Dá o tamanho da letra da legenda e faz a legenda se movimentar suavemente quando inicia e acerta"""
VAZIO = "https://i.imgur.com/npb9Oej.png"

class Associa:
    """ Jogo que associa o nome de um objeto com o seu desenho
    """
    CENA ="https://i.imgur.com/AD1wScZ.jpg"
    CELULA = "https://i.imgur.com/tcCj6nw.png"
    
    class Nome:
        """ Cria uma legenda a ser arrastada para a lacuna correta
        
        As legendas aparecem inicialmente no local certo e depois de um intervalo vão para o canto esquerdo
        
        :param nome: o nome que aparece na legenda
        :param  tit: a posição que a legenda assume no lado esquerdo
        :param    x: a posição horizontal da legenda
        :param    y: a posição vertical da legenda
        :param jogo: o jogo que esta legenda aparece
        :param cena: a cena onde o jogo aparece
        :param lacuna: imagem de fundo da lacuna
        :param legenda: imagem de fundo da legenda
        """
        def __init__(self, nome, tit, x, y, cena, jogo, lacuna=VAZIO, legenda=VAZIO):
            self.nome, self.tit, self.x, self.y, self.jogo = nome, tit, x, y, jogo
            titulo = f"n_{tit}"
            drop = {titulo: self.acertou}
            """este dicionário determina que somente a legenda que tenha este título vai acionar o método acertou"""
            self.lacuna = J.a(lacuna, x=x, y=y, w=160, h=40, style=SF, cena=cena, drop=drop)
            """Cria um elemento que posiciona a lacuna e aceita um drop do elemento que tem o título correto"""
            self.o_nome = J.a(legenda, tit=titulo, x=x, y=y, w=160, h=40, style=SF, cena=cena, drag=True)
            """Cria um elemento que posiciona a legenda e tem o título eceito pela lacuna e pode ser arrastado"""
            self.o_nome.elt.html = f"{nome}"
            """Adiciona o nome no elemento que é a legenda"""
            set_timeout(self.inicia, 1500+300*tit)
            """Inicia um cronômetro (1.5 seg) para o jogador ter um tempinho para ver a solução, cada legenda leva mais tempo"""
            
        def acertou(self, ev=None, nome=None):
            """Quando o jogador acerta, apaga as interrogações da lacuna e posiciona a legenda sobre a lacuna"""
            self.lacuna.elt.html = ""
            self.o_nome.x = self.x
            self.o_nome.y = self.y
            self.jogo.pontuar()
            
        def inicia(self, ev=None):
            """Quando inicia coloca interrogações na lacuna e posiciona a legenda à esquerda"""
            self.lacuna.elt.html = "??????????"
            self.o_nome.x = 100
            self.o_nome.y = 50+40*self.tit
        

    
    def __init__(self):
        self.cena = J.c(self.CENA)
        self.pontua = 0
        self.celula = J.a(self.CELULA, x=300, y=50, w=600, h=500, cena=self.cena)
        self.mito = self.Nome(nome="mitocôndria", tit=0, x=650, y=150, jogo=self, cena=self.cena)
        self.nucle = self.Nome(nome="núcleo",  tit=1, x=550, y=220, jogo=self, cena=self.cena)
        self.reticulo = self.Nome(nome="reticulo", tit=2, x=450, y=100, jogo=self, cena=self.cena)
        self.ribossomo = self.Nome(nome="ribossomo",  tit=3, x=560, y=40, jogo=self, cena=self.cena)
        self.cena.vai()
        
    def pontuar(self):
        self.pontua += 1
        if self.pontua == 4:
            J.n(self.cena, "Você acertou tudo! Parabéns!").vai()

def main():
    Associa()
    
main()