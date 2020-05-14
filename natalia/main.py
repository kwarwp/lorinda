# lorinda.natalia.main.py Leniaaaaah(não mexer)
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
from _spy.vitollino.main import Inventario as inv

STYLE["width"] = 800
STYLE["height"] = "600px"

ZEZINHO = "https://i.imgur.com/94lhgKo.png"
ROSALINDA = "https://i.imgur.com/qvuwHvs.png"
CASA = "https://www.tudoconstrucao.com/wp-content/uploads/2014/12/casa-de-praia-colorida-simples.jpg"
QUADROS = "https://staticcdns3.bidu.com.br/jamal/uploads/2016/11/06164925/3b1.jpg"
QUADROS1 = "https://staticcdns3.bidu.com.br/jamal/uploads/2016/11/06164925/3b1.jpg"
TOUR = "https://s2.glbimg.com/zYpJy77kEUuJR3sRh3kiTdzZ4Bk=/620x455/e.glbimg.com/og/ed/f/original/2014/02/27/cj688paisagismo130.jpg"
COFRE = "https://a-static.mlcdn.com.br/618x463/cofre-concretado-com-boca-de-lobo-ct30bl-30x36x26-segredo-mecanico-cofresventura/cofresventura/5030/aeae22f74a1dac4ebacb09409c0875bd.jpg"
HEREDOGRAMA = "https://pt-static.z-dn.net/files/d71/7bf7ab4461bea11a7a1c561ed2584a48.png"
PERGAMINHO = "https://i.pinimg.com/originals/df/6c/76/df6c765f7019656350531c4a4eff5e11.png"
BIBLIOTECA = "https://www.ifpb.edu.br/cajazeiras/noticias/2018/05/saiba-o-que-muda-com-a-implantacao-da-rede-integrada-de-bibliotecas-do-ifpb/regulamento-da-biblioteca-colegio-salesiano-dom-bosco-cidade-alta.png/@@images/image.png"
LIVRO = "https://img2.gratispng.com/20180505/hzw/kisspng-circle-black-and-white-clip-art-5aed68ee811080.5110845515255083345287.jpg"
SALA = "https://gizmodo.uol.com.br/wp-content/blogs.dir/8/files/2011/08/bias1-4e558ed-intro-thumb-640xauto-24932-1280x720.jpg"
QUADRADO = "https://w1.ezcdn.com.br/rebalcomercial/fotos/grande/3250fg1/prato-raso-porcelana-26-cm-branco-quadrado-americana-germer-gmr-068.jpg"
QUADRADO1 = "https://t2.uc.ltmcdn.com/pt/images/2/6/3/exercicio_para_calcular_a_diagonal_de_um_quadrado_24362_4_600.jpg"
CIRCULO = "https://png.pngtree.com/png-clipart/20190223/ourlarge/pngtree-circulo-ros%C3%AA-gold-png-image_693439.jpg"
HERDO0="https://i.imgur.com/9jsxjLw.png"
HERDO1="https://i.imgur.com/w60bNMG.png"
HERDO2="https://i.imgur.com/RztgWA1.png"
HERDO3="https://i.imgur.com/FZOhJhb.png"
AAH2= "https://i.imgur.com/y7R4ZdF.png"
AAH1 = "https://i.imgur.com/TiTfioK.png"
AAH3 = "https://i.imgur.com/coU94XJ.png"
AAH4 = "https://i.imgur.com/oXZfA3p.png"
QUE = "https://www.grupoescolar.com/a/b/heredograma-C8.jpg"

class MiniGameHerdograma:
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
            


