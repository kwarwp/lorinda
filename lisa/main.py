# lorinda.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"
SETA = "https://i.imgur.com/N3JNtRW.png"
GRUPO_ESTUDANTES="https://i.imgur.com/jIEEVl7.png"
DRA_ROSALIND="https://i.imgur.com/sBZyLaX.jpg"
EQUIPAMENTO="https://i.imgur.com/ANZw77S.png"
ABERTURA="https://i.imgur.com/g3wt0Vb.jpg"
LABORATORIO="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/InvestigadoresUR.JPG/350px-InvestigadoresUR.JPG"
RUA= "https://i.imgur.com/GAoOTwn.jpg"
#ESTRANHA= "https://i.imgur.com/o2iRg01.png"
ESTRANHA= "https://i.imgur.com/f1dGlgQ.png"
CASA= "https://i.imgur.com/pi9jHVf.png"
PACOTE = "https://i.imgur.com/ZwnOqUW.jpg"
RUA2 = "https://i.imgur.com/063NauC.jpg"
MARIA = "https://i.imgur.com/FukdPW2.jpg"
FIOCRUZ = "https://i.imgur.com/Fins20m.jpg"
CHEFE = "https://imgur.com/eAp7OQu.jpg"
CORREDOR = "https://i.imgur.com/7GyqLni.jpg"
LAMINA = "https://www.splab.com.br/imagens/informacoes/lamina-vidro-escavada-02.jpg"
LABORATORIO ="https://i.imgur.com/b6P8IWp.jpg"
MICROSCOPIO = "https://imgur.com/Mqzusew.jpg"
CARTAZ = "https://png.pngtree.com/element_our/png_detail/20181226/mockup-design-vector-poster-company-sample-concep-illustration-wave-png_282401.jpg"
CELULA = "https://i.imgur.com/sGoKfvs.jpg" #MUDE, COLOQUEI QQ COISA!
NEURONIO = "https://imgur.com/YK4fgSr.jpg"
HEMACIA = "https://imgur.com/6sZ3B2K.jpg"
PROCARIONTE = "https://i.pinimg.com/originals/fb/b9/c8/fbb9c8a5078a5417ecd182f2cb512909.jpg"
BACTERIA= "https://imgur.com/ifgaFEO.jpg"
TRYPANOSOMA_CRUZI = "https://imgur.com/ccjY50N.jpg"
ESPERMATOZOIDE = "https://imgur.com/RD0Fe3X.jpg"
ELODEA = "https://img1.gratispng.com/20180404/jkq/kisspng-algae-seaweed-aquatic-plants-aloe-5ac4853e2c61d2.8993360815228286061818.jpg"
CALCIFORME = "https://imgur.com/2kY3sBX.jpg"
NPC = "https://imgur.com/VcPXMYC.png"
CICLONE = "https://i.imgur.com/BC6X7ho.gif"

