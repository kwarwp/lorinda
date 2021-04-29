# lorinda.kristen.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import INVENTARIO as inv 

STYLE["width"] = 900
STYLE["heigth"] ='650px'

MATHEUS = "https://www.imagensempng.com.br/cartoon-quadrinhos-png"
CALICE = "" 
AMBULA = ""
PATENA = ""
GALHETA = ""
JARRO_BACIA_ = ""
SANGUINEO = ""
CORPORAL = ""
PALA = ""
PAROQUIA = "https://www.imagensempng.com.br/wp-content/uploads/apollo13_images/Efeito-Cartoon-Png-72qx5cm50i4sm57t6ga67lrxhbcdztvkhe.png"
ALTAR = ""
IGREJA_VELHA = ""
PRESBITERIO = "" 


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
        Texto(self.paroquia, " Bem vindos ao quiz dos corinhas.").vai()       
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
            A=Texto(self.igreja_p, "Errado."),
            B=Texto(self.igreja_p,"Errado."),
            C=Texto(self.igreja_p, "Correto!", foi=self.entrou_cena2),
         )
        respondeu[optou].vai()
        
    self.igreja_p.vai()
    self.theus.entra(self.igrej_p)
    self.theus.vai = Texto(self.igreja_p, "Qual destas é uma responsabilidade dos Coroinhas?"
                           foi=resposta, A= "Responder mal os pais.", B= "Conversar,rir ou brincar durante a celebração.", C= "Ser cuidadoso com as coisas da Igreja.").vai
        
        
    def entrou_cena2(self, *_):
        def reposta(optpou):
            respondeu = dict(
            A=Texto(self.ireja_p, "Errado."),
            B=Texto(self.igreja_p, "Correto!", foi=self.entrou_intro2),
            C=Texto(self.igreja_p, "Errado."),
         )
        respondeu[optou].vai()
        
    self.igreja_p.vai()
    self.theus.entra(self.igreja_p)
    self.theus.vai = Texto(self.igreja_p, "Chegando à igreja, para onde o coroinha deve se dirigir?"
                           foi=resposta, A= "Para a sacristia", B= "Para a Capela do Santíssimo", C= "Para o Presbitério").vai
                           
                           
                           
                           
                           
    def entrou_intro2(self, *_):
    self.theus.entra(self.igreja)
    Texto(self.igreja, " Nesta fase, recordamos a Liturgia ,  Celebrações Litúrgicas e alguns símbolos utilizados na liturgia.")
    self.theus.vai = Texto(self.igreja,
                            "Vamos nessa?"
                             foi=self.cena3).vai
                             
                             
    def entrou_cena3(self, *_):
        def resposta(optou):
            respondeu = dict(
            A=Texto(self.igreja_p, "Errado."),
            B=Texto(self.igreja_p, "Errado."),
            C=Texto(self.igreja_p, "Você acertou!",foi=self.entrou_cena4),
         )
        respondeu[optou].vai() 

    self.igreja_p.vai()
    self.theus.entra(self.igreja_p)
    self.theus.vai = Texto(self.igreja_p, "O que é Liturgia?"
                           foi=resposta, A= "O livro que recebemos mensalmente.", B= "As orações que fazemos em casa.", C="A ação do povo, o serviço do povo.").vai
            
            
        
    def entrou_cena4(self,*_):
        def resposta(optou):
            respondeu = dict(
            A=Texto(self.igreja_p, "Acertou!", foi=self.entrou_cena5),
            B=Texto(self.igreja_p, "Errado."),
            C=Texto(self.igreja_p, "Errado."),
         )
        respondeu[optou].vai()
        
    self.igreja_p.vai()
    self.theus.entra(self.igreja_p)
    self.theus.vai = Texto(self.igreja, "O que são celebrações Litúrgicas?"    
                           foi=resposta, A="Encontros de Deus com seu povo reunido.", B="Festa de aniversário.", C= "Celebração dos povos.").vai
            
        
    def entrou_cena5(self, *_):
        def resposta(optou):
            respondeu = dict(
            A=Texto(self.igreja_p,"Errado."),
            B=Texto(self.igreja_p,"Errado."),
            C=Texto(self.igreja_p,"Acertou!", foi=self.entrou_cena6),
        )
        respondeu[optou].vai()
        
    self.igreja_p.vai()
    self.theus.entra(self.igreja_p)
    self.theus.va = Texto(self.igreja, "O que significa INRI ?"
                          foi=resposta, A="Santíssima Trindade.", B="Nossa Senhora.",  C="Jesus Rei dos Judeus.").vai
                          
                        
    def entrou_cena_6(self, *_):
        def resposta(optou):
             respondeu = dict(
             A=Texto(self.igreja_p,"Errado."),
             B=Texto(self.igreja_p,"Acertou!", foi=self.entrou_intro3),
             C=Texto(self.igreja_p,"Errado."),
        )
        respondeu[optou].vai()
        
    self.igreja_p.vai()
    self.theus.entra(igreja_p)
    self.theus.vai = Texto(self.igreja, "O que siguinifica A e Ω ?"
                           foi=resposta, A="Cristo.", B="Alfa e Ômega.", C="Jesus salvador dos homens.").vai
                           
                           
    def entrou_intro3(self, *_):
    self.theus.entra(self.presbiterio)
    Texto(self.presbiterio, "Nesta próxima fase, relembramos algumas posições em que os coroinhas ficam durante a celebração da Santa Missa.")
    self.theus.vai = Texto(self.presbiterio,
                            "Estão preparados?"
                             foi=self.cena7).vai 
                             
                             
    def entro_cena7(self, *_):
        def resposta(optou):
            respondeu = dict(
            A=Texto(self.presbiterio_p,"Errado."),
            B=Texto(self.presbiterio_p,"Errado."),
            C=Texto(self.presbiterio_p,"Correto!", foi=self.entrou_cena8),
        )
        respondeu[optou].vai()
        
    self.prebiterio_p.vai()
    self.theus.entra(presbiterio_p)
    self.theus.vai = Texto(self.presbiterio, "O que siguinifica inclinar o corpo ?"
                           foi=resposta, A="Escuta da palavra.", B="Oração profunda.", C="Reverência e honra.").vai
                           
    def entrou_cena8
        def resposta(optou):
            respondeu = dict(
            A=Texto(self.presbiterio_p,"Errado."),
            B=Texto(self.presbiterio_p,"Correto!", foi=self.entrou_cena9),
            C=Texto(self.presbiterio_p,"Errado."),
        )
        respondeu[optou].vai()
        
    self.presbiterio_p.vai()
    self.theus.entra(prebiterio_p)
    self.theus.vai = Texto(self.presbiterio, "O que siguinifica estar sentado ?"
                           foi=resposta, A="Humildade.", B="Escuta da palavra.", C="Reverência e honra.").vai
                           
    def entrou_cena9
        def resposta(optou):
            respondeu = dict(
            A=Texto(self.presbiterio_p,"Correto!.", foi=self.entrou_cena9),
            B=Texto(self.presbiterio_p,"Errado."),
            C=Texto(self.presbiterio_p,"Errado."),
        )
        respondeu[optou].vai()
        
    self.presbiterio_p.vai()
    self.theus.entra(presbiterio_p)
    self.theus.vai = Texto(self.prebiterio, "O que siguinifica bater no peito ?"
                           foi=resposta, A="Arrependimento dos pecados.", B="Peregrino.", C="Meditação.").vai
            
        self.final.vai()  
Tiao()
    