class gameg():
    def __init__(self):
        """Inicia cada cena do jogo e conecta o metodo vai com um metodo (def) da classe gameg"""
        self.casa = casa = Cena( img = CASA)
        self.zezinho = Elemento( img = ZEZINHO, tit= "bOA TARDE, SOU ZEZINHO E VIM PARA A ENTREVISTA" ,
        style=dict (left=200, top=350, width=200, height="200px",))
        self.rosalinda = Elemento( img = ROSALINDA, tit= "OLÁ, SOU ROSALINDA,vAMOS COMEÇAR A ENTREVISTA?" ,
        style=dict (left=400, top=350, width=300, height="200px",))
        self.zezinho.entra(casa)
        self.rosalinda.entra(casa)
        casa.direita=Cena()
        """cria a cena quadros e conecta o metodo vai com um metodo (def) self.quadros_vai"""
        casa.direita.vai = self.quadros_vai
        self.quadros = quadros = Cena( img = QUADROS)
        # quadros.esquerda=casa
        quadros.esquerda=Cena()
        """Conecta o metodo esquerda vai com um metodo (def) self.casa_vai,
        permite que zezinho e rosalinda vontem para a cena casa
        cria uma cena vazia na direita para poder direcionar ao metodo self.tour_vai"""
        quadros.esquerda.vai = self.casa_vai
        quadros.direita=Cena()
        # casa.direita=quadros
        """cria a cena tour e conecta a esquerda com a cena quadros
        conencta o quadros direita (cena Vazia) com a cena tour via self.tour_vai"""
        self.tour = tour = Cena( img = TOUR)
        quadros.direita.vai = self.tour_vai
        tour.esquerda=quadros
        quadros1= Cena( img = QUADROS1)
        tour.direita=quadros1
        """cria a cena cofre e conecta a esquerda com a cena quadros
        conencta elemento o_quadro.vai com a cena cofre via self.quadro_vai, monta o minigame no cofre"""
        self.cofre = cofre = Cena(img = COFRE)# ESSE COFRE PRECISA TER UM HEREDPGRAMA PARA ABRIR
        cofre.esquerda = Cena()
        cofre.esquerda.vai = self.quadros_vai
        MiniGameHerdograma(cofre, self.mostra_conteudo_cofre)
        # heredo = Elemento(HEREDOGRAMA, x=540, y= 370, w=200, tit="Esse heredograma é a pista!")
        # heredo.entra(cofre)
        o_quadro = Elemento(QUADRADO, x=340, y= 270, tit="Esse quadro tem algo diferente", style={"opacity":0.05})
        o_quadro.vai = self.cofre_vai
        o_quadro.entra(quadros)
        self.pergaminho = pergaminho = Cena (img = PERGAMINHO)
        hum(pergaminho, self.mostra_conteudo_pergaminho)
        quadros1.direita=pergaminho
        pergaminho.esquerda=quadros
        self.sala=sala=Cena (img=SALA)
        aah(sala,self.mostra_conteudo_sala)
        sala.direita=quartos2
        self.biblioteca=biblioteca= Cena(BIBLIOTECA)
        funciona(biblioteca,self.mostra_conteudo_biblioteca)
        quartos2=Cena(img= QUARTOS2)
        biblioteca = Cena (img = BIBLIOTECA)
        pergaminho.direita= biblioteca
        livro = Elemento (img = LIVRO)
        livro.entra(biblioteca)
        que = Cena(img = QUE)
        casa.vai()
    def mostra_conteudo_cofre(self, *_):        
        Texto(self.cofre, "ZEZINHO: Encontrei um mapa interessante dentro do cofre!").vai()
    def mostra_conteudo_pergaminho(self, *_):   
        Texto(self.pergaminho, "parabéns, agora vamos ver para onde vamos!").vai()
        #COMADOS DE :ORGANIZE E MONTE
    def mostra_conteudo_sala(self,*_):
        Texto(self.sala,"MAPA").vai()
    def mostra_conteudo_biblioteca(self,*_):
        Texto(self.biblioteca,"parabéns , vcestá sabendo biologia, vamos ver na proxima fase se entendeu mesmo").vai()
        
    def quadros_vai(self, *_):        
        self.zezinho.entra(self.quadros)#colocar mesnagem confusa de zezinho em relação aos quadros
        self.zezinho.tit = "Lindos quadros!"
        self.rosalinda.tit = "Obrigada! Fique à vontade para examiná-los!"
        self.rosalinda.entra(self.quadros)
        ver_quadro = Texto(self.quadros, "ZEZINHO: Preciso examinar cada quadro, acho que tem um mistério aqui!")
        Texto(self.quadros, "ZEZINHO: Quadros! Muitos quadros, até quadros com escrita!", foi=ver_quadro.vai).vai()
        self.quadros.vai()
    def casa_vai(self, *_):        
        self.zezinho.tit = "Você é uma pessoa muito agradável!"
        self.rosalinda.tit = "Obrigada! Procuro tratar bem as pessoas"
        self.zezinho.entra(self.casa)
        self.rosalinda.entra(self.casa)
        self.casa.vai()
    def tour_vai(self, *_): 
        self.zezinho.entra(self.tour)#zezinha volta para ver o quadros pois ficou encafifado
        self.rosalinda.entra(self.tour)
        self.rosalinda.tit = "com licença, preciso atender essa ligação...mas fique a vontade, por favor"
        self.zezinho.tit = "preciso ver aqueles quadros novamente"
        self.tour.vai()
        
    def quadros1(self, *_):
        self.zezinho.entra(self.quadros1)#zezinho ajeita o quadro e quando irá arrumar outro quadro e ele está muito pesado, ao tirar da parde encontra um cofre
        #NAO ENTENDI A GAVETA COM LETRAS
        self.zezinho.entra.tit = "tem algo estranho com esse quadro"
        self.quadros1.vai()
        
    def cofre_vai(self, *_):
        #self.heredograma.entra(self.cofre)#estar como um quadro
        self.zezinho.entra(self.cofre)
        self.cofre.vai()
        # ao clicar no heredograma ,abrir o cofre
        #LEMBROU DE UMA AULA NA FIO CRUZ
        #ABRIU O COFRE E PEGOU UM PAPEL
    def pergaminho(self, *_):
        self.zezinho.entra(self.pergaminho)
        self.heredograma.entra(self.pergaminho)
        self.zezinho.entra.tit = "esse heredrograma irá para algum lugar"
        self.pergaminho.vai()
        
    def sala(self, *_): #colocar como def hum?
        self.quadrado.entra(self.sala)
        self.quadrado1.entra(self.sala)
        self.circulo.entra(self.sala)
        self.zezinho.entra(self.sala)
        self.zezinho.entra.tit = "acho que eu preciso fazer algo com isso"
        self.sala.vai()
        
        
