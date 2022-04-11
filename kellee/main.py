# lorinda.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, JOGO
from _spy.vitollino.main import Inventario as inv 
from anastasia.main import Associa, SF
from tracy.main import Personagem
# salas do games da Angelica, lorinda-lisa-libby e kellee
STYLE.update(width=600, height="600px")
#INICIO = "https://i.imgur.com/6vAoUiq.png"
FOCO="https://i.imgur.com/6e096Va.png"
MARIA = "https://i.imgur.com/FukdPW2.png"
ROSALINDA = "https://imgur.com/0Dv7w29.png"
LABORATORIO = "https://imgur.com/Ley1AXg.jpg"
LABORATORIO_1 = "https://imgur.com/Ley1AXg.jpg"
LABORATORIO_2 = "https://s1.static.brasilescola.uol.com.br/be/conteudo/images/o-nucleo-envolto-por-uma-membrana-apresenta-em-seu-interior-os-cromossomos-5a86b19fdc671.jpg"
LABORATORIO_3 = "https://s1.static.brasilescola.uol.com.br/be/conteudo/images/o-nucleo-envolto-por-uma-membrana-apresenta-em-seu-interior-os-cromossomos-5a86b19fdc671.jpg"
LABORATORIO_4 = "https://s1.static.brasilescola.uol.com.br/be/conteudo/images/o-nucleo-envolto-por-uma-membrana-apresenta-em-seu-interior-os-cromossomos-5a86b19fdc671.jpg"
LABORATORIO_5 = "https://s1.static.brasilescola.uol.com.br/be/conteudo/images/o-nucleo-envolto-por-uma-membrana-apresenta-em-seu-interior-os-cromossomos-5a86b19fdc671.jpg"
ESTRTURA= "https://imgur.com/iaGv545.png"
#NPC="https://i.imgur.com/hU2mulx.png"
DNA= "https://i.imgur.com/khPaSvV.png"
NPC="https://imgur.com/VcPXMYC.png"
ENIGMA= "https://i.imgur.com/pwI7UL8.png"
NUCLEO="https://i.imgur.com/0OsquxQ.jpeg" # trocar essa imagemTROCADA
PAREDE="https://i.imgur.com/khPaSvV.png" # trocar essa imagem
ORGANELA="https://i.imgur.com/kfZUTfR.png" # trocar essa imagemTROCADA
COMPLEXOG="https://i.imgur.com/PUbco5w.png" # trocar essa imagemTROCADA
RNA= "https://i.imgur.com/Fiq5UIH.png" # trocar essa imagemTROCADA


