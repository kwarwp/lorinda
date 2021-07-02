# lorinda.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, JOGO
from _spy.vitollino.main import Inventario as inv 
from anastasia.main import Associa, SF
# salas do games da Angelica, lorinda-lisa-libby e kellee
STYLE.update(width=600, height="600px")

MARIA = "https://i.imgur.com/FukdPW2.png"
ROSALINDA = "https://imgur.com/0Dv7w29.png"
LABORATORIO = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_1 = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_2 = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_3 = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_4 = "https://imgur.com/c71g0qt.jpg"
LABORATORIO_5 = "https://imgur.com/c71g0qt.jpg"
ESTRTURA= "https://imgur.com/iaGv545.png"
DNA= "https://i.imgur.com/khPaSvV.png"
NPC="https://i.imgur.com/hU2mulx.png"
ENIGMA= "https://i.imgur.com/pwI7UL8.png"
NUCLEO="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
PAREDE="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
ORGANELA="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
COMPLEXOG="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
class fase3():
    def __init__(self):
        self.laboratorio=Cena(img=LABORATORIO)
        self.maria=Elemento(img=MARIA, x=300, y=400, w=180, h=200, tit='oi,  Dr. Rosalinda sou sua fã, li todos os seus livros e seu artigo sobre "Direcionamento de Proteínas", ou seja, como as proteínas percorrem toda a célula')
        self.rosalinda=Elemento(img=ROSALINDA, x=100, y=400, w=180, h=200, tit="as proteínas são muito importantes, para a nossa saúde e beleza! Precismos estuda-las, para nos manter saudáveis, fortes e bonitas. ")
        self.maria.entra(self.laboratorio)
        self.rosalinda.entra(self.laboratorio)
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
        self.maria.tit=" Sim, elas são importantes.Então quer dizer que se eu não me alimentar bem, posso ter cabelos, unhas e pele feias?" 
        self.rosalinda.tit= ""
        self.laboratorio_1.direita=Cena(vai=self.parte_2)
        #rosalinda some 
    
    def parte_2(self):
        self.laboratorio_2= Cena(img=LABORATORIO_2)
        #self.laboratorio_1.direita=self.laboratorio_2
        self.laboratorio_2.vai()
        self.laboratorio_2.esquerda=self.laboratorio_1
        self.maria.entra(self.laboratorio_2)
        self.maria.tit= " Como ela desapareceu?"
        self.npc= Elemento(img=NPC,y=400,w=160,h=160, tit=" Você não deve esquecer do seu verdadeiro propósito buscar, desvendar um grande enigma celular. Você deve sempre lembrar que para uma célula funcionar, todas as suas organelas conectadas devem estar. Quando uma proteína conseguir transportar, livre você estará!")
        self.npc.entra(self.laboratorio_2)
        self.laboratorio_2.direita=Cena(vai=self.parte_3)
    
    def parte_3(self):
        self.laboratorio_3=Cena(img=LABORATORIO_3)
        self.laboratorio_3.vai()
        #self.laboratorio_2.direita=self.laboratorio_3
        self.laboratorio_3.esquerda=self.laboratorio_2
        self.npc.entra(self.laboratorio_3)
        self.maria.entra(self.laboratorio_3)
        self.npc.tit=" ele não é muito simpático"
        self.maria.tit=" quem é você?"
        self.dna=Elemento(img= DNA, y=450,x=200, tit="COMO, VOCÊ NÃO SABE MEU NOME?DE QUE PLANETA VOCÊ É?EU SOU O MAIORAL! ")
        self.dna.entra(self.laboratorio_3)
        self.laboratorio_3.direita=Cena(vai=self.parte_4)

    def parte_4(self):
        self.laboratorio_4=Cena(img=LABORATORIO_4)
        self.laboratorio_4.vai()
        self.laboratorio_4.esquerda=self.laboratorio_3
        self.dna.entra(self.laboratorio_4)
        self.npc.entra(self.laboratorio_4)
        self.dna.tit="vá estudar garota!"
        self.npc.tit=" Responda o enigma: Sou constituído por letras, que se encaixam perfeitamente, seguindo uma determinada ordem. Quando tem algum erro, pode provocar uma doença ou mutação."
        self.laboratorio_4.direita=Cena(vai=self.parte_5)
        
        #GABARITO DNA  (ácido dexoxirribonucleico) COMO PODEMOS COLOCAR ISSO ??

    def parte_5(self):
        from anastasia.main import Swap
        self.laboratorio_5=Cena(img=LABORATORIO_5)
        self.laboratorio_5.vai()
        Swap(JOGO,ENIGMA,self.laboratorio_5, x=50, y=50, w=500,h=500)
        