class hum :
    def __init__(self, esta_cena, chama_quando_acerta, partes=(AAH1, AAH2, AAH3, AAH4)):
        posiciona_proxima = self.posiciona_proxima
        class LinhaGeracional:
            """Representa cada uma das linhas recortadas do herdograma original"""
            def __init__(self, linha, posicao):
                self.posicao = posicao # posição original no topo da página
                self.linha = Elemento(linha, x=posicao*200, y=20, w=175, h=125, cena=esta_cena)
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
            for uma_posicao, uma_linha in enumerate(partes)]
        self.acertou = chama_quando_acerta
        self.parte_inicial = -1
        self.altura_da_linha = 125  # cada peça do herdograma tem esta altura
        self.posicoes_montadas = []  #l ista das linhas já montadas no herdograma
        self.posicoes_corretas = [0, 2, 1, 3] 
        
    def posiciona_proxima(self, posicao):
        
        largura_da_peca, inicio_horizontal, inicio_vertical, numero_de_pecas = 175, 300, 200, 4
        numero_de_pecas_por_linha = 2
        self.parte_inicial += 1  # incrementa a posição para montar a próxima posiçao da peça
        self.posicoes_montadas += [posicao]  # adiciona o índice desta peça na lista de peças montadas
        if self.posicoes_montadas == self.posicoes_corretas:
            self.acertou()  # invoca a ação acertou se montou nas posições corretas
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
        else:
            if len(self.posicoes_montadas) == numero_de_pecas:  # se montou qutro peças incorretas reinicia o game
                [linha.zera() for linha in self.linhas]  # volta as peças para o topo
                self.posicoes_montadas = []  # indica que nenhuma peça foi montada
                self.parte_inicial = -1  # inicia a altura de ontagem da primeira peça
                return 0, 0  #  retorna uma posição inválida para sinalizar a peça
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
    def acertou(self):
        Texto(self.sala, "UAU, você conseguiu passar a fase lembrar! Achei uma saída pela direita!").vai()
        self.sala = self.salax


