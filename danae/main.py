# lorinda.danae.main.py
from _spy.vitollino.main import Cena, Sala, Labirinto, Elemento, Texto, STYLE, INVENTARIO as inv
STYLE.update(width=900, height="650px")
CENAS = "CkepkCR nnBZp4Y 1ZCmVlf W5Q3VcS".split()
INTER = "XXQmytH UGVhUV6 dIPsMeh bi4tHyr".split()  #
SANCT = "5kwiit6 Bip0ltd jKNasd1 Ac7LD9Z".split()
CENA = "https://i.imgur.com/%s.jpg"
CAPEL = "XJTHqUW iiiorD4".split()
PROP = "S2td4Uk i2jZEzM WwNrwlJ u1bDkus cEJbS0C".split()  # hB7FFDO RO0oeZI
MPROP = "Fxc4cCK 4yxhrO0".split()
JEROM = "https://i.imgur.com/IGFstQy.png"
SONHO = "https://i.imgur.com/uHw57i1.jpg"
MARCA = "https://i.imgur.com/2moCwSz.png"
class TheCave:
    def __init__(self):
        cena = Cena(CENA % CENAS)
        self.jero, self.placa, self.cruz , self.grego , self.vulgata = [
            CENA % obj for obj in PROP]
        self.pano, self.livro = [
            CENA % obj for obj in MPROP]
        
        self.capel = capel = [Cena(CENA % parede) for parede in CAPEL]
        self.sala = sala = Sala(*[CENA % parede for parede in CENAS]) 
        self.atrio = atrio = Sala(*[CENA % parede for parede in INTER]) 
        self.sanct = sanct = Sala(*[CENA % parede for parede in SANCT]) 
        #cena.vai()
        cave = Labirinto(c=atrio,n=sanct, s=sala)
        # capel[0].meio = capel[1]
        capel[0].meio = Cena(vai=self.sao_jeronimo)
        capel[1].meio = capel[1].esquerda = capel[1].direita = sala.norte
        #capel[0].vai()
        #atrio.leste.vai()
        #sanct.leste.vai()
        self.e_limbo = Elemento("")
        self.e_grego = Elemento(self.grego, x=510, y=210, w=280, vai=self.rasga)
        self.e_placa = Elemento(self.placa, x=510, y=210, w=280, cena=atrio.leste)
        self.e_jero = Elemento(self.jero, x=360, y=214, w=147, h=250, cena=sanct.leste, tit="icone", drag=True)
        #self.e_jero = Elemento(self.pano, x=360, y=212, w=150, h=250, cena=sanct.leste)
        self.e_jerom = Elemento(JEROM, x=0, y=400, w=150, h=250, cena=sanct.leste)
        self.e_vecruz = Elemento(MARCA, x=480, y=100, w=150, h=250, o=0.1, cena=capel[0],
            vai= self.sao_jeronimo)
        self.e_vecruz.o = 0.2
        self.sao_jeronimo()
        
    def sao_jeronimo(self, *_):
        def sonho(*_):
            Texto(self.sala.sul, "A devoção de São Jerônimo invade seu coração"
            " e você entra em um sonho que ele teve com Jesus",
            foi=self.o_sonho).vai()
            
        self.e_vecruz = Elemento(MARCA, x=640, y=150, w=90, h=180, o=0.1, cena=self.sala.sul,
            vai= sonho)
        self.e_vecruz.o = 0.2
        self.capel[1].vai()
        #self.e_vecruz.x, self.e_vecruz.y, self.e_vecruz.w, self.e_vecruz.h = 580, 150, 180, 60
        #self.e_vecruz.x = 640
        self.e_vecruz.vai = sonho
        busca = Texto(self.capel[1], "Visite a gruta e toque em um crucifixo sob um foco de luz",
            foi=lambda *_: self.e_vecruz.entra(self.sanct.norte))
        fala = Texto(self.capel[1], "Que bom você me visitar, aprenda meu caminho para santidade", foi=busca.vai)
        self.e_jerom.vai = fala.vai
        visao = Texto(self.capel[1], "Você se ajoelha e faz uma oração, São Jerônimo aparece numa visão",
        foi=lambda *_: self.e_jerom.entra(self.capel[1]))
        Texto(self.capel[1], "Você veio conhecer a gruta onde São Jerônimo traduziu a Bíblia", foi=visao.vai).vai()
        
    def o_sonho(self, *_):
        def acorda(*_):
            self.e_vecruz.entra(self.limbo)
            self.e_grego.entra(self.sala.sul)
            self.sala.sul.vai()
        local = Cena(SONHO)
        self.e_jerom.entra(local) 
        busca = Texto(local, "Eu acho que ele esta em cima da minha escrivaninha",
            foi=acorda )
        fala = Texto(local, "Você precisa me ajudar a encontrar o pergaminho em grego que eu estava traduzindo", foi=busca.vai)
        self.e_jerom.vai = fala.vai
        local.vai()
        visao = Texto(local, "Neste sonho, Jesus me repreende porque não tenho me dedicado à leitura da Bíblia"
        ).vai()
    def toca(*_):
            inv.bota(self.e_jero)
            santo = Texto(local, "Preciso que você ore por mim, para que eu termine a tradução."
            "Bote o meu retrato em trẽs altares diferentes da gruta e peça que Deus me ilumine",
            foi=lambda *_: Altares(self.sala, self.atrio, self.sanct)).vai()
        
    def rasga(self, *_):
        def santo(*_):
            self.e_jero.vai = toca

        def emenda(*_):
            santo = Texto(local, "Deus o abençoe pela ajuda. Preciso que você ore por mim"
            "Toque no meu retrato na parede e ganhe um santinho", foi=santo).vai()
            Texto(local, "Deus seja louvado! Agora posso continuar escrevendo a Vulgata", foi=santo.vai).vai()
            local = self.sanct.norte
        def rasgou(*_):
            self.e_grego.entra(self.e_limbo)
            Puzzle(local, emenda, image=self.grego)
        local = self.sanct.norte
        self.e_jerom.entra(local) 
        Texto(local, "O pergaminho é antigo, quanto tocado se desfaz em vários pedaços",
        foi=rasgou).vai()

