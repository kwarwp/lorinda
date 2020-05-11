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
class oi:
    '''coloquei um def para cada cena, mas ainda não foi. Tenho que fazer essa 'cena fantasma' com todas as cenas??'''
    def __init__(self):
        self.um = um = Sala(n=SALA1, l=SALA2, s=SALA3, o= SALA4)
        self.um.sul.direita = Cena()
   

        self.uma= uma = Sala(o= SALA4, s= SALA5, l= SALA6, n= SALA1)
      
        
        self.dois = dois = Sala (n=SALA1, s= SALA7, l= SALA8, o= SALA4)
    

    
      
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
       
        pasta= Elemento(FOCOSE, x=660, y=250, w=130, h=80, cena=self.um.sul, style={"opacity": 40}, vai=self.um.oeste.vai)
        # def texto_sul_um(self):
        #CLICAR NA PASTA COLORIDA QUE IRÁ ABRIR UMA OUTRA PASTA
        self.pasta = Elemento (img="https://i.imgur.com/bPsIZws.png", tit = "pasta", 
        style=dict(left=350, top=180, width=100, heigth="2px")) 
        self.pasta.entra(um.sul)
        self.pasta.vai=self.texto_oeste_um  # um.oeste.vai
        
    def texto_oeste_um(self, *_):
        #NESSA CENA ELE TERÁ QUE DESEMBARALHAR OS CODONS CLICANDO NELES E UM DELES É O CODON SECRETO
        # O CODIGO EMBARALHADO SECRETO É GAU (AUG-METIONINA)
        #ESSE CODIGO ABRIRÁ O COFRE
        #DICA DO CODON 
        self.um.oeste.vai()
        self.aminoacido= Elemento(img= "https://i.imgur.com/YF2cXp3.png", tit ="Aminoácido",
        style=dict(left=900, top=200, width=90, height="90px")) 
        
        self.aminoacido.entra(self.um.oeste)
        Texto(self.um.oeste, "Como nada nessa vida é fácil, você precisará de uma senha para a proxima etapa. Há 4 códigos genéticos que estão embaralhados, você terá que desembaralhar todos e descobrir o 'nosso' aminoacido secreto. FIQUE ATENTO AS NOSSAS DICAS!! ").vai()
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
        
        
        

# aqui!!!
    def texto_uma_sul(self, *_):
        
        Texto(self.uma.sul, "Será que esse é o nosso código genético secreto?. Clique nele e vamos desembaralhar").vai()
        self.uma.sul.vai()
        self.falauau= Texto(self.uma.sul, "Forma correta é: UAU. Que é a Tirosina, mas infelizmente não é esse nosso código secreto. Com isso, você não conseguiu abrir o cofre. Aperte na setinha e tente novamente.")

        uau = Elemento(FOCOD, x=450, y=260, w=150, h=60, cena=self.uma.sul, style={"opacity": 0}, vai=self.falauau.vai)
       
        self.tirosina= Elemento(img = "https://i.imgur.com/TFGte7s.png", tit= "Tirosina",
        style=dict(left=500, top=400, width=250, heigth="100px"))
        self.tirosina.entra(self.uma.sul)
        
        self.falatiro= Texto(self.uma.sul, "A tirosina (abreviadamente Tyr ou Y)[4] ou 4-hidroxifenilalanina, É um dos 20 aminoácidos que fazem parte das proteínas. É um ÎÂÂ±-aminoácido com uma cadeia lateral formada por CH2 ligado a um grupo fenol, o que a torna uma cadeia lateral cíclica aromática com um grupo OH, que lhe confere um carácter polar neutro.")
        self.tirosina.vai= self.falatiro.vai

        
        self.seta1=Elemento(img ="https://i.imgur.com/STflSS1.gif", tit ="voltar",
        style=dict(left=100, top=400, width=150, heigth="30px"))
        self.seta1.entra(self.uma.sul)
        self.seta1.vai=self.um.oeste.vai
        
        self.setinha1= Elemento (img="https://i.imgur.com/jUJQ5Oc.png", tit = "seta",
        style=dict(left=600, top=300, width=90, heigth="20px"))
        self.setinha1.entra(self.uma.sul)
    
    def texto_uma_leste(self, *_):   
        self.uma.leste.vai()
        
        Texto(self.uma.leste, "Será que esse é o nosso código genético secreto?. Clique nele e vamos desembaralhar").vai()
        self.falaaua= Texto(self.uma.leste, "Forma correta é: AUA. Que é a Isoleucina, mas infelizmente não é esse nosso código secreto. Com isso, você não conseguiu abrir o cofre. Aperte na setinha e tente novamente.")
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
        style=dict(left=600, top=300, width=90, heigth="20px"))
        self.setinha2.entra(self.uma.leste)
    
    
    def texto_dois_sul(self, *_):    
        self.dois.sul.vai()
        Texto(self.dois.sul, "Será que esse é o nosso código genético secreto?. Clique nele e vamos desembaralhar").vai()
        self.falaagu= Texto(self.dois.sul, "Forma correta é: AGU. Que é a Serina, mas infelizmente não é esse nosso código secreto. Com isso, você não conseguiu abrir o cofre. Aperte na setinha e tente novamente.")
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
        style=dict(left=600, top=300, width=90, heigth="20px"))
        self.setinha3.entra(self.dois.sul)
    
        
    def texto_dois_leste(self, *_):  
        self.dois.leste.vai()
        Texto(self.dois.leste, "Será que esse é o nosso código genético secreto?. Clique nele e vamos desembaralhar").vai()
        self.falaaug= Texto(self.dois.leste, "Forma correta é: AUA. Que é a Isoleucina, mas infelizmente não é esse nosso código secreto. Com isso, você não conseguiu abrir o cofre. Aperte na setinha e tente novamente.")
        aug = Elemento(FOCOT, x=450, y=260, w=150, h=60, cena=self.dois.leste, style={"opacity": 0}, vai=self.falaaug.vai)
        
oi()