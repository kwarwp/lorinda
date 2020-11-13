# lorinda.samantha.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE

# from _spy.vitollino.main import inventario as inv

STYLE["width"] = 900
STYLE["height"] = '650px'

FLAVINHO = "https://imgur.com/fv9BZ54.jpg"
FOTO_PRINCIPAL = "https://imgur.com/NTZqSBD.jpg"
DALMACIA = "https://imgur.com/dyLIQib.jpg"
JERONIMO_JOVEM = "blob:https://web.whatsapp.com/edad8633-e384-4538-b7f3-ddd4837df1c0"
FUNDO_PERGUNTAS = "https://imgur.com/w7OnO7L.jpg"
CURIOSIDADE = ""
LEAO = "https://1.bp.blogspot.com/-59thFerIMG4/VglSIs30pcI/AAAAAAAAIXE/EI8WJS59Xv0/s1600/sao-jeronimo11.jpg"
PAPA_LIBERIO = "https://imgur.com/vlIrMHW.jpg"
BATIZADO_JERONIMO = ""
ROMA = "https://imgur.com/Zh5yUpP.jpg"
ORDDENACAO_SACERDOTAL = "https://imgur.com/qZ3zINX.jpg"
#SONHO = "blob:https://web.whatsapp.com/2960c698-2f09-4eff-abd9-6ee5d4b7ee47"
SONHO = "https://i.imgur.com/uHw57i1.jpg"
JERONIMO_CAVERNA = ""
BIBLIA = "https://imgur.com/QPELbOd.jpg"
VULGATA = "https://i.imgur.com/Uyy86ge.jpg"
BELEM = "https://imgur.com/sf5X4cr.jpg"
FOTO_DO_PADROEIRO = "https://imgur.com/Y0CZrXO.jpg"
FRASE = "https://imgur.com/LR9Tnyf.jpg"
CENA_FINAL = "https://imgur.com/kRQyK02.jpg"
PAPAD = "https://i.imgur.com/tav4zK0.jpeg"
CAVERNA = "https://imgur.com/fBFCru5.jpg"
FOTO_PAROQUIA = "https://imgur.com/zFwNqPr.jpg"


