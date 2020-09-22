# lorinda.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"
GRUPO_ESTUDANTES="https://i.imgur.com/jIEEVl7.png"
DRA_ROSALIND="https://i.imgur.com/sBZyLaX.jpg"
EQUIPAMENTO="https://i.imgur.com/ANZw77S.png"
LABORATORIO="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/InvestigadoresUR.JPG/350px-InvestigadoresUR.JPG"
RUA= "https://i.imgur.com/GAoOTwn.jpg"
ESTRANHA= "https://i.imgur.com/o2iRg01.png"
CASA= "https://i.imgur.com/pi9jHVf.png"
PACOTE = "https://i.imgur.com/ZwnOqUW.jpg"
RUA2 = "https://i.imgur.com/063NauC.jpg"
MARIA = "https://i.imgur.com/OsN5Mxj.png"
FIOCRUZ = "https://i.imgur.com/Fins20m.jpg"
CHEFE = "https://i.imgur.com/kAaFiwg.png"
CORREDOR = "https://i.imgur.com/7GyqLni.jpg"
LAMINA = "https://www.splab.com.br/imagens/informacoes/lamina-vidro-escavada-02.jpg"
LABORATORIO ="https://i.imgur.com/b6P8IWp.jpg"
MICROSCOPIO = "https://i.imgur.com/IA1JT2z.png"
#COMO SERIA ESSE CARTAZ??
CARTAZ = ""
CELULA = ""
#colocar imagens da class apresentação 
class apresentacao():
    def __init__(self):
        casa = Cena(img = CASA)#maria vai para fio cruz
        maria= Elemento(img= MARIA, x=460, y=250, w=150, h=80)
        rua= Cena(img= RUA)
        estranha= Elemento(img= ESTRANHA, texto= "Guarde e proteja esse pacote com sua própria vida")
        pacote=Elemento(img=PACOTE)
        casa.direta=rua
        rua.esquerda=casa
        #maria.entra(rua)
        #coloquei .vai() em alguns
        #maria.entra(rua) 
        rua2=Cena(img= RUA2)
        rua.direita= rua2
        rua2.esquerda=rua
        #maria.entra(rua2)
        estranha.entra(rua2)#entrega o pacote e some
        pacote=Elemento(img= PACOTE)
        fiocruz= Cena(img=FIOCRUZ)
        pacote.entra(rua2)
        rua2.direta=fiocruz
        fiocruz.esquerda=rua2
        chefe=Elemento(img=CHEFE)
        laboratorio= Cena(img= LABORATORIO)
        #microscopio = Elemento(img = MICROSCOPIO)
        # cartaz= Elemento(img= CARTAZ)
        #chefe.entra(fiocruz)
        #será que assim vai? colocar separado? mas se colocar assim os dois textos vão aparecer
        #juntos, não
        #maria abre o pacote e encontra uma lâmina
        lamina=Elemento(img= LAMINA)
        #maria vai para um laboratório, mas antes passa por um corredor
        corredor= Cena(img= CORREDOR)
        fiocruz.direita= corredor
        corredor.esquerda=fiocruz
        celula= Cena(img= CELULA)#QUANDO CLICA NO MICRÓSCÓPIO IRÁ PARA ESSA CENA
        

    def entrou_maria(*_):
        maria.entrou(casa)
        maria.vai= Texto(casa," olá me chamo Maria e amo estudar biologia e lutar pelos direitos das mulheres")
    def entrou_rua(*_):
        maria.entrou(rua)
        maria.vai= Texto(rua, "estou indo para FIOCRUZ, acho que vou conseguir um estágio lá, uip")
    def entrou_rua2(*_):
        maria.entra(rua2)
        maria.vai= Texto(rua2, "parece uma pessoa estranha, não quero aceitar nada dela")
    def entra_fiocruz(*_):
        chefe.entra(fiocruz)
        chefe.vai= Texto(fiocruz, "Boa tarde Maria, temos um tempo antes da entrevista, fique a vontade...se quiser pode explorar os laboatórios para estudar")
        maria.entra(fiocruz)
        maria.vai=Texto(fiocruz,"nossa um pedaço de vidro, tenho um tempo antes da entrevista do estagio a moça disse que eu poderia ficar nos laboratórios estudando")
    
    def entrou_laboratorio(*_):
        maria.entra(laboratorio)
        maria.vai= Texto(laboratorio, "aqui tem uns equipamentos para ver esse vidro, escolha qual vc acha melhor")
    def entrou_lamina(*_):
        lamina.entra(laboratorio)
        lamina.vai= Texto(laboratorio,  "nossa um pedaço de vidro, tenho um tempo antes da entrevista do estagio a moça disse que eu poderia ficar nos laboratórios estudando")
    def entrou_microscopio(*_):
        microscopio.entra(laboratorio)
        microscopio.vai= Texto(laboratorio, " olá, eu sou utilizado para ver coisas que o olho humano não ve ")
    """ colocar outros equipamentos de laboratório"""
    def entrou_cartaz(*_):
        cartaz.entra(laboratorio)
        cartaz.vai=Texto(laboratorio, "para se usar o microscópio faça isso...")
    
        """arrastar e colocar a lâmina no microscópio e então aparece um um ciclone que a leva para dentro da célula, 
        ela grita e pergunta onde estou""" 
    