class Fase3():
    def __init__(self,*_):
        #self.inicio=Cena(img=INICIO)
        #self.foco=Elemento(img=FOCO, x=250, y=280, w=90, h=150, style={"opacity": 0})
        #self.foco.entra(self.inicio)
        
        self.laboratorio=Cena(img=LABORATORIO)
        #self.maria=Elemento(img=MARIA, x=300, y=400, w=180, h=200, tit='Oi, Dra. Rosalinda! Sou sua fã!  Li todos os seus livros e seu artigo sobre "Direcionamento de Proteínas", ou seja, como as proteínas percorrem toda a célula.')
        #self.rosalinda=Elemento(img=ROSALINDA, x=100, y=400, w=180, h=200, tit="As proteínas são muito importantes para a nossa saúde e beleza! Precisamos estuda-las para nos manter saudáveis, fortes e bonitas. ")
        mtit = ('Oi, Dra. Rosalinda! Vim ao seu laboratório pois sou sua fã!  Admiro seu trabalho sobre a difração dos raio-x e me encanta saber que foi você quem realmente descobriu o formato helicoidal do DNA",' 
        'Quero aprender sobre proteínas, me ajuda?')
        self.maria=Elemento(img=MARIA, x=200, y=280, w=280, h=300, texto=mtit)
        rtit = ("As proteínas são moléculas orgânicas fundamentais para os seres vivos, elas são muito importantes para a nossa saúde e beleza!"
        "Precisamos estuda-las para nos manter saudáveis, fortes e bonitas. ")
        self.rosalinda=Elemento(img=ROSALINDA, x=300, y=280, w=280, h=300, texto=rtit)
        self.maria.entra(self.laboratorio)
        self.rosalinda.entra(self.laboratorio)
        #self.foco.vai=self.laboratorio.vai
        self.laboratorio_1 = Cena(img= LABORATORIO_1)
        # self.laboratorio.direita=self.laboratorio_1
        self.laboratorio.direita=Cena(vai=self.some)
        self.laboratorio.vai()
    
    def some (self):
        def sumir(ev=0):
            self.rosalinda.x=-100000
        self.laboratorio_1.vai()
        self.laboratorio_1.esquerda=self.laboratorio
        self.rosalinda.entra(self.laboratorio_1)
        fala_rosalinda = "sim claro"
        self.rosalinda.vai = Texto(self.laboratorio_1, fala_rosalinda, foi=sumir).vai
        #self.elt.onclick = some
        self.maria.entra(self.laboratorio_1)
        self.maria.texto=" Quais as funções delas no nosso organismo?" 
        self.rosalinda.tit= "Elas tem inúmeras funções. Tem função estrutural, pois são os constituintes básicos das fibras musculares, cabelo, ossos, dentes e pele. Também desempenham importante papel na proteção do organismo contra os agentes patológicos, é o caso dos anticorpos; na constituição de hormônios importantes para o bom funcionamento do organismo, em especial, a insulina, o FSH e o LH; na aceleração das reações químicas que acontecem no organismo."
        self.laboratorio_1.direita=Cena(vai=self.parte_2)
        #rosalinda some 
    
    def parte_2(self):
        self.laboratorio_2= Cena(img=LABORATORIO_2)
        #self.laboratorio_1.direita=self.laboratorio_2
        self.laboratorio_2.vai()
        self.laboratorio_2.esquerda=self.laboratorio_1
        self.maria.entra(self.laboratorio_2)
        self.maria.tit= " Como ela desapareceu?"
        self.npc= Elemento(img=NPC,y=400,w=200,h=200, tit=" Você não deve esquecer do seu verdadeiro propósito buscar, desvendar um grande enigma celular. Você deve sempre lembrar que para uma célula funcionar, todas as suas organelas conectadas devem estar. ")
        self.npc.entra(self.laboratorio_2)
        self.laboratorio_2.direita=Cena(vai=self.parte_3)
    
    def parte_3(self):
        self.laboratorio_3=Cena(img=LABORATORIO_3)
        self.laboratorio_3.vai()
        #self.laboratorio_2.direita=self.laboratorio_3
        self.laboratorio_3.esquerda=self.laboratorio_2
        self.npc.entra(self.laboratorio_3)
        self.maria.entra(self.laboratorio_3)
        self.npc.tit=" Maria ele não é muito simpático. É o todo poderoso! E se acha"
        self.maria.tit="Maria o observa atentamente,Maria caminha pelo meio daquele material gelatinoso e se aproximadele.Ele percebe que está sendo observado e olha com uma cara não muito amigavel.quem é você?"
        self.dna=Elemento(img= DNA, y=450,x=300,tit="COMO, VOCÊ NÃO SABE MEU NOME!?DE QUE PLANETA VOCÊ É?!EU SOU O MAIORAL!! ")
        self.dna.entra(self.laboratorio_3)
        self.laboratorio_3.direita=Cena(vai=self.parte_4)

    def parte_4(self):
        self.laboratorio_4=Cena(img=LABORATORIO_4)
        self.laboratorio_4.vai()
        self.laboratorio_4.esquerda=self.laboratorio_3
        self.dna.entra(self.laboratorio_4)
        self.npc.entra(self.laboratorio_4)
        self.dna.tit= "Vá estudar garota!"
        self.npc.tit=" Responda o enigma: No meu interior há uma molécula constituída por letras que se encaixam perfeitamente seguindo uma determinada ordem. Quando nela há algum erro pode provocar uma doença ou mutação. Monte o quebra-cabeça e passe de fase."
        self.laboratorio_4.direita=Cena(vai=self.parte_5)
        
        #GABARITO DNA  (ácido dexoxirribonucleico) COMO PODEMOS COLOCAR ISSO ??

    def parte_5(self):
        from anastasia.main import Swap
        self.laboratorio_5=Cena(img=LABORATORIO_5)
        self.laboratorio_5.vai()
        text = Texto(self.laboratorio_5, "Foi!", foi=Fase4)
        Swap(JOGO,ENIGMA,self.laboratorio_5, x=50, y=50, w=500,h=500, venceu=text)
        
#fase3()