iih, iih1, iih2, iih3 = AAH1, AAH2, AAH3, AAH4   # remendo provisório só para rodar       
class aah :
    #imagem salva no meu computador como heredogramas
    def __init__(self, esta_cena, chama_quando_acerta, partes=(iih, iih1, iih2, iih3)):# esta sem imagem pois o editor de fotos não esta funcionando
        posiciona_proxima = self.posiciona_proxima
        class LinhaGeracional:
            """Representa cada uma das linhas recortadas do herdograma original"""
            def __init__(self, linha, posicao):
                self.posicao = posicao # posição original no topo da página
                self.linha = Elemento(linha, x=posicao*200, y=20, w=175, h=125, cena=esta_cena)
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
            for uma_posicao, uma_linha in enumerate(partes)]
        self.acertou = chama_quando_acerta
        self.parte_inicial = -1
        self.altura_da_linha = 125  # cada peça do herdograma tem esta altura
        self.posicoes_montadas = []  #l ista das linhas já montadas no herdograma
        self.posicoes_corretas = [3, 1, 2, 0] 
        
    def posiciona_proxima(self, posicao):
        largura_da_peca, inicio_horizontal, inicio_vertical, numero_de_pecas = 175, 300, 200, 4
        numero_de_pecas_por_linha = 2
        self.parte_inicial += 1  # incrementa a posição para montar a próxima posiçao da peça
        self.posicoes_montadas += [posicao]  # adiciona o índice desta peça na lista de peças montadas
        if self.posicoes_montadas == self.posicoes_corretas:
            self.acertou()  # invoca a ação acertou se montou nas posições corretas
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
        else:
            if len(self.posicoes_montadas) == numero_de_pecas:  # se montou qutro peças incorretas reinicia o game
                [linha.zera() for linha in self.linhas]  # volta as peças para o topo
                self.posicoes_montadas = []  # indica que nenhuma peça foi montada
                self.parte_inicial = -1  # inicia a altura de ontagem da primeira peça
                return 0, 0  #  retorna uma posição inválida para sinalizar a peça
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
    def acertou(self):
        Texto(self.sala, "MAPA").vai()
        self.salax = self.quartos2
        def salax (self,*_):
            self.salax.vai()
        
        #fazer uma fase de transição ao achar o mapa e procurar alguns quartos
ff1, ff, ff2, ff3 = AAH1, AAH2, AAH3, AAH4   # remendo provisório só para rodar

class funciona :
    def __init__(self, esta_cena, chama_quando_acerta, partes=(ff1, ff, ff2, ff3)):#esta sem imagem pq o editor não funciona
        posiciona_proxima = self.posiciona_proxima
        class LinhaGeracional:
            """Representa cada uma das linhas recortadas do herdograma original"""
            def __init__(self, linha, posicao):
                self.posicao = posicao # posição original no topo da página
                self.linha = Elemento(linha, x=posicao*200, y=20, w=175, h=125, cena=esta_cena)
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
            for uma_posicao, uma_linha in enumerate(partes)]
        self.acertou = chama_quando_acerta
        self.parte_inicial = -1
        self.altura_da_linha = 125  # cada peça do herdograma tem esta altura
        self.posicoes_montadas = []  #l ista das linhas já montadas no herdograma
        self.posicoes_corretas = [1, 3, 2, 0] 
        
    def posiciona_proxima(self, posicao):
        largura_da_peca, inicio_horizontal, inicio_vertical, numero_de_pecas = 175, 300, 200, 4
        numero_de_pecas_por_linha = 2
        self.parte_inicial += 1  # incrementa a posição para montar a próxima posiçao da peça
        self.posicoes_montadas += [posicao]  # adiciona o índice desta peça na lista de peças montadas
        if self.posicoes_montadas == self.posicoes_corretas:
            self.acertou()  # invoca a ação acertou se montou nas posições corretas
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
        else:
            if len(self.posicoes_montadas) == numero_de_pecas:  # se montou qutro peças incorretas reinicia o game
                [linha.zera() for linha in self.linhas]  # volta as peças para o topo
                self.posicoes_montadas = []  # indica que nenhuma peça foi montada
                self.parte_inicial = -1  # inicia a altura de ontagem da primeira peça
                return 0, 0  #  retorna uma posição inválida para sinalizar a peça
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
    def acertou(self):
        Texto(self.sala, "parabéns , vcestá sabendo biologia, vamos ver na proxima fase se entendeu mesmo").vai()
        self.quartos2 = self.ajuda
        def quartos2(self,*_):
            # Figuras geométricas/Traços (simples, duplos, triplos)
            #Casamento cosanguineo/Quatro indivíduas/Dois com anomalias/Dois normais do sexo masculino
            #dar um motivo para fazer esse quebra cabeça
            self.quartos2.vai()

        def ajuda(self,*_):
            self.que = Cena (img = QUE)
            # uma caixinha de pergunta para aconselhar
            
            self.ajuda.vai()

