# lorinda.kristen.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv 

STYLE["width"] = 900
STYLE["heigth"] ='650px'

MATHEUS = ""

CALICE = "" 
AMBULA = ""
PATENA = ""
GALHETA = ""
JARRO_BACIA_ = ""
SANGUINEO = ""
CORPORAL = ""
PALA = ""
PAROQUIA = ""
ALTAR = ""
IGREJA_VELHA = ""
PRESBITERIO = "https://scontent.fcfb1-1.fna.fbcdn.net/v/t1.6435-9/168540222_4412180955478316_593441197893704662_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=8bfeb9&_nc_eui2=AeGCOzl1cuuTXD_uWyjqV2DDmCHEghmzKhKYIcSCGbMqEnSR9qEKiqw1WlDrkYUaZbWF2P3dN7kHV4mgBvbpkhJ6&_nc_ohc=q9C75Mp_uKQAX-IbCvE&_nc_ht=scontent.fcfb1-1.fna&oh=1e4daad38474aea8803fe038836cc4a1&oe=60AA3B07" 


class Tiao:
    def __init__(self):
        self.theus = Elemento(img=MATHEUS)
        self.calice = Elemento(img=CALICE) 
        self.ambula = Elemento(img=AMBULA)
        self.patena = Elemento(img=PATENA)
        self.galheta = Elemento(img=GALHETA)
        self.jarro = Elemento(img=JARRO_BACIA_MANUSTERGIO)
        self.sanguineo = Elemento(img=SANGUINEO)
        self.corporal = Elemento(img=CORPORAL)
        self.pala = Elemento(img=PALA)
        self.paroquia = Cena(img=PAROQUIA)
        self.altar = Cena(img=ALTAR)
        self.igreja = Cena(img=IGREJA_VELHA)
        self.presbiterio = Cena(img=PRESBITERIO)
        self.paroquia.vai()
        self.entrou_theus()
    
    def entrou_theus(self, *_):
        self.theus.entra(self.paroquia)
        Texto(self.paroquia, " Bem vindos ao quiz dos corinhas.")       
        self.theus.vai = Texto(self.paroquia,  
                               "Eu sou o Matheus! Neste jogo, testarei seus conhecimentos sobre o que foi ensinado em nossos encontros!" 
                                foi=self.intro).vai
        
    def entrou_intro(self, *_):
        self.theus.entra(self.igreja)
        Texto(self.igreja, "Estão prontos?")
        self.theus.vai = Texto(self.igreja,
                               "Como foi ensinado em nossos encontros,o grupo de coroinhas é formado por meninos e meninas que, nas igrejas, realizam funções de auxílio ao que preside a celebração, especialmente o padre."
                               foi=self.cena1).vai
                               
                               
    def entrou_cena1(self, *_):
        def resposta(optou):
            respondeu = dict(
            A=Texto(self.igreja_p, ""),
            B=Texto(self.igreja_p,""),
            C=Texto(self.igreja_p, "Correto!", foi=self.entrou_igreja),
         )
        respondeu[optou].vai()
        
    self.igreja_p.vai()
    self.theus.entra(self.igrej_p)
    self.theus.vai = Texto(self.igreja_p, "Qual destas é uma responsabilidade dos Coroinhas?"
                           foi=resposta, A= "Responder mal os pais.", B= "Conversar,rir ou brincar durante a celebração.", C= "Ser cuidadoso com as coisas da Igreja.").vai
        