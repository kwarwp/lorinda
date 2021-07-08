# lorinda.adda.main.py
#jogo do centro espírita sobre Jesus(Leniah)
from _spy.vitollino.main import Cena, Sala, Labirinto, Elemento, Texto, STYLE, INVENTARIO as inv
STYLE.update(width=900, height="650px")

JESUS= ""
LUGAR1= ""
LUGAR2=""
LUGAR3=""
LUGAR4=""
LUGAR5=""
LUGAR6=""
LUGAR7=""
MARIA=""
JOSE=""
AMIGOS=""
PERSONAGEM=""

class Jesus:
    def __init__(self):
        self.lugar1=Cena(img=LUGAR1)
        self.lugar2=Cena(img=LUGAR2)
        self.lugar3=Cena(img=LUGAR3)
        self.lugar4=Cena(img=LUGAR4)
        self.lugar5=Cena(img=LUGAR5)
        self.lugar6=Cena(img=LUGAR6)
        self.lugar7=Cena(img=LUGAR7)
        self.jesus=Elemento(img=JESUS)
        self.personagem=Elemento(img=PERSONAGEM)
        
        self.personagem.entra(self.lugar1)
        self.lugar1.vai()
        self.Primeira_pergunta.vai()
        
    def Primeira_pergunta()
        self.personagem.entra(self.lugar1)
        Texto(self.lugar1, "Olá pessoal, certinho?" ).vai()
        self.personagem.vai = Texto(self.lugar1,
                               "Eu sou xx e vou te ajudar nessa aventura sobre a história de alguém que veio para nos ensinar muito amor",
                               foi=self.entrou_1).vai
    def entrou_1(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.lugar1, "Alguém que nos ensinou a amar."foi=self.entrou_nasceu),
                B=Texto(self.lugar1, "alguém que mostrou as riquezas", ),
                C=Texto(self.lugar1, "xxxx"
            )
            respondeu[optou].vai()

        self.lugar1.vai()
        self.personagem.entra(self.ft_p)
        self.personagem.vai = Texto(self.lugar1, "quem é jesus?",
                               foi=resposta, A="um Humano", B="uma luz", C="amigo").vai
       
      def entrou_nasceu()
         self.personagem.entra(self.lugar2)
         self.personagem.vai = Texto(self.lugar2, "São Jerônimo nasceu na Dalmácia no ano de 340.", foi=self.entrou_2).vai
         self.lugar2.vai()
      def entrou_2(self, *_):
        def resposta(optou):
            respondeu = dict(
                A=Texto(self.lugar2, "Parabéns! Você acertou"),
                B=Texto(self.lugar2, "Essa grave doença veio depois."foi=self.entrou_3),
                C=Texto(self.lugar2, "O sonho aconteceu em Roma"),
            )
            respondeu[optou].vai()

        self.lugar2.vai()
        self.personagem.entra(self.lugar2)
        acontecimento = Texto(self.lugar2, "Onde foi que jesus nasceu?",
                               foi=resposta, A="Belém", B="Jerusalém", C="Nazaré")
        self.lugar2.vai()
        self.personagem.entra(self.lugar2)
        self.personagem.vai = Texto(self.lugar2,
                               " os pais de Jesus estavam em Belém ,Jerusalem foi depois do nascimento"
                               , foi=acontecimento.vai).vai
        self.lugar2.vai()
        