class Altares:
    def __init__(self, sala, atrio, sanct):
        self.jero, self.placa, self.cruz , self.grego , self.vulgata = [
            CENA % obj for obj in PROP]
        self.sala, self.atrio, self.sanct = sala, atrio, sanct
        self.icone = Elemento(self.jero, x=360, y=214, w=147, h=250, tit="icone", drag=True)
        # self.icone = inv["icone"]
        inv.bota("icone")
        self.oracao = "Ó Deus, criador do universo, que vos revelastes aos homens, através dos séculos,"
        " pela Sagrada Eucaristia,",
        "e levastes o vosso servo, São Jerônimo, a dedicar a sua vida ao estudo e à meditação da Bíblia,",
        "dai-me a graça de compreender com clareza a vossa palavra quando leio a Bíblia."
        drop =dict(icone=self.oracao)
        self.limbo = Cena("")
        self.altar_estudio = Elemento(MARCA, x=480, y=260, w=250, h=150, o=0.2, cena=sala.norte,
            drop=dict(icone=self.oracao_estudio))
        self.altar_cripta = Elemento(MARCA, x=480, y=300, w=250, h=150, o=0.2, cena=sala.oeste,
            drop=dict(icone=self.oracao_cripta))
        self.altar_nicho = Elemento(MARCA, x=480, y=220, w=250, h=150, o=0.2, cena=sala.sul,
            drop=dict(icone=self.oracao_nicho))
    def oracao_nicho(self, *_):
        self.icone.entra(inv.cena)
        self.icone.x = 640
        self.icone.y = 340
        Texto(inv.cena, **self.ora(self.altar_nicho))
    def oracao_cripta(self, *_):
        self.icone.entra(inv.cena)
        self.icone.x = 640
        self.icone.y = 340
        Texto(inv.cena, **self.ora(self.altar_nicho))
    def oracao_estudio(self, *_):
        self.icone.entra(inv.cena)
        self.icone.x = 640
        self.icone.y = 340
        Texto(inv.cena, **self.ora(self.altar_nicho))
        
    def ora(self, altar):
        def fim(*_):
            inv.bota(self.icone)
            altar.entra(self.limbo)
        def bencao(*_):
            inv.tira("icone")
            altar.entra(self.limbo)
            Texto(inv.cena, "Que a graça de Nosso Senhor Jesus Cristo esteja com você!"
            "Depois de trinta anos de estudos, consegui terminar a minha tradução da Bíblia").vai()
            
        oracao = self.oracao.pop(0)
        Texto(inv.cena, oracao).vai()
        return dict(txt=oracao, foi=fim if self.oracao else bencao)
        