#apresentacao()
#print (apresentacao)
PROCARIONTE = TRYPANOSOMA_CRUZI = NEURONIO = BACTERIA = "https://i.imgur.com/illvVvw.jpg"
ESPERMATOZOIDE = HEMACIA = ELODEA = CALCIFORME = NPC = "https://i.imgur.com/illvVvw.jpg"
class Fase1(): 
    def __init__(self):
        self.laboratorio= Cena(img =  LABORATORIO)
        self.procarionte= Elemento(img= PROCARIONTE, x=100, y=100)
        self.trypanosoma_cruzi= Elemento(img=TRYPANOSOMA_CRUZI, x=200, y=0)
        self.neuronio=Elemento(img= NEURONIO, x=300, y=100)
        self.bacteria = Elemento(img= BACTERIA)
        self.espermatozoide= Elemento(img=  ESPERMATOZOIDE) 
        self.hemacia= Elemento(img= HEMACIA)
        self.elodea= Elemento(img= ELODEA)
        self.calciforme= Elemento(img=CALCIFORME)
        self.npc= Elemento(img= NPC,texto = "você precisa descobrir quem é procarionte para a próxima fase", cena=self.laboratorio)#resposta certa é a bactéria
        self.npc.texto.foi = self.entrou_procarionte
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
        self.neuronio.vai=Texto(self.laboratorio,"eus ou bem complicado, pois eu fico na cabeça e passo informação pelo corpo, imagina como eu devo ser feito").vai
    def entrou_bacteria(self, *_):
        self.bacteria.entra(self.laboratorio)
        self.bacteria.vai=Texto(self.laboratorio,"olá eu sou uma pessoa simples, igual arroz pois combino com tudo e posso estar em qualquer lugar, sempre tem espaço para mim").vai
    def entrou_espematozoide(self, *_):
        self.espermatozoide.entra(self.laboratorio)
        self.espermatozoide.vai=Texto(self.laboratorio,"eu sou quem dá a origem dos humanos, então imagina como devo ser dificil e complexo me estudar").vai 
    def entrou_hemacia(self, *_):
        self.hemacia.entra(self.laboratorio)
        self.hemacia.vai=Texto(self.laboratorio, "eu sou o transporte da galera, carrego muita coisa, imagina como sou").vai
    def entra_elodea(self, *_):
        self.elodea.entra(self.laboratorio)
        self.elodea.vai= Texto(self.laboratorio,"eu vivo na agua e sou muito importante para a manutenção do ambiente marinho, posso ser encoderijo , comida ou o2").vai
    def entrou_calciforme(self, *_):
        self.calciforme.entra(self.laboratorio)
        self.calciforme.vai=Texto(self.laboratorio,"eu fico no instestino delgado eu tenho diversas funções, uma dela pe revestir com muco para proteger onde estou").vai
    def entrou_celula(self, *_):
        self.maria.entrou(self.celula)
        self.maria.vai=Texto(self.celula, "ONDE ESTOU?").vai
        self.npc.entrou(self.celula)
        self.npc.vai=Texto(self.celula, " na cidade das células! CITONÓPOLIS").vai
        self.maria.entrou(self.celula)
        self.maria.vai=Texto(self.celula,"como posso sair desse lugar?").vai
        self.npc.entra(self.celula)
        self.npc.vai=Texto(self.celula,"  vc foi trazida para outra dimensão, a dimensão microscópica das células" 
 "Para sair, vc terá  que vencer alguns enigmas e desafios, relacionados ao mundo das células ou ficará presa aqui para sempre.").vai 
    def vai(self):

        self.laboratorio.vai()
Fase1().vai()

#print(Fase1)