#colocar imagens da class apresentação 
class apresentacao():
    def __init__(self):
        self.casa = Cena(img = CASA)#maria vai para fio cruz
        self.maria= Elemento(img= MARIA, x=300, y=300, w=350, h=250)
        self.rua= Cena(img= RUA)
        self.estranha= Elemento(img= ESTRANHA, x=600, y=400, texto= "Guarde e proteja esse pacote com sua própria vida. Nele tem um mistério que só você poderá desvendar.")
        self.pacote=Elemento(img=PACOTE, x=760, y=450) #, tit="pacote")
        self.casa.direita=Cena(vai=self.entrou_rua)#self.rua
        self.rua.esquerda=self.casa
        #maria.entra(rua)
        #coloquei .vai() em alguns
        #maria.entra(rua) 
        self.rua2=Cena(img= RUA2)
        #self.rua.direita= self.rua2
        self.rua.direita=Cena(vai=self.entrou_rua2)
        self.rua2.esquerda=self.rua
        #maria.entra(rua2)
        self.estranha.entra(self.rua2)#entrega o pacote e some
        #self.pacote=Elemento(img= PACOTE)
        self.fiocruz= Cena(img=FIOCRUZ)
        self.pacote.entra(self.rua2)
        self.rua2.direita=self.fiocruz
        self.fiocruz.esquerda=self.rua2
        self.chefe=Elemento(img=CHEFE, x=560, y=450)
        self.laboratorio= Cena(img= LABORATORIO)
        self.cartaz=Elemento(CARTAZ, x=400)
        self.microscopio = Elemento(img = MICROSCOPIO, x=760, y=350)
        # cartaz= Elemento(img= CARTAZ)
        #chefe.entra(fiocruz)
        #será que assim vai? colocar separado? mas se colocar assim os dois textos vão aparecer
        #juntos, não
        #maria abre o pacote e encontra uma lâmina
        self.lamina=Elemento(img= LAMINA)
        #maria vai para um laboratório, mas antes passa por um corredor
        self.corredor= Cena(img= CORREDOR)
        self.fiocruz.direita= self.corredor
        self.corredor.esquerda=self.fiocruz
        self.celula= Cena(img= CELULA)#QUANDO CLICA NO MICRÓSCÓPIO IRÁ PARA ESSA CENA
        #self.casa.foi=self.entrou_maria
        Texto(self.casa, "Maria hoje tem um compromisso. Ela não sabe, mas vai viver uma experiência extraordinária.", foi=self.entrou_maria).vai()
    def entrou_maria(self,*_):
        self.maria.entra(self.casa)
        self.maria.vai= Texto(self.casa,
        " Olá! Me chamo Maria. Amo estudar biologia e lutar pelos direitos das mulheres.",
        foi=self.entrou_rua).vai
    def entrou_rua(self,*_):
        self.rua.vai()
        self.maria.entra(self.rua)
        self.maria.vai= Texto(self.rua, 
        "Estou indo para FIOCRUZ, acho que vou conseguir um estágio lá, uip",
        foi=self.entrou_rua2).vai
    def entrou_rua2(self,*_):
        self.rua2.vai()
        self.maria.entra(self.rua2)
        pega= Texto(self.rua2, 
        "Mas estou muito curiosa, vou abrir depois .",
        foi=self.entra_fiocruz)
        self.maria.vai= Texto(self.rua2, 
        " Que pessoa estranha, não quero nada aceitar dela",
        foi=pega.vai).vai
    def entra_fiocruz(self,*_):
        self.fiocruz.vai()
        self.chefe.entra(self.fiocruz)
        self.chefe.vai= Texto(self.fiocruz, "Boa tarde, Maria! Temos um tempo antes da entrevista. Fique à vontade, se quiser, pode explorar os laboratórios para estudar.").vai
        self.maria.entra(self.fiocruz)
        self.maria.vai=Texto(self.fiocruz,
        "Nossa! Uma lâmina! Tenho um tempo antes da entrevista do estágio, vou procurar um laboratório",
        foi=self.entrou_laboratorio).vai
    def entrou_laboratorio(self,*_):
        self.laboratorio.vai()
        self.maria.entra(self.laboratorio)
        self.maria.vai= Texto(self.laboratorio, 
        "Aqui tem uns equipamentos para ver essa lâmina, escolha qual vc acha melhor",
        foi=self.entrou_lamina).vai
    def entrou_lamina(self,*_):
        self.lamina.entra(self.laboratorio)
        self.lamina.vai= Texto(self.laboratorio, 
        " O que será que tem nessa lâmina?",
        foi=self.entrou_cartaz).vai
   
    def entrou_cartaz(self,*_):
        self.cartaz.entra(self.laboratorio)
        self.cartaz.vai=Texto(self.laboratorio, 
        "Um laboratório é um local que deve ser utilizado com muita responsabilidade. Existem normas de segurança que precisam ser seguidas, no laboratório há reagentes químicos e aparelhos, que se usados de maneira errada podem causar acidentes",
        foi=self.entrou_microscopio).vai
    def entrou_microscopio(self,*_):
        self.microscopio.entra(self.laboratorio)
        self.microscopio.vai= Texto(self.laboratorio, "  Neste laboratório tem vários microscópios, microscópios ópticos e também eletrônico. Você pode utiliza-los para descobrir o que tem nessa lâmina.",
        foi=self.ciclone).vai
        #foi=Fase1(self.maria).vai).vai
    def ciclone(self, *_):
        self.redemoinho = Elemento(CICLONE, x=0, y=0, w=600, h=600, o=0.8, cena=self.laboratorio,
        style= {"transition": "left 6s"})
        self.redemoinho.elt.ontransitionend = Fase1(self.maria).vai
        self.maria_double=Elemento(img=MARIA, x=300, y=300, w=350, h=250, cena=self.laboratorio,
        style= {"transition": "left 6s, transform 1s"})
        Texto(self.laboratorio, 
        "Eita! O que será este redemoinho que apareceu do nada no laboratório?",foi=self.anda_redemoinho).vai()
        
    def anda_redemoinho(self, _=0):
        self.redemoinho.x = 1500
        self.maria.x = 1500
        self.maria_double.x = 1500
        self.maria_double.elt.style.transform = "rotate(300deg)"
    def vai(self):

    
       self.casa.vai()
apresentacao()
#print (apresentacao)
#PROCARIONTE = TRYPANOSOMA_CRUZI = NEURONIO = BACTERIA = "https://i.imgur.com/illvVvw.jpg"
#ESPERMATOZOIDE = HEMACIA = ELODEA = CALCIFORME = NPC = "https://i.imgur.com/illvVvw.jpg"
class Fase0(): 
    def __init__(self, maria=None):
        self.laboratorio= Cena(img =  ABERTURA)
        self.seta = Elemento(SETA, x=300, y=400, w=400, cena=self.laboratorio, vai=self.segue)
    def vai(self, *_):
        self.laboratorio.vai()
        t = Texto(self.laboratorio, "Aprenda a jogar. Olá! Agora iremos começar uma grande aventura...Para isso, preciso que prestem bastante atenção!! Toda vez que aparecer um personagem e não aparecer uma caixinha como essa, é só passar o mouse por cima do personagem ou elemento e lembre-se, sempre comece pela Maria, ela é o personagem principal.")
        t.vai()
    def segue(self, *_):
        apresentacao().vai()
