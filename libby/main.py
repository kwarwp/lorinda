# lorinda.libby.main.
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv 
from anastasia.main import Associa, SF
from courtney.main import MOCHILA
SF.update({"font-size":"20px", "transition": "left 1s, top 1s"})
STYLE.update(width=1000, height="600px")
#bacteriaCerto
CELULA_1 = "https://s1.static.brasilescola.uol.com.br/be/conteudo/images/o-nucleo-envolto-por-uma-membrana-apresenta-em-seu-interior-os-cromossomos-5a86b19fdc671.jpg"
#protozoarioCERTO
CELULA_2 = "https://imgur.com/zpc9NP0.jpg"
#vegetalCERTO
CELULA_3 = "https://imgur.com/6sZ3B2K.jpg"
#espermatozoide
CELULA_4 = "https://imgur.com/RD0Fe3X.jpg" 
#espermatozoide
CELULA_5 = "https://imgur.com/2kY3sBX.jpg"
#nervosa neuronio
MARIA = "https://i.imgur.com/1sI2ePw.png"

CELULA_6 = "https://imgur.com/YK4fgSr.jpg"
MOEDAS = "https://i.imgur.com/VfyiFmY.png"
CICLONE = "https://static.todamateria.com.br/upload/55/65/556506fa96eca-ciclone.jpg"
CELULA = "https://i.imgur.com/SVGoGCK.jpg"
NPC = "https://imgur.com/VcPXMYC.png"
MEMBRANA = "https://i.imgur.com/5NdRkMo.jpg"
A = ""
B = ""
C = ""
D = ""
LIVRO = "https://i.imgur.com/tOQ2Lq0.png"
class Fase1(): 
    def __init__(self, maria=None):
        self.laboratorio= Cena(img =  LABORATORIO)
        self.celula = Cena(CELULA)
        self.livro = Elemento(LIVRO, x=500, y=40, w=500, h=500, cena=self.celula)