fase3()

class fase4():  # SEM NENHUMA IMAGEM
    def __init__(self):
        self.maria=Elemento(img=MARIA, tit="não consigo sair daqui")
        self.nucleo=Cena(img=NUCLEO)
        self.nucleo.vai()
        self.parede=Cena(img=PAREDE)
        
        
        self.maria.entra(self.nucleo)
        #self.nucleo.direita=self.parede
        self.parede.esquerda=self.nucleo
        
        self.npc=Elemento(img=NPC, tit= "atenção garota, veja o DNA")
        self.dna=Elemento(img=DNA, tit= "só eu trabalho aqui, vou ter que criar um RNA para me ajudar")
        self.rna=Elemento(img=RNA, tit= " Vamos lá galera, produzindo proteínas ") #aparece depois do dna
        self.npc.entra(self.nucleo)
        self.dna.entra(self.nucleo)
        self.rna.entra(self.nucleo)
        self.nucleo.direita=Cena(vai=self.npc)
        
    def npc(self):
        self.parede=Cena(img=PAREDE)
        self.npc=Elemento(img=NPC,tit="se vc acertar os processos irá ganhar moléculas de atp")
        self.maria=Elemento(img=MARIA, tit="nossas, quantas proteínas diferentes são formadas")
        self.npc.entra(self.parede)
        self.maria.entra(self.parede)
        Texto(self.parede,"Marque os processos que o DNA executa para a produção de proteína",foi=self.anda).vai()
        self.parede.vai()
        self.parede.esquerda=self.nucleo
        
        self.acabou = 2
        self.pergunta()
    def pergunta(self, ev=None):
        if self.acabou == 0:
            return
        self.acabou -= 1
        self.multi = Texto(self.parede, "Quais são os processos do DNA?",
                           foi=self.resposta, A= "Tradução, Transdução e proteína", B= "Fagositose,Tradução e Proteína", C= "Pnocitose,Tradução e proteína", D= "Fagocitose,Transdução e Proteína").vai()

    def mover(self, ev=None):
        self.movente.x=800
        
    def resposta(self, rep):
        if rep == "A":
            Texto(self.parede, "ganhou um ATP!").vai()
        else:
            Texto(self.parede, "Ops não acertou", foi=self.pergunta).vai()
fase4()

class fase5():
    def __init__(self):
        self.organela=Cena(img=ORGANELA)
        self.rosalinda=Elemento(img=ROSALINDA,tit ="Maria, olhe a estrutura")
        self.maria=Elemento(img=MARIA, tit="  quem é você? ")
        self.complexog=Elemento(img=COMPLEXOPG, tit="Sou uma organela, ué")
        self.organela.direita=Cena(vai=self.mariafala) 
    def mariafala(self):
        self.organela=Cena(img=ORGANELA)
        self.maria=Elemento(img=MARIA, tit="sim, mas qual é seu nome? Pode me ajudar a sair daqu")
        self.npc=Elemento(img=NPC, tit="Vim da Itália, era histologista, dei uma parte do meu nome para essa organela.Qual é meu nome?")
        
        self.acabou = 2
        self.pergunta()
    def pergunta(self, ev=None):
        if self.acabou == 0:
            return
        self.acabou -= 1
        self.multi = Texto(self.parede, "Qual o meu nome?",
                           foi=self.resposta, A= "Lisossomo", B= "Perisoxomo ", C= "complexo de golgi", D= "ribossomo").vai()

    def mover(self, ev=None):
        self.movente.x=800
    def resposta(self, rep):
        if rep == "C":
            Texto(self.parede, "ganhou um ATP!").vai()
        else:
            Texto(self.parede, "Ops não acertou", foi=self.pergunta).vai()

            


    
    
    
    
    
    