II1,II2,II3,II4, II5,II6,II7,II7,II8,II9 = AAH1, AAH2, AAH3, AAH4, AAH1, AAH2, AAH3, AAH4,  AAH3, AAH4   # remendo provisório só para rodar

class acabou :
    def __init__(self, esta_cena, chama_quando_acerta, partes=(II1,II2,II3,II4, II5,II6,II7,II7,II8,II9)):
        posiciona_proxima = self.posiciona_proxima
        class LinhaGeracional:
            """Representa cada uma das linhas recortadas do herdograma original"""
            def __init__(self, linha, posicao):
                self.posicao = posicao # posição original no topo da página
                self.linha = Elemento(linha, x=posicao*200, y=20, w=175, h=125, cena=esta_cena)
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
            for uma_posicao, uma_linha in enumerate(partes)]
        self.acertou = chama_quando_acerta
        self.parte_inicial = -1
        self.altura_da_linha = 125  # cada peça do herdograma tem esta altura
        self.posicoes_montadas = []  #l ista das linhas já montadas no herdograma
        self.posicoes_corretas = [1, 3, 2, 0, 5 , 4, 9, 8, 7]
        
    def posiciona_proxima(self, posicao):
        
        largura_da_peca, inicio_horizontal, inicio_vertical, numero_de_pecas = 175, 300, 200, 4
        numero_de_pecas_por_linha = 2
        self.parte_inicial += 1  # incrementa a posição para montar a próxima posiçao da peça
        self.posicoes_montadas += [posicao]  # adiciona o índice desta peça na lista de peças montadas
        if self.posicoes_montadas == self.posicoes_corretas:
            self.acertou()  # invoca a ação acertou se montou nas posições corretas
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
        else:
            if len(self.posicoes_montadas) == numero_de_pecas:  # se montou qutro peças incorretas reinicia o game
                [linha.zera() for linha in self.linhas]  # volta as peças para o topo
                self.posicoes_montadas = []  # indica que nenhuma peça foi montada
                self.parte_inicial = -1  # inicia a altura de ontagem da primeira peça
                return 0, 0  #  retorna uma posição inválida para sinalizar a peça
            return (inicio_horizontal+largura_da_peca*(self.parte_inicial%numero_de_pecas_por_linha),
                    inicio_vertical+self.altura_da_linha*(self.parte_inicial//numero_de_pecas_por_linha))
    def acertou(self):
        Texto(self.sala, "INCRIVÉL SEUS CONHECIMENTOS EM HEREDITARIEDADE, ACREDITO QUE SERÁ O MELHOR CIENTISTA").vai()           
        def ultimaparte(self,*_):
            #volta para sala(onde tem o monitor
            #para ter acesso ao computador precisa criar um heredograma
            #quebra cabeça 
            #informções que precisa saber
            #Homem/Mulher/Aborto/União Múltipla/Cosanguinidade/Mulher/Adotado pela família/Natimorto
            #motivo destravar o computador
            self.ultimarparte.vai()
        
        
        
gameg()        
        
        