class Fase1(): 
    def __init__(self, maria=None):
        self.laboratorio= Cena(img =  LABORATORIO)
        self.celula = Cena(CELULA)
        self.maria=maria or Elemento(img= MARIA, x=460, y=450, w=150, h=80)
        self.procarionte= Elemento(img= PROCARIONTE, x=100, y=100)
        self.trypanosoma_cruzi= Elemento(img=TRYPANOSOMA_CRUZI, x=200, y=0)
        self.neuronio=Elemento(img= NEURONIO, x=300, y=100)
        self.bacteria = Elemento(img= BACTERIA)
        self.espermatozoide= Elemento(img=  ESPERMATOZOIDE) 
        self.hemacia= Elemento(img= HEMACIA)
        self.elodea= Elemento(img= ELODEA)
        self.calciforme= Elemento(img=CALCIFORME)
        self.npc= Elemento(img= NPC,texto = "Para começar a sua missão, você precisa passar por uma estrutura muito relevante para a célula. É ela quem tem a função de proteger, delimitar, transportar e selecionar as substâncias que entram e saem da célula. Você sabia que as células presentes nos seres vivos são classificadas em eucariontes e procariontes? Mas para seguir adiante, você precisa clicar na célula procarionte", cena=self.laboratorio)#resposta certa é a bactéria
        self.npc.texto.foi = self.entrou_celula
    """
    def entrou_procarionte(self, *_):
        self.procarionte.entra(self.laboratorio)
        self.procarionte.vai=Texto(self.laboratorio,
        " oi eu sou uma célula procarionte,e me chama assim pq eu tenho apenas uma célula no meu corpo",
        foi=self.entrou_trypanosoma).vai
    def entrou_trypanosoma(self, *_):
        self.trypanosoma_cruzi.entra(self.laboratorio)
        self.trypanosoma_cruzi.vai=Texto(self.laboratorio,
        "a galera não gosta muito de mim pq dizem que eu sou parasita e que causa uma doença no coração, mas é que o coração grande é tão quentinho",
        foi=self.entrou_neuronio).vai
    def entrou_neuronio(self, *_):
        self.neuronio.entra(self.laboratorio)
        self.neuronio.vai=Texto(self.laboratorio,
        "eus ou bem complicado, pois eu fico na cabeça e passo informação pelo corpo, imagina como eu devo ser feito",
        foi=self.entrou_bacteria).vai
    def entrou_bacteria(self, *_):
        self.bacteria.entra(self.laboratorio)
        self.bacteria.vai=Texto(self.laboratorio,
        "olá eu sou uma pessoa simples, igual arroz pois combino com tudo e posso estar em qualquer lugar, sempre tem espaço para mim",
        foi=self.entrou_espermatozoide).vai
    def entrou_espermatozoide(self, *_):
        self.espermatozoide.entra(self.laboratorio)
        self.espermatozoide.vai=Texto(self.laboratorio,
        "eu sou quem dá a origem dos humanos, então imagina como devo ser dificil e complexo me estudar",
        foi=self.entrou_hemacia).vai
    def entrou_hemacia(self, *_):
        self.hemacia.entra(self.laboratorio)
        self.hemacia.vai=Texto(self.laboratorio, 
        "eu sou o transporte da galera, carrego muita coisa, imagina como sou",
        foi=self.entrou_elodea).vai
    def entrou_elodea(self, *_):
        self.elodea.entra(self.laboratorio)
        self.elodea.vai= Texto(self.laboratorio,
        "eu vivo na agua e sou muito importante para a manutenção do ambiente marinho, posso ser encoderijo , comida ou o2",
        foi=self.entrou_calciforme).vai
    def entrou_calciforme(self, *_):
        self.calciforme.entra(self.laboratorio)
        self.calciforme.vai=Texto(self.laboratorio,
        "eu fico no instestino delgado eu tenho diversas funções, uma dela pe revestir com muco para proteger onde estou",
        foi=self.entrou_celula).vai"""
    def entrou_celula(self, *_):
        self.celula.vai()
        self.maria.entra(self.celula)
        self.maria.vai=Texto(self.celula, "ONDE ESTOU?", foi=self.faladepois1).vai
        self.npc.entra(self.celula)
        self.npc.vai=Texto(self.celula, " Na cidade das células! CITONÓPOLIS", foi=self.faladepois2).vai
    def faladepois1(self,*_):
        self.maria.vai=Texto(self.celula,"Como posso sair desse lugar?").vai
    def faladepois2(self,*_):
        from libby.main import Fase2
        self.npc.vai=Texto(self.celula,"  Você foi trazida para outra dimensão, a dimensão microscópica das células. Para você sair terá que vencer alguns enigmas e desafios relacionados ao mundo das células ou ficará presa aqui para sempre.", foi=Fase2).vai 
    def vai(self, *_):

        self.laboratorio.vai()
        self.maria.entra(self.laboratorio)
        #self.celula.vai()
#Fase1().vai()
#apresentacao().vai()
Fase0().vai()
#print(Fase1)



