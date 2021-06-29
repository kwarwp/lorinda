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
        Texto(self.parede,"Marque os processos que o DNA executa para a produção de proteína").vai()
        self.parede.vai()
        self.parede.esquerda=self.nucleo

        
        #como colocar essa parte no jogo? sei que esta desorganizado 
        #self.proteina=Elemento(img=PROTEINA,cena=self.cena,vai=self.mover,style={"transition":"left2s"}) #FICAR PASSANDO PELA CELULA
        #self.proteina.entra(self.parede)
        self.jogo=Associa(self.parede, caixa=300, borda=20, acertou=self.acertou, acertos=3)
        self.jogo.nome(nome="Tradução"tit=0, x=450, y=50)#clicar e acertar
        self.jogo.nome(nome="Retículo", tit=1, x=750, y=50)
        self.jogo.nome(nome="Transcrição", tit=2, x=450, y=150)#clicar e acertar
        self.jogo.nome(nome="Fagocitose", tit=3, x=850, y=150)
        self.jogo.nome(nome="Pinocitose", tit=4, x=450, y=250)
        self.jogo.nome(nome="Proteína", tit=5, x=750, y=250)#clicar e acertar 
        
    def acertou(self):  
        Texto(self.parede, "Você acertou tudo! Está sabendo tudo de biologia, a ordem certa é transcrição-tradução-proteína",
        foi=MOCHILA.mostra_mochila).vai()
        MOCHILA.ganha_atp()
fase4()

class fase5():
    



    
    
    
    
    
    