class Fase4():  # SEM NENHUMA IMAGEM
    def __init__(self):
        self.maria=Elemento(img=MARIA, tit="Não consigo sair daqui")
        self.nucleo=Cena(img=NUCLEO)
        self.nucleo.vai()
        self.parede=Cena(img=PAREDE)
        
        
        self.maria.entra(self.nucleo)
        #self.nucleo.direita=self.parede
        self.parede.esquerda=self.nucleo
        
        self.npc=Elemento(img=NPC, x=200, tit= "Atenção garota, veja o DNA")
        self.dna=Elemento(img=DNA, x=300, tit= "Só eu trabalho aqui? Vou ter que criar um RNA para me ajudar.")
        self.rna=Elemento(img=RNA, x=300, tit= " Vamos lá galera! Produzindo proteínas. ") #aparece depois do dna
        self.npc.entra(self.nucleo)
        self.dna.entra(self.nucleo)
        self.rna.entra(self.nucleo)
        self.nucleo.direita=Cena(vai=self.cena_parede)
        
    def cena_parede(self, *_):
        self.parede=Cena(img=PAREDE)
        self.npc=Elemento(img=NPC, x=100,tit="se vc acertar os processos irá ganhar moléculas de atp")
        self.maria=Elemento(img=MARIA, tit="nossas, quantas proteínas diferentes são formadas")
        self.npc.entra(self.parede)
        self.maria.entra(self.parede)
        Texto(self.parede,"Marque os processos que o DNA executa para a produção de proteína",foi=self.pergunta).vai()
        self.parede.vai()
        self.parede.esquerda=self.nucleo
        
        self.acabou = 2
        #self.pergunta()
    def pergunta(self, ev=None):
        if self.acabou == 0:
            return
        self.acabou -= 1
        self.multi = Texto(self.parede, "Quais são os processos do DNA?",
                           foi=self.resposta, A= "Transcrição, tradução e proteína", B= "Fagocitose,tradução e proteína", C= "Pinocitose,tradução e proteína", D= "Fagocitose,transdução e proteína").vai()

    def mover(self, ev=None):
        self.movente.x=800
        
    def resposta(self, rep):
        if rep == "A":
            Texto(self.parede, "Ganhou um ATP!", foi=Fase5).vai()
        else:
            Texto(self.parede, "Ops não acertou!", foi=self.pergunta).vai()
#fase4()
SETA = "https://i.imgur.com/N3JNtRW.png"

class Fase5():
    def __init__(self):
    
        self.organela=Cena(img=ORGANELA)
        self.rosalinda=Elemento(img=ROSALINDA, x=0, y=350, w=200, h=200, tit ="Maria, olhe a estrutura ao seu lado.", cena=self.organela)
        self.maria=Elemento(img=MARIA, x=150, y=350, w=200, h=200, tit=" Quem é você? ", cena=self.organela)
        self.complexog=Elemento(img=COMPLEXOG, x=350, y=350, w=200, h=200,  tit="Sou uma organela, ué", cena=self.organela)
        self.organela.direita=Cena(vai=self.mariafala)
        vai_reticulo = Elemento(SETA, tit="Conheça melhor o Retículo Endoplasmático clicando nesta seta", x=20, y=200,
        vai=self.viagem_reticulo, cena=self.organela)
        self.organela.vai()
        
    def viagem_reticulo(self, *_):
        from stacy.main import Reticulo
        Reticulo(voltar=self.mariafala)
    def mariafala(self, *_):
        self.organela=Cena(img=ORGANELA)
        self.maria=Elemento(img=MARIA, x=100, y=400, w=200, h=200, tit="Sim, mas qual é o nome dele? Será que ele pode me ajudar a sair daqui?", cena=self.organela)
        self.npc=Elemento(img=NPC, x=300, y=475, tit="Ele veio da Itália, era histologista, deu uma parte do meu nome para essa organela.Qual o seu nome?", cena=self.organela)
        self.organela.vai()
        self.acabou = 2
        self.pergunta()
    def pergunta(self, ev=None):
        if self.acabou == 0:
            return
        self.acabou -= 1
        self.multi = Texto(self.organela, "Sou responsável por armazenar, transformar e exportar as substâncias produzidas no retículo endoplasmático liso e rugoso.Qual o meu nome?",
                           foi=self.resposta, A= "Lisossomo", B= "Peroxissomo ", C= "Complexo de Golgi", D= "Ribossomo").vai()

    def mover(self, ev=None):
        self.movente.x=800
    def resposta(self, rep):
        from naomi.main import Fase6

        if rep == "C":
            Texto(self.organela, "Ganhou um ATP!", foi=Fase6).vai()
        else:
            Texto(self.organela, "Ops! Não acertou", foi=self.pergunta).vai()

            
    
if __name__ == "__main__":
    #Fase3()
    Fase5()

    
    
    
    
    
    