class Bala:
    def __init__(self):
        self.ft = Cena(img=FOTO_PAROQUIA)
        self.leao = Cena(img=LEAO)
        self.padre = Elemento(img=FLAVINHO)
        self.f_t = Cena(img=FOTO_PRINCIPAL)
        self.dalmacia = Cena(img=DALMACIA)
        self.j_j = Elemento(img=JERONIMO_JOVEM)
        self.ft_p = Cena(img=FUNDO_PERGUNTAS)
        self.batizado = Cena(img=BATIZADO_JERONIMO)
        self.roma = Cena(img=ROMA)
        self.ordenacao = Cena(img=ORDDENACAO_SACERDOTAL)
        self.sonho = Cena(img=SONHO)
        self.cr = Cena(img=CURIOSIDADE)
        self.caverna = Cena(img=CAVERNA)
        #self.pl = Elemento(img=PAPA_LIBERIO)
        self.pl = Cena(img=PAPA_LIBERIO)
        self.j_c = Cena(img=JERONIMO_CAVERNA)
        self.biblia = Cena(img=BIBLIA)
        self.vulgata = Cena(img=VULGATA)
        self.belem = Cena(img=BELEM)
        self.f_p = Cena(img=FOTO_DO_PADROEIRO)
        self.frase = Cena(img=FRASE)
        self.cf = Cena(img=CENA_FINAL)
        #self.pd = Elemento(img=PAPAD)
        self.pd = Cena(img=PAPAD)
        self.f_t.vai()
        self.entrou_padre()
        self.entrou_10()

    def entrou_padre(self, *_):
        
        self.padre.entra(self.f_t)
        Texto(self.f_t, "Olá pessoal, certinho?" ).vai()
        self.padre.vai = Texto(self.f_t,
                               "Eu sou o Padre Flávio e vou te ajudar nessa aventura sobre a história do nosso amado padroeiro",
                               foi=self.entrou_1).vai

    def entrou_1(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.ft_p, "Ele irá a Roma."),
                B=Texto(self.ft_p, "Correto!", foi=self.entrou_dalmacia),
                C=Texto(self.ft_p, "Muitos santos são da Polônia, mas São Jerônimo não foi um deles."),
            )
            respondeu[optou].vai()

        self.ft_p.vai()
        self.padre.entra(self.ft_p)
        self.padre.vai = Texto(self.ft_p, "Sabe onde Jerônimo nasceu?",
                               foi=resposta, A="Roma", B="Dalmácia", C="Polônia").vai

    def entrou_dalmacia(self, *_):
        self.padre.entra(self.dalmacia)
        self.padre.vai = Texto(self.dalmacia, "São Jerônimo nasceu na Dalmácia no ano de 340.", foi=self.entrou_2).vai
        self.dalmacia.vai()

    def entrou_2(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.roma, "Parabéns! Você acertou", foi=self.entrou_3),
                B=Texto(self.roma, "Essa grave doença veio depois."),
                C=Texto(self.roma, "O sonho aconteceu em Roma"),
            )
            respondeu[optou].vai()

        self.ft_p.vai()
        self.padre.entra(self.ft_p)
        acontecimento = Texto(self.roma, "Após qual acontecimento ele foi para Roma estudar?",
                               foi=resposta, A="A morte de seus pais", B="Uma grave doença", C="Um sonho")
        self.ft_p.vai()
        self.padre.entra(self.roma)
        self.padre.vai = Texto(self.roma,
                               "Após a morte de seus pais, Jerônimo foi para Roma estudar e durante sua permanencia teve um sonho muito importante para sua conversão."
                               , foi=acontecimento.vai).vai
        self.roma.vai()

    def entrou_3(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.sonho, "Também seria uma honra, mas não foi com nossa mãezinha."),
                B=Texto(self.sonho, "O Aracanjo não estava presente no sonho!"),
                C=Texto(self.sonho, "Você acertou", foi=self.entrou_4)
            )
            respondeu[optou].vai()
            # self.ft_p.vai()

        self.padre.entra(self.ft_p)
        sonhou = Texto(self.sonho, "Você consegue adivinhar com quem foi esse sonho?",
                               foi=resposta, A="Nossa Senhora", B="São Miguel", C="Jesus Cristo").vai
        self.padre.entra(self.sonho)
        self.padre.vai = Texto(self.sonho,
                               "No sonho, Jerônimo apresentava-se como cristão e era repreedindo pelo próprio Cristo por estar faltando com a verdade.",
                               foi = sonhou).vai
        self.sonho.vai()
    def entrou_4(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.pl,"Não tinha nascido" ),
                B=Texto(self.pl,"Acertou", foi=self.entrou_5),
                C=Texto(self.pl,"Não tinha nascido" )
            )
            respondeu[optou].vai()

        self.padre.entra(self.ft_p)
        batizou = Texto(self.pl, "Qual destes Papas batizou nosso padroeiro?",
                               foi=resposta, A="Papa Francisco", B="Papa Libério", C="Papa Bento XVI").vai
        self.padre.entra(self.pl)
        self.padre.vai = Texto(self.pl,
                               "Aos 25 anos de idade Jerônimo foi batizado pelo Papa no fim de sua permanencia em Roma.",
                               foi = batizou).vai
        self.pl.vai()

    def entrou_5(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.ordenacao, "OOps"),
                B=Texto(self.ordenacao, "Acertou", foi= self.ordenado),
                C=Texto(self.ordenacao, "OOps"),
            )
            respondeu[optou].vai()

        self.ft_p.vai()
        self.padre.entra(self.ft_p)
        self.padre.vai = Texto(self.ordenacao, "Você sabe em qual ano São Jerônimo foi ordenado sacerdote?",
                               foi=resposta, A="356", B="379", C="450").vai
        self.padre.entra(self.ordenacao)
        self.ordenado = Texto(self.ordenacao,
                               "Jerônimo foi ordenado sacerdote no ano de 379, retirando-se para dedicar-se ao estudo.",
                               foi=self.entrou_6).vai
        self.ordenacao.vai()

    def entrou_6(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.pd, "Acertou", foi=self.damaso),
                B=Texto(self.pd, "Nope"),
                C=Texto(self.pd, "Nope"),
            )
            respondeu[optou].vai()

        self.padre.vai = Texto(self.pd, "A pedido de qual papa Jerônimo traduziu as escrituras?",
                               foi=resposta, A="Papa Damaso", B="Papa João Paulo II", C="Papa Leão XII").vai
        self.padre.entra(self.pd)
        self.damaso = Texto(self.pd,
                               "Por ter aprendido as linguas originais para melhor compreender as escrituras, Nosso padroeiro pôde a pedido do Papa Damaso traduzir as escrituras para o Latim.",
                               foi=self.entrou_7).vai
        self.pd.vai()
    def entrou_7(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.biblia, "sqn"),
                B=Texto(self.biblia, "Acertou", foi=self.escrituras),
                C=Texto(self.biblia, "sqn"),
            )
            respondeu[optou].vai()

        self.padre.vai = Texto(self.biblia, "De quais línguas foi traduzida a Sagrada Escritura? ",
                               foi=resposta, A="Chinês, Inglês e Português.", B="Grego, Hebraico e Aramaico.",
                               C="Russo, Espanhol e latim.").vai
        self.padre.entra(self.biblia)
        self.escrituras = Texto(self.biblia, "As escrituras foram traduzidas do grego, hebraico e aramaico.",foi=self.entrou_8).vai
        self.biblia.vai()

    def entrou_8(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.vulgata, "não acertou"),
                B=Texto(self.vulgata, "poxa, não é"),
                C=Texto(self.vulgata, "isso mesmo, esta sabendo!", foi=self.traducao),
            )
            respondeu[optou].vai()

        
        self.padre.vai = Texto(self.vulgata, "Qual nome recebeu a tradução da biblía?",
                               foi=resposta, A="Livro", B="Enciclopédia", C="Vulgata").vai
        self.padre.entra(self.vulgata)
        self.traducao = Texto(self.vulgata, "A tradução da sagrada escritura recebeu o nome Vulgata.", foi=self.entrou_9).vai
        self.vulgata.vai()
    def entrou_9(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.belem, "isso mesmo", foi=self.traduzir),
                B=Texto(self.belem, "ainda não"),
                C=Texto(self.belem, "não foi "),
            )
            respondeu[optou].vai()

       
        self.padre.vai = Texto(self.belem, "Para onde Jerônimo mudou-se após traduzir a Biblía?",
                               foi=resposta, A="Belém", B="Egito", C="Índia").vai
        self.padre.entra(self.belem)
        self.traduzir = Texto(self.belem,
                               "Após traduzir a sagrada escritura , Jerônimo mudou-se para Belém a cidade onde nasceu nosso Salvador.",
                              foi=self.entrou_10 ).vai
        self.belem.vai()
    def entrou_10(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.f_p, "depois"),
                B=Texto(self.f_p, "sim", foi=self.morte),
                C=Texto(self.f_p, "foi depois"),
            )
            respondeu[optou].vai()


        self.padre.vai = Texto(self.f_p, "Em qual dia comemoramos o dia de São Jerônimo?",
                               foi=resposta, A="01 de setembro", B="30 de outubro", C="30 de setembro").vai
        self.padre.entra(self.f_p)
        self.morte = Texto(self.f_p,
                               "Jerônimo morreu no dia 30 de setembro de 420 em Belém, por isso o dia da Biblía e de São Jerônimo são comemorados no dia 30 de setembro."
                               ,foi=self.entrou_11).vai
        self.f_p.vai()
    def entrou_11(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.leao, "nao"),
                B=Texto(self.leao, "sim", foi=self.animal),
                C=Texto(self.leao, "não"),
            )
            respondeu[optou].vai()

        
        self.padre.vai = Texto(self.leao, "Qual o animal podemos encontar ao lado de São Jerônimo?",
                               foi=resposta, A="sapo", B="leão", C="cordeiro").vai
        self.padre.entra(self.leao)
        self.animal = Texto(self.leao, "É um leão!!",foi=self.entrou_12).vai
        self.leao.vai()
    def entrou_12(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.ft_p, "O autor desta frase é João Paulo II"),
                B=Texto(self.ft_p, "Esta frase é pensamento de Santa Teresinha"),
                C=Texto(self.ft_p, "Correto!!"),
            )
            respondeu[optou].vai()

        self.ft_p.vai()
        self.padre.entra(self.ft_p)
        self.padre.vai = Texto(self.ft_p, "Qual destas é uma frase de São Jerônimo",
                               foi=resposta,
                               A="Depositemos sempre a nossa confiança no Espírito Santo, para descobrirmos em cada situação nova uma ocasião para alargar o amor redentor de Cristo.",
                               B="O bom Deus, que conhece as recompensas que Ele reserva a seus amigos, gosta, muitas vezes, de fazê-los ganhar seus tesouros por meio de sacrifícios",
                               C="Ignorar as Escrituras Sagradas é ignorar a Cristo.").vai
        self.padre.entra(self.frase)
        self.padre.vai = Texto(self.frase,
                               "A frase mais conhecida de nosso padroeiro é:  Ignorar as Escrituras Sagradas é ignorar a Cristo").vai
    
    
    def entrou_final(self, *_):
        self.padre.entra(self.cf)
        self.padre.vai = Texto(self.cf,
                               "Espero que tenham gostado de aprender um pouco mais da história do nosso amdado padroeiro São Jerônimo!").vai
        self.padre.vai = Texto(self.cf, " Até a próxima !!!").vai


Bala()
