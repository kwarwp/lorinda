# lorinda.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"
#quadro negro
BOTAO = "https://pngimage.net/wp-content/uploads/2018/05/bot%C3%A3o-power-png-7.png"
#
FOCO = "https://i.imgur.com/6e096Va.png"
FOCOD = "https://i.imgur.com/6e096Va.png"
FOCOT = "https://i.imgur.com/6e096Va.png"
FOCOQ = "https://i.imgur.com/6e096Va.png"
FOCOC = "https://i.imgur.com/6e096Va.png"
FOCOS = "https://i.imgur.com/6e096Va.png"
FOCOSE = "https://i.imgur.com/6e096Va.png"
FOCOO = "https://i.imgur.com/6e096Va.png"
FOCON = "https://i.imgur.com/6e096Va.png"
#saladeinformatica 1 CENA
SALA1 ="https://i.imgur.com/bnapnxL.png"
  #teladocomputador
SALA2 = "https://i.imgur.com/78zBQ2V.png"
#tela das pastas
SALA3 = "https://i.imgur.com/N6JUV1K.png"
#codon embaralhado
SALA4 = "https://i.imgur.com/fxMYKmc.png"
# codon AUU (uau) TIROSINA
SALA5 = "https://i.imgur.com/mLC28Jx.png"
# codon GUA(agu) SERINA
SALA7 = "https://i.imgur.com/AdIuakb.png"
# codon AAU(aua) ISOLEUCINA
SALA6 = " https://i.imgur.com/Ey3Gccw.png"
#codon GAU (aug) metionina
SALA8 = "https://i.imgur.com/9ZxVZDJ.png"
#cofre 
SALA9 = "https://i.imgur.com/XMKlMUb.png"
SALA10 = "https://i.imgur.com/O43oDtt.png"
SALA11= "https://media.giphy.com/media/mq5y2jHRCAqMo/giphy.gif"
SALA12="https://media.giphy.com/media/mq5y2jHRCAqMo/giphy.gif "
SALA13 = "https://images.madeiramadeira.com.br/product/images/93158678-adesivo-paisagem-natureza-lago-papel-parede-montanhas-gg423prdjlgbeahvwvdsv-179-1-800x729.jpg"
SALA14= "https://media.giphy.com/media/mq5y2jHRCAqMo/giphy.gif"

