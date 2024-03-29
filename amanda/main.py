# lorinda.amanda.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE, JOGO
from _spy.vitollino.main import Inventario as inv
from anastasia.main import Swap

STYLE["width"] = 800
STYLE["height"] = "600px"
MARIA = "https://i.imgur.com/1sI2ePw.png"
NPC = "https://imgur.com/VcPXMYC.png"

PAREDE = "https://i.imgur.com/ZAoCT4o.png"
P = ""
A = ""
R= ""
E = ""
D = ""
E = ""
C = ""
L = ""
U = ""
L = ""
A = ""
R = ""
class Fase10:
    """Usa um editor de imagem ( /) e recorta o Herdograma em linhas geracionais.
       No game, o jogador terá que clicar nas linhas em ordem certa para montar o herdograma corretamente.
    """
    def __init__(self, esta_cena, chama_quando_acerta):
        posiciona_proxima = self.posiciona_proxima
        class LinhaGeracional:
            """Representa cada uma das linhas recortadas do herdograma original"""
            def __init__(self, linha, posicao):
                self.posicao = posicao # posição original no topo da página
                self.linha = Elemento(linha, x=posicao*200, y=20, w=200, h=50, cena=esta_cena)
                self.linha.vai = self.clica_e_posiciona_a_linha #quando clica, monta o herdograma
            def zera(self):
                self.linha.x = self.posicao*200  # posiciona cada peça com 200 pixels de distância
                self.linha.y = 20  # posiciona a peça no topo da página
                self.linha.vai = self.clica_e_posiciona_a_linha
            def clica_e_posiciona_a_linha(self, *_):
                x, y = posiciona_proxima(self.posicao)
                if y:  # se o y retornou zero é porque o posiciona próxima detectou montagem errada
                    self.linha.x, self.linha.y = x, y # monta a linha no herdograma
                    self.linha.vai = lambda *_:None #desativa o click da linha

        # coloca cada uma das linhas embaralhadas 
        self.linhas = [
            LinhaGeracional(linha=uma_linha, posicao=uma_posicao)
            for uma_posicao, uma_linha in enumerate([HERDO1, HERDO3, HERDO2, HERDO0])]
        self.acertou = chama_quando_acerta
        self.linha_inicial = 300
        self.altura_da_linha = 50  # cada peça do herdograma tem esta altura
        self.posicoes_montadas = []  #l ista das linhas já montadas no herdograma
        self.posicoes_corretas = [3, 0, 2, 1]  # lista das linhas montadas corretamente

    def posiciona_proxima(self, posicao):
        """Chamdo pelo clique (vai) de cada peça. Atualiza a próxima posição da peça.
           Calcula se montou correto, comparando com a lista de posicões corretas.
           Se já montou quatro peças, e não acerto sinaliza com zero, para iniciar o jogo.
        """
        self.linha_inicial += self.altura_da_linha  # incrementa a posição para montar na linha de baixo
        self.posicoes_montadas += [posicao]  # adiciona o índice desta peça na lista de peças montadas
        if self.posicoes_montadas == self.posicoes_corretas:
            self.acertou()  # invoca a ação acertou se montou nas posições corretas
            return 300, self.linha_inicial
        else:
            if len(self.posicoes_montadas) == 4:  # se montou qutro peças incorretas reinicia o game
                [linha.zera() for linha in self.linhas]  # volta as peças para o topo
                self.posicoes_montadas = []  # indica que nenhuma peça foi montada
                self.linha_inicial = 300  # inicia a altura de ontagem da primeira peça
                return 0, 0  #  retorna uma posição inválida para sinalizar a peça
        return 300, self.linha_inicial

class Dialogo:
    def __init__(self):
        self.cena = cena = JOGO.c('https://i.imgur.com/ujAF00x.jpg').vai()
        fala = ("NPC: É uma estrutura que envolve a membrana plasmática,"
        " e está presente em células vegetais, organismos procariotos e alguns eucariotos, como os fungos."
        " Tem como principal função, proteger a célula.")
        self.npc = Elemento(NPC, x=400, y=300, w=100, cena=cena, texto=fala, foi=self.maria_fala)
        vai = self.npc.vai
        self.npc.vai, self.npc_vai = self.nada, self.npc.vai
        def maria_fala(*_):
            self.npc.vai = self.npc_vai
            self.maria.vai, self.maria_vai = self.nada, self.maria.vai
        self.maria = Elemento(MARIA, x=200, y=300, w=100, cena=cena, texto="Nossa! Que estrutura é essa?", foi=maria_fala)
    def nada(self, *_):
        pass
    def maria_fala(self, *_):
        self.npc.vai, self.npc_vai = self.nada, self.npc.vai
        self.maria.vai = Texto(self.cena, "Maria pergunta: E agora como faço para sair daqui?", foi=self.npc_fala).vai
    def npc_fala(self, *_):
        fala = "NPC: Você precisa resolver o enigma. Forme a palavra correta e livre você estará."
        self.npc.vai = Texto(self.cena, fala, foi=self.jogar).vai

    def jogar(self, _=0):
        cena = JOGO.c('https://i.imgur.com/ujAF00x.jpg').vai()
        t = JOGO.n(cena, 'É isto! A Parede Celular!')
        Swap(JOGO, PAREDE, cena, w=700,h=200,x=50,y=150,dw=7,dh=2, venceu=t)

def main(_=0):
    Dialogo()
    # t = JOGO.n(cena, 'É isto! A Parede Celular!').vai()
    
    
if __name__ == "__main__":
    main()
    