class Puzzle :
    def __init__(self, esta_cena, chama_quando_acerta, partes=(1,2,3,5,8,0,4,6,7,9),
         image = None):#COM IMAGEM 
        posiciona_proxima = self.posiciona_proxima
        self.image = image
        self.sala = esta_cena
        class LinhaGeracional:
            """Representa cada uma das linhas recortadas do herdograma original"""
            def __init__(self, linha, posicao, image=image):
                self.posicao = posicao # posição original no topo da página
                self.linha = Elemento(image, x=(posicao//3)*100, y=(posicao%3)*80+20, w=90, h=70,
                cena=esta_cena)
                self.linha.siz = (90*3, 70*3)
                self.linha.pos = (-90*(linha//3), -70*(linha%3))
                self.linha.vai = self.clica_e_posiciona_a_linha #quando clica, monta o herdograma
            def zera(self):
                self.linha.x = (self.posicao//3)*100  # posiciona cada peça com 200 pixels de distância
                self.linha.y = (self.posicao%3)*80+20  # posiciona a peça no topo da página
                self.linha.vai = self.clica_e_posiciona_a_linha
            def clica_e_posiciona_a_linha(self, *_):
                x, y = posiciona_proxima(self.posicao)
                if y:  # se o y retornou zero é porque o posiciona próxima detectou montagem errada
                    self.linha.x, self.linha.y = x, y # monta a linha no herdograma
                    self.linha.vai = lambda *_:None #desativa o click da linha

        # coloca cada uma das linhas embaralhadas 
        self.linhas = [
            LinhaGeracional(linha=uma_linha, posicao=uma_posicao)
            for uma_posicao, uma_linha in enumerate(partes)]
        self.acertou = chama_quando_acerta
        self.parte_inicial = -1
        self.altura_da_linha = 70  # cada peça do herdograma tem esta altura
        self.posicoes_montadas = []  #l ista das linhas já montadas no herdograma
        self.posicoes_corretas = [ 1,2,3,5,8,0,4,6,7,9,10,11] 
        self.posicoes_corretas = [5, 2, 7, 0, 6, 8, 1, 3, 4] 
        
    def posiciona_proxima(self, posicao):
        largura_da_peca, inicio_horizontal, inicio_vertical, numero_de_pecas = 90, 300, 200, 9
        numero_de_pecas_por_linha = 3
        self.parte_inicial += 1  # incrementa a posição para montar a próxima posiçao da peça
        self.posicoes_montadas += [posicao]  # adiciona o índice desta peça na lista de peças montadas
        if self.posicoes_montadas == self.posicoes_corretas:
            self.acertou()  # invoca a ação acertou se montou nas posições corretas
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
        else:
            if len(self.posicoes_montadas) == numero_de_pecas: 
                print(self.posicoes_montadas)# se montou qutro peças incorretas reinicia o game
                [linha.zera() for linha in self.linhas]  # volta as peças para o topo
                self.posicoes_montadas = []  # indica que nenhuma peça foi montada
                self.parte_inicial = -1  # inicia a altura de ontagem da primeira peça
                return 0, 0  #  retorna uma posição inválida para sinalizar a peça
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
    def acertou(self):
        Texto(self.sala, "Deus seja louvado! Agora posso continuar escrevendo a Vulgata").vai()
        self.quartos2 = self.ajuda
        def quartos2(self,*_):
            # Figuras geométricas/Traços (simples, duplos, triplos)
            #Casamento cosanguineo/Quatro indivíduas/Dois com anomalias/Dois normais do sexo masculino
            #dar um motivo para fazer esse quebra cabeça
            self.quartos2.vai()
            
def main():
    sala = Sala(*[CENA % parede for parede in CENAS]) 
    sala.norte.vai()
    Altares(sala, sala, sala)
        
if __name__ == "__main__":
    #TheCave()
    main()