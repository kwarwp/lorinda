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
""" 
class gameg():

        casa = Cena( img = CASA)
        zezinho = Elemento( img = ZEZINHO, tit= "bOA TARDE, SOU ZEZINHO E VIM PARA A ENTREVISTA" ,
        style=dict (left=200, top=350, width=200, height="200px",))
        rosalinda = Elemento( img = ROSALINDA, tit= "OLÁ, SOU ROSALINDA,vAMOS COMEÇAR A ENTREVISTA?" ,
        style=dict (left=400, top=350, width=300, height="200px",))
        zezinho.entra(casa)
        rosalinda.entra(casa)
        
        quadros = Cena( img = QUADROS)
        casa.direita=quadros
        quadros.esquerda=casa
        zezinho.entra(quadros)#colocar mesnagem confusa de zezinho em relação aos quadros
        rosalinda.entra(quadros)
        
        tour= Cena( img = TOUR)
        quadros.direita=tour
        tour.esquerda=quadros
        zezinho.entra(tour)#zezinha volta para ver o quadros pois ficou encafifado
        rosalinda.entra(tour)#recebe um telfonema e diz que zezinho pode ficar a vontade, mas ela tera que se ausentar
        
        quadros1= Cena( img = QUADROS1)
        tour.direita=quadros1
        zezinho.entra(quadros1)#zezinho ajeita o quadro e quando irá arrumar outro quadro e ele está muito pesado, ao tirar da parde encontra um cofre
        cofre = Cena(img = COFRE)# ESSE COFRE PRECISA TER UM HEREDPGRAMA PARA ABRIR
        #NAO ENTENDI A GAVETA COM LETRAS
        heredograma= Elemento( img = HEREDOGRAMA)# ESTAR COMO UM QUADRO
        #LEMBROU DE UMA AULA NA FIO CRUZ
        #OLHOU NOVAMENTO NO COFRE E TINHA UMAS LETRAS EMBARALHAS
        #ABRIU O COFRE E PEGOU UM PAPEL
        
        quadros1.direita=pergaminho
        pergaminho = Cena (img = PERGAMINHO)
        pergaminho.esquerda=quadros
        zezinho.entra(pergaminho)
        #informações sobre o heredograma
        
        biblioteca = Cena (img = BIBLIOTECA)
        pergaminho.direta= biblioteca
        livro = Elemento (img = LIVRO)
        livro.entra(biblioteca)
        #o livro irá abrir para uma pagina secreta
        
        sala = Cena (img = SALA)
        quadrado = Elemento (img = QUADRADO)
        quadrado1 = Elemento (img = QUADRADO1)
        circulo = Elemento (img = CIRCULO)
        dois_t = Elemento (img = DOIS_T)
        #FAZER COM QUE O JOGADOR POSSA MONTAR ESSE HEREDROGRAMA
        #COMADOS DE :ORGANIZE E MONTE
        # Rapidamente após de montar tudo, apareceu alguns nomes ao lado de cada desenho :
        #quadrado em branco - indivíduo do sexo masculino; esfera em branco - indivíduo do sexo feminino;
        # traço - casamento; quadrado com risco no meio - indivíduo falecido 
        # DEPOIS DE MONTAR APARECEU A PALAVRA MAPA
        
        # EM UMA ESCRIVANINHA APARECE UM MAPA 
        
        
        #APARECE UM OUTRO HEREDOGRAMA PARA ANALISAR
        #MONTAR UM HEREDROGRAMA COM AS INDICAÇOES ABAIXO
        
        
        
        
        casa.vai()
gameg()"""       
class MiniGameHerdograma:
"""Usa um editor de imagem (https://www.online-image-editor.com/) e recorta o Herdograma em linhas geracionais.
   No game, o jogador terá que clicar nas linhas em ordem certa para montar o herdograma corretamente.
"""
    def __init__(self):
        class LinhaGeracional:
        """Representa cada uma das linhas recortadas do herdograma original"""
            def __init__(self, linha, posicao):
                self.linha = Elemento(linha, x=posicao*200, y=10, w=200)
        class LinhaMontada:
            def __init__(self, linha):
                self.linha = Elemento(linha)
        
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
        cofre = Cena(img = COFRE)# ESSE COFRE PRECISA TER UM HEREDPGRAMA PARA ABRIR
        cofre.esquerda = quadros
        heredo = Elemento(HEREDOGRAMA, x=540, y= 370, w=200, tit="Esse heredograma é a pista!")
        heredo.entra(cofre)
        o_quadro = Elemento(QUADRADO, x=340, y= 270, tit="Esse quadro tem algo diferente", style={"opacity":0.05})
        o_quadro.vai = cofre.vai
        o_quadro.entra(quadros)
        pergaminho = Cena (img = PERGAMINHO)
        quadros1.direita=pergaminho
        pergaminho.esquerda=quadros
        biblioteca = Cena (img = BIBLIOTECA)
        pergaminho.direita= biblioteca
        livro = Elemento (img = LIVRO)
        livro.entra(biblioteca)
        casa.vai()
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
        
    def cofre(self, *_):
        self.heredograma.entra(self.cofre)#estar como um quadro
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
        
    def sala(self, *_):
        self.quadrado.entra(self.sala)
        self.quadrado1.entra(self.sala)
        self.circulo.entra(self.sala)
        self.zezinho.entra(self.sala)
        self.zezinho.entra.tit = "acho que eu preciso fazer algo com isso"
        self.sala.vai()
        """ http://supygirls.pythonanywhere.com/supygirls/gamer/henrietta/rachel""" #CÓDIGO DO QUEBRA CABEÇA
        #TENHO QUE FAZER UM DEF PARA CADA ELEMENTO?????
        
        
        #colocar o código do quebra cabeça para montar heredogramas com firguras geometricas separadas
        #FAZER COM QUE O JOGADOR POSSA MONTAR ESSE HEREDROGRAMA
        #COMADOS DE :ORGANIZE E MONTE
        # Rapidamente após de montar tudo, apareceu alguns nomes ao lado de cada desenho :
        #quadrado em branco - indivíduo do sexo masculino; esfera em branco - indivíduo do sexo feminino;
        # traço - casamento; quadrado com risco no meio - indivíduo falecido 
        """APARECER UMA uma chave"""
        def salax (self,*_):
        # montar um quebra cabeça 
        # Cientista contou 4 quadrados brancos, 2 esferas brancas e 1 preta,
        #e 7 traços. Depois de ter encaixado as peças, formou esta imagem como resposta:
        # quando terminou apareceu a palavra mapa
           self.salax.vai()
        
        #fazer uma fase de transição ao achar o mapa e procurar alguns quartos
        def quartos2(self,*_):
            #quebra cabeça
            # Figuras geométricas/Traços (simples, duplos, triplos)
            #Casamento cosanguineo/Quatro indivíduas/Dois com anomalias/Dois normais do sexo masculino
            #dar um motivo para fazer esse quebra cabeça
            self.quartos2.vai()
        def ajuda(self,*_):
            # data:image/png;base64,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
            # ter essa imagem e aconselhar o casal.
            #motivo ajudar o casal
            self.ajuda.vai()
        def ultimaparte(self,*_):
            #volta para sala(onde tem o monitor
            #para ter acesso ao computador precisa criar um heredograma
            #quebra cabeça 
            #informções que precisa saber
            #Homem/Mulher/Aborto/União Múltipla/Cosanguinidade/Mulher/Adotado pela família/Natimorto
            #motivo destravar o computador
            self.ultimarparte.vai()
        
        
        
gameg()        
        
        