class Fase2():
    def __init__(self):
        #self.npc= Elemento(img= NPC)
        def some(ev):
            self.celula_1.x = -10000
        self.ciclone= Elemento(img= CICLONE)
        self.membrana= Cena(img= CELULA)
        #self.livro = Elemento(LIVRO, x=300, y=10, w=700, h=500, cena=self.membrana)
        self.celula_1= Elemento(img= CELULA_1,x=750,y=120, w=150, h= 150,  tit="Tenho como característica principal, é que meu material genético não está envolto por uma membrana nuclear. Ele fica espalhado pelo citoplasma, em regiões conhecidas como nucleóides, onde fica o DNA circular do tipo cromossômico. ", vai=self.acertou)
        #self.celula_1.elt.onclick = some  #Sair dessa sala e ir para a sala kelle, depois que acertar
        self.celula_2= Elemento(img= CELULA_2,x=550,y=300, w=150, h=150, tit="Sou a célula vegetal, sou o componente básico de todos os seres vivos que fazem parte do Reino Vegetal. Possuo núcleo organizado e vários tipos de organelas. Parede celular, plastos e vacúolos são estruturas que pertencem apenas a mim, pois são específicas para o estilo de vida das plantas.", vai=self.errou)
        self.celula_3= Elemento(img= CELULA_3,x=550,y=120, w=150, h=150, tit="Sou a hemácia. Faço parte do grupo de células que compõem o sangue. Sou especialista em transportar O2 e CO2. Quando madura, não possuo núcleo. Tenho forma bicôncava, o que facilita as trocas gasosas. Essa forma se deve à presença de proteínas estruturais no citoesqueleto.", vai=self.errou)
        self.celula_4= Elemento(img= CELULA_4,x=150,y=120, w=150, h=150, tit="Pertenço ao sistema reprodutor masculino, tenho uma função muito importante, transfiro o DNA masculino ao ovócito. Possuo numerosas mitocôndrias que me fornecem ATP (adenosina trifosfato) para a locomoção. Sou a única célula dos mamíferos que possui flagelo. Sou o espermatozoide.", vai=self.errou)
        self.celula_5= Elemento(img= CELULA_5,x=350,y=120,w=150, h=150, tit="Sou a célula caliciforme do intestino, sou um exemplo de uma célula epitelial especializada na síntese e exportação de proteínas para o meio extracelular. Me localizo, principalmente, no intestino delgado. Sou responsável pela produção e secreção do muco que reveste e protege o epitélio intestinal. Sou uma célula alongada, e, como esperado, muito rica em organelas relacionadas à rota secretora ou de exportação. Assim, verifica-se em mim a presença de um retículo endoplasmático granular abundante, um complexo de Golgi bem desenvolvido que dá origem a inúmeras vesículas secretoras. Estas vesículas dirigem-se à membrana plasmática apical, com a qual se fundem (por exocitose), descarregando seu conteúdo (o muco) na luz do intestino.", vai=self.errou)
        self.celula_6= Elemento(img= CELULA_6,x=350,y=300,w=150, h=150, tit="Sou uma célula altamente especializada em processar informações, capaz de transmitir o impulso nervoso para outras células. Possuo estruturas celulares como núcleo e mitocôndrias, como outras células, mas tenho uma forma diferenciada, que está relacionada com a minha função. Me chamo neurônio.", vai=self.errou)
        self.membrana.vai()
        #self.jogo = Associa(self.membrana, caixa=300, borda=20, acertou=self.acertou, acertos=6)
        self.celula_1.entra(self.membrana)
        self.celula_2.entra(self.membrana)
        self.celula_3.entra(self.membrana)
        self.celula_4.entra(self.membrana)
        self.celula_5.entra(self.membrana)
        self.celula_6.entra(self.membrana)
        self.npc=Elemento(img=NPC, x=900,y=350)
        
        """self.jogo.nome(nome="1-Meu núcleo é espalhado", tit=0, x=450, y=50)
        self.jogo.nome(nome="2-Citoplasma, membrana, núcleo", tit=1, x=750, y=50)
        self.jogo.nome(nome="3-Citoplasma, membrana, núcleo", tit=2, x=450, y=150)
        self.jogo.nome(nome="4-Citoplasma, membrana, núcleo", tit=3, x=850, y=150)
        self.jogo.nome(nome="5-Citoplasma, membrana, núcleo", tit=4, x=450, y=250)
        self.jogo.nome(nome="6-Citoplasma, membrana, núcleo", tit=5, x=750, y=250)
        self.jogo.nome(nome= "Para sair desse mundo você precisa achar o protozoário",tit=6,x=1000,y=350)# como fazer para aparecer tudo ?"""
    
    def acertou(self,*_):
        from kellee.main import Fase3
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()
        Texto(self.membrana, "Você acertou! Parabéns! Você ganhou cinco ATP, veja sua mochila.",
        foi=self.atravessa_membrana).vai()
    
    def atravessa_membrana(self,*_):
        def maria_anda(*_):
            self.maria.y = 450
            self.maria.o = 0.2
        def maria_chega(*_):
            self.maria.y = 450
            self.maria.o = 1
            self.maria.vai = self.atravessou_membrana
        self.membrana = Cena(MEMBRANA).vai()
        fala = Texto(self.membrana, "Tenho que atravessar a membrana plasmática para entrar na célula.", foi=maria_anda)
        self.maria = Elemento(img= MARIA, x=200, y=50, w=150, h=120, cena=self.membrana, vai=fala.vai,
        style= {"transition": "top 5s, opacity 5s"})
        self.maria.elt.ontransitionend = maria_chega
        
    
    def atravessou_membrana(self,*_):
        from kellee.main import Fase3
        Texto(self.membrana, "Você atravessou a membrana plasmática. Uma estrutura fantástica que possui composição lipoproteica, ou seja, é formada por proteínas e lipídios. Ela é composta por duas camadas de lipídios e as proteínas estão imersas nessas camadas. Esses lipídios mudam constantemente de posição e as proteínas distribuídas pela membrana lembram um mosaico, por isso, esse modelo de membrana recebeu o nome de “modelo do mosaico fluido”.",
        foi=Fase3).vai()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()
        MOCHILA.ganha_atp()

    def errou(self, *_):
        Texto(self.membrana, "Poxa! Não sou eu, pois sou uma célula eucarionte. ").vai()
    
    
        #self.npc.entra(self.celula,Tit = "Observe atentamente essas imagens e coloque as letras correspondentes."
        #"Cada imagem terá apenas três letras, arraste para a área correspondente da célula")    #não temos ainda a imagem da célula
        #self.npc.entra(self.membrana,Tit = "Você precisa de moedas de ATP para sair dessa dimenção, para isso, precisamos excluir a célula procarionte")
        
"""class celulas():
    def __init__(self):
        self.a= Elemento(img= A)
        self.b= Elemento(img= B)
        self.c= Elemento(img= C)
        self.d= Elemento(img= D)
        self.celula_1.entra(self.celula,x=50,y=50,z=50)
        self.celula_2.entra(self.celula,x=60,y=60,z=60)
        self.celula_3.entra(self.celula,x=70,y=70,z=70)
        self.celula_4.entra(self.celula,x=80,y=80,z=80)
        self.celula_5.entra(self.celula,x=90,y=90,z=90)
        self.celula_6.entra(self.celula,x=100,y=100,z=100)
        self.a.entra(self.celula,x=200,y=50,z=50,Tit= "Eu sou a membrana plasmatica")
        self.b.entra(self.celula,x=250,y=60,z=60,Tit= "Eu sou um citoplasma")
        self.c.entra(self.celula,x=300,y=70,z=70,Tit= "Eu sou o nucleo")
        self.d.entra(self.celula,x=350,y=80,z=80,Tit= "Eu sou o material do nucleo espalhado no citoplasma")
    
    """
    
if __name__ == "__main__":
    Fase2()
    
    