class oi:
    '''coloquei um def para cada cena, mas ainda não foi. Tenho que fazer essa 'cena fantasma' com todas as cenas??'''
    def __init__(self):
        self.um = um = Sala(n=SALA1, l=SALA2, s=SALA3, o= SALA4)
        self.um.sul.direita = Cena()


        self.uma= uma = Sala(o= SALA4, s= SALA5, l= SALA6, n= SALA1)

        
        self.dois = dois = Sala (n=SALA1, s= SALA7, l= SALA8, o= SALA4)
    
        self.tres = tres = Sala(o=SALA4, s= SALA9, l=SALA10, n=SALA1)
    
        self.quatro = quatro = Sala( n=SALA1, l=SALA11, s=SALA12, o= SALA4)
        
        self.cinco= cinco = Sala( o= SALA4, l=SALA13, s=SALA14, n=SALA1)
        self.um.norte.vai()
        

        #def texto_norte_um(self):
        Texto(self.um.norte, "Seja bem vindo, cientista! Hoje iremos aprender um pouquinho sobre biologia com o auxilio da nossa maravilhosa tecnologia. Vamos nessa?").vai()
        #
          #O JOGADOR TERÁ QUE APERTAR O BOTAO PARA LIGAR O COMPUTADOR
        self.botao=Elemento(img=BOTAO,tit="ligar",
        style=dict(left=350,top=250,width=30,height="30px")) 
        self.botao.entra(um.norte)
        self.botao.vai=self.um.leste.vai
    
        #def texto_leste_um(self):
        self.voltar1=Elemento(img="https://image.flaticon.com/icons/png/512/74/74345.png", tit="desligar",
        style=dict(left=200, top=500, width=60, height="50px")) 
        self.voltar1.entra(um.leste)
        self.voltar1.vai=self.um.norte.vai
         
        #APÓS ELE LIGAR O COMPUTADOR TERÁ QUE COLOCAR A SENHA QUE É "SINTESE DE PROTEINAS"
        sin= Elemento(FOCO, x=460, y=250, w=150, h=80, cena=self.um.leste, style={"opacity": 0}, vai=self.um.sul.vai)
       
        pasta= Elemento(FOCOSE, x=750, y=230, w=130, h=80, cena=self.um.sul, style={"opacity": 0}, vai=self.texto_oeste_um)
        self.voltar2=Elemento(img="https://image.flaticon.com/icons/png/512/74/74345.png", tit="voltar",
        style=dict(left=200, top=500, width=60, height="50px")) 
        self.voltar2.entra(um.sul)
        self.voltar2.vai=self.um.leste.vai
         
        # def texto_sul_um(self):
        #CLICAR NA PASTA COLORIDA QUE IRÁ ABRIR UMA OUTRA PASTA
       
        
    def texto_oeste_um(self, *_):
        #NESSA CENA ELE TERÁ QUE DESEMBARALHAR OS CODONS CLICANDO NELES E UM DELES É O CODON SECRETO
        # O CODIGO EMBARALHADO SECRETO É GAU (AUG-METIONINA)
        #ESSE CODIGO ABRIRÁ O COFRE
        #DICA DO CODON 
        self.um.oeste.vai()
        self.aminoacido= Elemento(img= "https://i.imgur.com/YF2cXp3.png", tit ="Aminoácido",
        style=dict(left=950, top=180, width=90, height="90px")) 
        
        self.aminoacido.entra(self.um.oeste)
        Texto(self.um.oeste, "Como nada nessa vida é fácil, você precisará de uma senha para abrir nosso cofre e passar para proxima etapa. Há 4 códigos genéticos que estão embaralhados, você terá que desembaralhar todos e descobrir o 'nosso' aminoacido secreto(clique na nossa imagem que representa um aminoacido). FIQUE ATENTO AS NOSSAS DICAS!! ").vai()
        self.dica=Elemento(img= "https://i.imgur.com/J5A0Jdo.png", tit = "dica!!",
        style=dict(left=530, top=400, width=80, heigth="80px"))
        self.dica.entra(self.um.oeste)
        self.faladica= Texto(self.um.oeste, "Met(metionina)")
        self.dica.vai=self.faladica.vai
        self.falamido= Texto(self.um.oeste, "Uma grande parte dos nossos células, músculos e tecido é constituído por aminoácidos, o que significa que realizar muitas funções importantes do corpo, tais como as células dando a sua estrutura. Eles também desempenham um papel chave no transporte e armazenamento de nutrientes.")
        self.aminoacido.vai=self.falamido.vai


        auu = Elemento(FOCO, x=190, y=320, w=150, h=80, cena=self.um.oeste, style={"opacity": 0}, vai=self.texto_uma_sul)
        aau = Elemento(FOCO, x=400, y=320, w=150, h=80, cena=self.um.oeste, style={"opacity": 0}, vai=self.texto_uma_leste)
        gua = Elemento(FOCO, x=590, y=320, w=150, h=80, cena=self.um.oeste, style={"opacity": 0}, vai=self.texto_dois_sul)
        gau = Elemento(FOCO, x=800, y=320, w=150, h=80, cena=self.um.oeste, style={"opacity": 0}, vai=self.texto_dois_leste)
        
        
        '''TODOS OS CENARIOS DE TODOS OS CÓDONS'''

