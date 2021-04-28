# lorinda.anastasia.main.py
from _spy.vitollino.main import Jogo, STYLE
from browser.timer import set_timeout
"""Usa o timer do navegador para dar um tempinho inicial"""

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
        def __init__(self, nome, tit, x, y, cena, jogo, caixa=160, borda=100,
            lacuna=VAZIO, legenda=VAZIO):
            self.nome, self.tit, self.x, self.y, self.jogo, self.borda = nome, tit, x, y, jogo, borda
            titulo = f"n_{tit}"
            """Este título serve para marcar cada legenda. É usado pelo drop para conferir se é a legenda certa"""
            drop = {titulo: self.acertou}
            """este dicionário determina que somente a legenda que tenha este título vai acionar o método acertou"""
            self.lacuna = J.a(lacuna, x=x, y=y, w=160, h=40, style=SF, cena=cena, drop=drop)
            """Cria um elemento que posiciona a lacuna e aceita um drop do elemento que tem o título correto"""
            self.o_nome = J.a(legenda, tit=titulo, x=x, y=y, w=caixa, h=40, style=SF, cena=cena, drag=True)
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
            self.o_nome.x = self.borda
            self.o_nome.y = 50+40*self.tit
        

    
    def __init__(self, cena, acertou=None, acertos=4, caixa=160, borda=100):
        self.cena, self.caixa, self.borda, self.acertos = cena, caixa, borda, acertos
        self.pontua = 0
        self.acertou = acertou or self.acerta
        '''
        self.mito = self.Nome(nome="mitocôndria", tit=0, x=650, y=150, jogo=self, cena=self.cena)
        self.nucle = self.Nome(nome="núcleo",  tit=1, x=550, y=220, jogo=self, cena=self.cena)
        self.reticulo = self.Nome(nome="reticulo", tit=2, x=450, y=100, jogo=self, cena=self.cena)
        self.ribossomo = self.Nome(nome="ribossomo",  tit=3, x=560, y=40, jogo=self, cena=self.cena)
        #self.cena.vai()'''
        
    def nome(self, nome, tit=0, x=650, y=150):
        return self.Nome(nome=nome, tit=tit, x=x, y=y,caixa=self.caixa, borda=self.borda,
        jogo=self, cena=self.cena)
        
    def acerta(self):
            J.n(self.cena, "Você acertou tudo! Parabéns!").vai()
        
    def pontuar(self):
        self.pontua += 1
        if self.pontua == self.acertos:
            self.acertou()



class Swap:
    """ Jogo que embaralha as partes de um desenho e usa drag and drop para rearrumar.
        
        As peças aparecem inicialmente embaralhadas e devem ser arrastadas para o local onde deveriam estar
        
        :param    j: referência ao Jogo do Vitollino.
        :param  img: a imagem que deve ser embaralhada
        :param cena: a cena onde o jogo aparece
        :param    x: a posição horizontal da imagem
        :param    y: a posição vertical da imagem
        :param    w: a largura da imagem
        :param    h: a altura da imagem
        :param   dw: quantidade de colunas que recortam a imagem
        :param   dh: quantidade de linhas que recortam a imagem
    """
    def __init__(self, j, img, cena, w=900,h=400,x=100,y=50,dw=3,dh=3):
        swap = self
        class Peca(j.a):
            """ A Peça representa um recorte da imagem que vai ser embaralhada.
            """
            def __init__(self, local, indice):
                self.local, self.indice = local, indice
                """ local em que a peça foi colocada; local onde a peça deveria estar"""
                pw, ph = w//dw, h//dh
                """largura e altura da peça"""
                lx, ly = x+local%dw*pw, y+local//dw*ph
                """posição horizontal e vertical em pixels onde a peça será desenhada"""
                px, py = indice%dw*pw, indice//dw*ph
                """posição horizontal e vertical em pixels onde o desenho da peça está na imagem"""
                super().__init__(img, x=lx, y=ly, w=pw, h=ph, drag=True, cena=cena)
                """chama o construtor do Elemento Vitollino passandoa as informações necessárias"""
                self.siz = (w, h)
                """redimensiona a figura da imagem para o tamanho fornecido"""
                self.elt.Id = f"_swap_{local}"
                """rotula o elemento da peça com a posição onde foi alocada"""
                self.pos = (-px, -py)
                """reposiciona a figura da imagem para o pedaço que vai aparecer na peça"""
                self.elt.ondrop = lambda ev: self.drop(ev)
                """captura o evento drop da peça para ser tratado pelo método self.drop"""
            def drop(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                src_id = ev.data['text']
                local = int(src_id.split('_')[-1])
                print(f"local -> {local} | indice -> {self.indice}")
                self.dropped(ev, local)
                
            def dropped(self, ev, local):
                o_outro = swap.pecas[local].pra_la(self, self.x, self.y, local)
                o_local = swap.pecas[local].local
                print(f"indice, o outro -> {self.indice} @ {self.local} <-> {o_outro} @ {o_local}")
                swap.montou()
            def pra_la(self, peca, x, y, local):
                self.local = peca.pra_ca(self.x, self.y, self.local)
                self.x, self.y = x, y
                return self.indice
            def pra_ca(self, x, y, local):
                self.local, local = local, self.local
                self.x, self.y = x, y
                return local
            def certo(self):
                return self.indice == self.local
            def __repr__(self):
                return str(self.indice)

        from random import shuffle
        pecas = list(range(dw*dh))
        shuffle(pecas)
        self.pecas = [Peca(local, indice) for local, indice in enumerate(pecas)]
        self.venceu = J.n(cena, "Voce venceu!")
    def montou(self):
        resultado = [peca.certo() for peca in self.pecas]
        print(resultado)
        self.venceu.vai() if all(resultado) else None 
        return all(resultado)
        

def main():
    cena = J.c(Associa.CENA)
    celula = J.a(Associa.CELULA, x=300, y=50, w=600, h=500, cena=cena)
    # Swap(j=J, img=Associa.CELULA, cena=cena, w=600,h=500,x=300,y=50,dw=3,dh=3)
    associa = Associa(cena, caixa=300, borda=20)
    mito = associa.nome(nome="mitocôndria", tit=0, x=650, y=150)
    nucle = associa.nome(nome="núcleo",  tit=1, x=550, y=220)
    reticulo = associa.nome(nome="reticulo", tit=2, x=450, y=100)
    ribossomo = associa.nome(nome="ribossomo",  tit=3, x=560, y=40)
    cena.vai()
    
main()