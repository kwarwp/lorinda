# lorinda.samantha.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, Sala, STYLE
from _spy.vitollino.main import inventario as inv
STYLE["width"]=900
STYLE["height"]='650px'

FLAVINHO ="https://imgur.com/fv9BZ54"
FOTO_PRINCIPAL ="https://imgur.com/NTZqSBD"
DALMACIA ="https://imgur.com/dyLIQib"
JERONIMO_JOVEM ="blob:https://web.whatsapp.com/edad8633-e384-4538-b7f3-ddd4837df1c0"
FUNDO_PERGUNTAS ="https://imgur.com/w7OnO7L"
CURIOSIDADE ="" 
LEAO ="blob:https://web.whatsapp.com/78b2c07d-57e3-4b38-92d1-2dfff506a540"
PAPA_LIBERIO="https://imgur.com/vlIrMHW"
BATIZADO_JERONIMO  =""
ROMA ="https://imgur.com/Zh5yUpP"
ORDDENACAO_SACERDOTAL ="https://imgur.com/qZ3zINX"
SONHO ="blob:https://web.whatsapp.com/2960c698-2f09-4eff-abd9-6ee5d4b7ee47"
JERONIMO_CAVERNA =""
BIBLIA ="https://imgur.com/QPELbOd"
VULGATA =""
BELEM ="https://imgur.com/sf5X4cr"
FOTO_DO_PADROEIRO ="https://imgur.com/Y0CZrXO"
FRASE ="https://imgur.com/LR9Tnyf"
CENA_FINAL="https://imgur.com/kRQyK02"
PAPAD="https://imgur.com/a/bO5ZNKx"
CAVERNA="https://imgur.com/fBFCru5"
FOTO_PAROQUIA="https://imgur.com/zFwNqPr"

 class kkkk():
    def __init__(self):
    self.ft= Cena(img=FOTO_PAROQUIA)
    self.leao= Cena(img=LEAO)
    self.padre= Elemento(img=FALVINHO)
    self.f_t= Cena(img=FOTO_PRINCIPAL)
    self.dalmacia= Cena(img=DALMACIA)
    self.j_j= Elemento(img=JERONIMO_JOVEM)
    self.ft.p= Cena(img=FUNDO_PERGUNTAS)
    self.batizado= Cena(img=BATIZADO_JERONIMO)
    self.roma= Cena(img=ROMA)
    self.ordenacao= Cena(img=ORDDENACAO_SACERDOTAL)
    self.sonho= Cena(img=SONHO)
    self.cr= Cena(img=CURIOSIDADE)
    self.caverna= Cena(img=CAVERNA)
    self.pl= Elemento(img=PAPA_LIBERIO)
    self.j_c= Cena(img=JERONIMO_CAVERNA)
    self.biblia= Cena(img=BIBLIA)
    self.vulgata= Cena(img=VULGATA)
    self.belem= Cena(img=BELEM)
    self.f_p= Cena(img=FOTO_DO_PADROEIRO)
    self.frase= Cena(img=FRASE)
    self.cf= Cena(img=CENA_FINAL)
    self.pd= Elemento(img=PAPAD)
    
         def entrou_padre(self,*_):
            self.padre.entra(self.f_t)
            self.padre.vai=Texto(self.f_t, "olá pessoal, certinho?").vai
            self.padre.vai=Texto(self.f_t, "Eu sou o Padre Flávio e vou te ajudar nessa aventura sobre a história do nosso amado padroeiro").vai
        
        def entrou_1(self,*_):
            def resposta(optou):
                respondeu = dict(
                A=Texto(self.ft.p,
                B=Texto(self.ft.p,
                C=Texto(self.ft.p,
                )
                 respondeu[optou].vai()
                  foi=resposta, A="Egito", B="Dalmácia", C="Brasil").vai
            self.ft.p.vai()
            self.padre.entra(self.dalmacia)
            self.padre.vai=Texto(self.dalmacia, "São Jerônimo nasceu na Dalmácia no ano de 340.").vai
             self.dalmacia.vai()
        
        def entrou_2(self,*_):
            self.padre.entra(self.roma)
            self.padre.vai=Texto(self.roma, "Após a morte de seus pais, Jerônimo foi para Roma estudar e durante sua permanencia teve um sonho muito importante para sua conversão.").vai
        
        
        def entrou_3(self,*_)
            self.padre.entra(self.sonho)
            self.padre.vai=Texto(sonho, "No sonho, Jerônimo apresentava-se como cristão e era repreedindo pelo próprio Cristo por estar faltando com a verdade.").vai

        def entrou_4(self,*_)
            self.padre.entra(self.pl)
            self.padre.vai=.vai=Texto(self.pl, "Aos 25 anos de idade Jerônimo foi batizado pelo Papa Libério no fim de sua permanencia em Roma.").vai
            self.padre.vai=Texto(self.fp, "Aos 25 anos de idade Jerônimo foi batizado pelo Papa Libério no fim de sua permanencia em Roma.").vai
        
        def entrou_5(self,*_)
            self.padre.entra(self.ordenacao)
            self.padre.vai=Texto(self.ordenacao= "Jerônimo foi ordenado sacerdote no ano de 379, retirando-se para dedicar-se ao estudo.").vai
    
        def entrou_curi(self,*_)
            self.padre.entra(self.curiosidade)
            self.padre.vai=Texto(self.curiosidade,"Jerônimo foi ordenado sacerdote no ano de 379, retirando-se para dedicar-se ao estudo.").vai

        def entrou_6(self,*_)
            self.padre.entra(self.caverna)
            self.padre.vai=Texto(self.caverna,"Por ter aprendido as linguas originais para melhor compreender as escrituras, Nosso padroeiro pôde a pedido do Papa Damaso traduzir as escrituras para o Latim.").vai 
    
        def entro_7(self,*_)
            self.padre.entra(self.biblia)
            self.padre.vai=Texto(self.biblia, "A tradução da sagrada escritura recebeu o nome Vulgata.").vai

        def entrou_8(self,*_)
            self.padre.entra(self.vulgata)
            self.padre.vai=Texto(self.vulgata, "A tradução da sagrada escritura recebeu o nome Vulgata.").vai
        
    
        def entrou_9(self,*_)
            self.padre.entra(self.belem)
            self.padre.vai=Texto(self.belem, "Após traduzir a sagrada escritura , Jerônimo mudou-se para Belém a cidade onde nasceu nosso Salvador.").vai
    
        def entrou_10(self,*_)
            self.padre.entra(self.f_p)
            self.padre.vai=Texto(self.f_p, "Jerônimo morreu no dia 30 de setembro de 420 em Belém, por isso o dia da Biblía e de São Jerônimo são comemorados no dia 30 de setembro.").vai
    
    
        def entrou_11(self,*_)
            self.padre.entra(self.leao)
            self.padre.vai=Texto(self.leao "É um leão!!").vai
    
       def entrou_12(self,*_)
            self.padre.entra(self.frase)
            self.padre.vai=Texto(self.frase, "A frase mais conhecida de nosso padroeiro é:  Ignorar as Escrituras Sagradas é ignorar a Cristo").vai
    
        def entrou_final(self,*_)
            self.padre.entra(self.cf)
            self.padre.vai=Texto(self.cf, "Espero que tenham gostado de aprender um pouco mais da história do nosso amdado padroeiro São Jerônimo!").vai
            self.padre.vai=Texto(self.cf, " Até a próxima !!!").vai
f_T.vai()
kkkk()