# aqui!!!
    def texto_uma_sul(self, *_):
        
        Texto(self.uma.sul, "Será que esse é o nosso código genético secreto?. Clique no código e vamos desembaralhar").vai()
        self.uma.sul.vai()
        self.falauau= Texto(self.uma.sul, "Forma correta é: UAU. Que é a Tirosina, mas infelizmente não é esse nosso código secreto. Com isso, você não conseguiu abrir o cofre. Aperte na imagem que representa a Tirosina e logo após clique para voltar e tente novamente.")

        uau = Elemento(FOCOD, x=450, y=260, w=150, h=60, cena=self.uma.sul, style={"opacity": 0}, vai=self.falauau.vai)
       
        self.tirosina= Elemento(img = "https://i.imgur.com/TFGte7s.png", tit= "Tirosina",
        style=dict(left=500, top=400, width=250, heigth="100px"))
        self.tirosina.entra(self.uma.sul)
        
        self.falatiro= Texto(self.uma.sul, "A tirosina (abreviadamente Tyr ou Y)[4] ou 4-hidroxifenilalanina, É um dos 20 aminoácidos que fazem parte das proteínas. É um ÎÂÂÂÂÂÂÂ±-aminoácido com uma cadeia lateral formada por CH2 ligado a um grupo fenol, o que a torna uma cadeia lateral cíclica aromática com um grupo OH, que lhe confere um carácter polar neutro.")
        self.tirosina.vai= self.falatiro.vai

        
        self.seta1=Elemento(img ="https://i.imgur.com/STflSS1.gif", tit ="voltar",
        style=dict(left=100, top=400, width=150, heigth="30px"))
        self.seta1.entra(self.uma.sul)
        self.seta1.vai=self.um.oeste.vai
        
        self.setinha1= Elemento (img="https://i.imgur.com/jUJQ5Oc.png", tit = "seta",
        style=dict(left=600, top=300, width=50, heigth="20px"))
        self.setinha1.entra(self.uma.sul)
    
    def texto_uma_leste(self, *_):   
        self.uma.leste.vai()
        
        Texto(self.uma.leste, "Será que esse é o nosso código genético secreto?. Clique no código e vamos desembaralhar").vai()
        self.falaaua= Texto(self.uma.leste, "Forma correta é: AUA. Que é a Isoleucina, mas infelizmente não é esse nosso código secreto. Com isso, você não conseguiu abrir o cofre. Aperte na imagem que representa a Isoleucina e logo após clique para voltar e tente novamente.")
        aua = Elemento(FOCOT, x=450, y=260, w=150, h=60, cena=self.uma.leste, style={"opacity": 0}, vai=self.falaaua.vai)
        
        self.isoleucina=Elemento(img = "https://i.imgur.com/tL2cc9H.png", tit = "Isoleucina",
        style=dict(left=500, top=400, width=150, heigth="80px"))
        self.isoleucina.entra(self.uma.leste)
        
        self.seta2=Elemento(img ="https://i.imgur.com/STflSS1.gif", tit ="voltar",
        style=dict(left=100, top=400, width=150, heigth="30px"))
        self.seta2.entra(self.uma.leste)
        self.seta2.vai=self.um.oeste.vai
    
        self.falaiso= Texto(self.uma.leste, "A Isoleucina é utilizada pelo organismo especialmente para construir os tecidos musculares. A isoleucina, leucina e valina são os aminoácidos de cadeia ramificada e são melhor absorvidos e utilizados pelo organismo na presença de vitaminas do complexo B, como o feijão ou lecitina de soja.")
        self.isoleucina.vai=self.falaiso.vai
        
        self.setinha2= Elemento (img="https://i.imgur.com/jUJQ5Oc.png", tit = "seta",
        style=dict(left=600, top=300, width=50, heigth="20px"))
        self.setinha2.entra(self.uma.leste)
    
    
    def texto_dois_sul(self, *_):    
        self.dois.sul.vai()
        Texto(self.dois.sul, "Será que esse é o nosso código genético secreto?. Clique no código e vamos desembaralhar").vai()
        self.falaagu= Texto(self.dois.sul, "Forma correta é: AGU. Que é a Serina, mas infelizmente não é esse nosso código secreto. Com isso, você não conseguiu abrir o cofre. Aperte na imagem que representa a Serina e logo após clique para voltar e tente novamente.")
        agu = Elemento(FOCOT, x=450, y=260, w=150, h=60, cena=self.dois.sul, style={"opacity": 0}, vai=self.falaagu.vai)
        self.serina=Elemento(img= "https://i.imgur.com/IDBTwzj.png", tit= "Serina",
        style=dict(left=530, top=400, width=150, heigth="80px"))
        self.serina.entra(self.dois.sul)
        
        self.seta3=Elemento(img ="https://i.imgur.com/STflSS1.gif", tit ="voltar",
        style=dict(left=100, top=400, width=150, heigth="30px"))
        self.seta3.entra(self.dois.sul)
        self.seta3.vai=self.um.oeste.vai
        
        self.falaseri=Texto(self.dois.sul, "A serina é importante no metabolismo, dado que participa na biossíntese de purinas e pirimidinas. É o percursor de vários aminoácidos, incluindo glicina e cisteína, e triptofano em bactérias.")
        self.serina.vai=self.falaseri.vai
        
        self.setinha3= Elemento (img="https://i.imgur.com/jUJQ5Oc.png", tit = "seta",
        style=dict(left=600, top=300, width=50, heigth="20px"))
        self.setinha3.entra(self.dois.sul)
    
        '''CÓDON CERTO'''
    def texto_dois_leste(self, *_):  
        self.dois.leste.vai()
        Texto(self.dois.leste, "Será que esse é o nosso códigoo genético secreto?. Clique no código e vamos desembaralhar").vai()
        
        self.falaaug= Texto(self.dois.leste, "A FORMA CORRETA É: AUG. Chamado Metionina, muito bom!! Você descobriu a senha do nosso cofre. Parabéns! Clique na Metionina para saber mais sobre ela, logo após clique para próxima etapa")
        aug = Elemento(FOCOT, x=450, y=260, w=150, h=60, cena=self.dois.leste, style={"opacity": 0}, vai=self.falaaug.vai)
        
        self.metionina=Elemento(img= "https://i.imgur.com/H3QrDcM.png", tit= "Metionina",
        style=dict(left=530, top=400, width=150, heigth="80px"))
        self.metionina.entra(self.dois.leste)
        
        self.seta4=Elemento(img ="https://i.imgur.com/STflSS1.gif", tit ="voltar",
        style=dict(left=100, top=400, width=150, heigth="30px"))
        self.seta4.entra(self.dois.leste)
        self.seta4.vai=self.um.oeste.vai
        
        self.falametio=Texto(self.dois.leste, "A metionina (Met) é um dos aminoácidos codificados pelo código genético, sendo portanto um dos componentes das proteínas dos seres vivos, com exceção das bactérias procariontes (as quais possuem N-Formil Metionina.")
        self.metionina.vai=self.falametio.vai
        
        
        
        self.setinha5= Elemento (img="https://i.imgur.com/jUJQ5Oc.png", tit = "seta",
        style=dict(left=600, top=300, width=50, heigth="20px"))
        self.setinha5.entra(self.dois.leste)
        
        self.foi= Elemento(img="https://i.imgur.com/mI8mB36.png", tit = "próx. etapa",
        style=dict(left=1090, top=200, width=40, heigth="20px"))
        self.foi.entra(self.dois.leste)
        self.foi.vai=self.texto_tres_sul
        
        #QUANDO O JOGADOR ACERTA O CÓDON CERTO, ELE IRÁ ABRIR UM COFRE
        ''' CENA DO COFRE'''
        
    def texto_tres_sul(self, *_): 
        self.tres.sul.vai()
        Texto(self.tres.sul, "Você conseguiu abrir nosso cofre!! Agora vamos lá descobrir o que tem dentro dele.").vai()
        cof=Elemento (FOCOO, x=380, y=200, w=70, h=260, cena=self.tres.sul, style={"opacity": 0}, vai=self.texto_tres_leste)
        
        '''CENA DAS PORTAS'''
        #ELE TERÁ QUE LEVAR O CÓDIGO DE INICIAÇÃO PARA A PORTA CERTA -> ENTÃO A PORTA IRÁ ABRIR
        #EXISTEM 4 PORTAS, A NOORTE É A CERTA
        #CADA PORTA TEM UMA SEQUÊNCIA DE CÓDONS

    def texto_tres_leste(self, *_):
        self.tres.leste.vai()
        Texto (self.tres.leste, "Olá, parábens! Você conseguiu desvendar o código de iniciação que é a: Metíonina. Nessa fase cada porta possui uma sequência de codons, mas apenas uma irá se abrir. Para poder abrir a porta, você precisará levar o código de iniciação para a sequência certa").vai()
        foco_sul= Elemento (img = " https://i.imgur.com/6e096Va.png", x=100, y=100, w=150, h=200, style={"opacity": 0}, cena = self.tres.leste, vai= self.texto_quatro_leste)
        foco_oeste= Elemento (img= "https://i.imgur.com/6e096Va.png", x=350, y=100, w=150, h=200, style={"opacity": 0}, cena = self.tres.leste, vai = self.texto_quatro_sul)
        foco_norte= Elemento (img= "https://i.imgur.com/6e096Va.png", style={"opacity": 0}, cena = self.tres.leste, vai = self.texto_cinco_leste, tit = "DNA: ACT GCC ATC AGG")
        codon_iniciacao = Elemento (img = "https://i.imgur.com/foWxout.png", x=250, y=350, w=650, h=200, cena = self.tres.leste)
        
        #foco_leste= Elemento (img= "https://i.imgur.com/6e096Va.png", x=940, y=100, w=150, h=200, style={"opacity": 0}, cena = self.tres.leste, vai = self.texto_cinco_sul)
        


        '''quando a porta se abrir:'''
      #porta sul
    def texto_quatro_leste (self, *_):
        self.quatro.leste.vai()
        Texto(self.quatro.leste, "Não foi dessa vez, sequência errada!!!! Aperte no 'X' para voltar").vai()
        erroQL = Elemento (img ="https://i.imgur.com/eoMGnKA.png", cena= self.quatro.leste, vai= self.texto_tres_leste)
        #porta oeste
    def texto_quatro_sul(self, *_):
        Texto(self.quatro.sul, "Não foi dessa vez, sequência errada!!!! Aperte no 'X' para voltar").vai()
        erroQS = Elemento (img ="https://i.imgur.com/eoMGnKA.png", cena= self.quatro.sul, vai= self.texto_tres_leste)
        self.quatro.sul.vai()
        #porta norte
    def texto_cinco_leste( self, *_):
        Texto(self.cinco.leste, "Não foi dessa vez, sequência errada!!!! Aperte no 'X' para voltar").vai()
        erroCL = Elemento (img ="https://i.imgur.com/eoMGnKA.png", cena= self.cinco.leste, vai= self.texto_tres_leste)
        self.quatro.leste.vai()
        #porta leste
    def texto_cinco_sul(self, *_):
        self.cinco.sul.vai()
        Texto(self.cinco.sul, "Não foi dessa vez, sequência errada!!!! Aperte no 'X' para voltar").vai()
        erroCS = Elemento (img ="https://i.imgur.com/eoMGnKA.png", cena= self.cinco.sul, vai= self.texto_tres_leste)
    

oi()