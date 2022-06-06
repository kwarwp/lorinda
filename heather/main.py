# lorinda.heather.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, JOGO
from _spy.vitollino.main import Inventario as inv 
# from _spy.vitollino.jogos import
from anastasia.main import Associa, SF
from tracy.main import Personagem
from sarah.main import Ator, Fala, A, Roteiro
# salas do games da Angelica, lorinda-lisa-libby e kellee
STYLE.update(width=600, height="600px")
#INICIO = "https://i.imgur.com/6vAoUiq.png"
FOCO="https://i.imgur.com/6e096Va.png"
MARIA = "https://i.imgur.com/FukdPW2.png"
ROSALINDA = "https://imgur.com/0Dv7w29.png"
LABORATORIO = "https://imgur.com/Ley1AXg.jpg"
LABORATORIO_1 = "https://imgur.com/Ley1AXg.jpg"
LABORATORIO_2 = LABORATORIO_3 = LABORATORIO_4 = "https://i.imgur.com/C3NTDfU.jpg"
LABORATORIO_5 = "https://i.pinimg.com/564x/b1/b7/99/b1b799b781cdec873b72fee24ef4c03e.jpg"
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
        def sumir(ev=0):
            self.rosalinda.x=-100000
        c = self.laboratorio=Cena(img=LABORATORIO)
        mtit = ('Oi, Dra. Rosalinda! Vim ao seu laboratório pois sou sua fã!  Admiro seu trabalho sobre a difração dos raio-x e me encanta saber que foi você quem realmente descobriu o formato helicoidal do DNA",' 
        'Quero aprender sobre proteínas, me ajuda?')
        rtit = ("As proteínas são moléculas orgânicas fundamentais para os seres vivos, elas são muito importantes para a nossa saúde e beleza!"
        "Precisamos estuda-las para nos manter saudáveis, fortes e bonitas. ")
        texto=" Quais as funções delas no nosso organismo?" 
        rose_fala = ("Elas tem inúmeras funções. Tem função estrutural, "
                     "pois são os constituintes básicos das fibras musculares, cabelo, ossos, dentes e pele.")
        rose_mais = (" Também desempenham importante papel na proteção do organismo contra os agentes patológicos,"
                     " é o caso dos anticorpos; na constituição de hormônios importantes para o bom funcionamento do organismo,"
                     " em especial, a insulina, o FSH e o LH; na aceleração das reações químicas que acontecem no organismo.")
        m = self.maria=Elemento(img=MARIA, x=100, y=280, w=280, h=300)
        r = self.rosalinda=Elemento(img=ROSALINDA, x=300, y=280, w=280, h=300)
        self.maria.entra(self.laboratorio)
        self.rosalinda.entra(self.laboratorio)
        ele = [Ator(self.maria,"Maria", 0.4, A.e),
               Ator(self.rosalinda, "Dr. Rosalinda", 0.4, A.e)]
        rot = [
               Fala(m, mtit, r, None),
               Fala(r, "Sim, claro!", m, None),
               Fala(m, "O que são as proteínas?", r, None),
               Fala(r, rtit, m, None),
               Fala(m, texto, r, None),
               Fala(r, rose_fala, m, None),
               Fala(m, "Estou impressionada! Elas são muito importantes!", r, None),
               Fala(r, rose_mais, m, sumir),
               Fala(m, "Dr. Rosalinda? Doutora?", None, self.parte_2),
               ]
        Roteiro(c, rot, ele, None)
        self.laboratorio_1 = Cena(img= LABORATORIO_1)
        self.laboratorio.vai()
    
    
    def parte_2(self):
        def desce():
            d.y = 250
        c = self.laboratorio_2= Cena(img=LABORATORIO_2)
        #self.laboratorio_1.direita=self.laboratorio_2
        self.laboratorio_2.vai()
        self.laboratorio_2.esquerda=self.laboratorio_1
        texto= " Como ela desapareceu?"
        npc = "Dr. Robert"
        robert = ("Você não deve esquecer do seu verdadeiro propósito buscar, desvendar um grande enigma celular."
        " Você deve sempre lembrar que para uma célula funcionar, todas as suas organelas conectadas devem estar. ")
        rob_ob=("Maria observa atentamente a estrutura onde está, ela tem duas membranas,"
        " poros e no seu interior alguém dá muitas ordens."
        " Ela percebe que ele a olha com uma cara não muito amigável")
        quem_ = "Quem é você? Dr. Robert, você o conhece?"
        amigavel = "Maria, ele não é muito simpático. É o todo poderoso! Ele se acha."
        dna_e = "Como você não sabe o meu nome? De que planeta você é?! EU SOU O MAIORAL!!"
        desvende = (" Desvende o enigma: No interior do núcleo há uma molécula constituída por letras que se encaixam"
            " perfeitamente seguindo uma determinada ordem. Quando nela há algum erro pode provocar uma doença ou mutação."
            " Monte o quebra-cabeça e passe de fase.")

        r = self.npc= Elemento(img=NPC, y=400,w=200,h=200) #, texto=npc, foi=self.parte_3)
        m = self.maria
        self.maria.entra(self.laboratorio_2)
        self.npc.entra(self.laboratorio_2)
        d = self.dna=Elemento(img= DNA, tit="DNA", x=255,y=150,w=200, h=200)
        ele = [Ator(self.maria,"Maria", 0.4, A.e), Ator(self.dna,"DNA", 0.4, A.e),
               Ator(self.npc, npc, 0.6, A.e)]
        rot = [
               Fala(m, texto, r, None),
               Fala(r, robert, m, None),
               Fala(m, "Esta estrutura!", r, lambda *_: d.entra(c)),
               Fala(r, rob_ob, m, None),
               Fala(m, quem_, r, None),
               Fala(r, amigavel, m, None),
               Fala(m, "Dá para notar daqui. Mas afinal, quem é este sujeito?", d, desce),
               Fala(d, dna_e, m, None),
               Fala(m, "Que você se acha o maioral, já sabia, mas qual é o seu nome?", d, None),
               Fala(d, "Vai estudar, garota!", r, None),
               Fala(r, desvende, None, self.parte_5),
               ]
        Roteiro(c, rot, ele,None)
        
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
        a = self.rna=Elemento(img=RNA, x=450, y=50, w=150, h=150)
        d = self.dna=Elemento(img=DNA, x=300,y=0, w=200, h=200)
        r = self.npc=Elemento(img=NPC, x=200,y=25)
        m = self.maria=Elemento(img=MARIA, x=0, y=0, w=200, h=200)
        c = self.nucleo=Cena(img=NUCLEO)
        self.nucleo.vai()
        self.parede=Cena(img=PAREDE)
        
        
        self.maria.entra(self.nucleo)
        #self.nucleo.direita=self.parede
        self.parede.esquerda=self.nucleo
        
        self.npc.entra(self.nucleo)
        self.dna.entra(self.nucleo)
        #self.nucleo.direita=Cena(vai=self.cena_parede)
        npc = "Dr. Robert"
        texto= "Só eu trabalho aqui? Vou ter que criar um RNA para me ajudar."
        ele = [Ator(m,"Maria", 0.4, A.e), Ator(self.dna,"DNA", 0.4, A.e),
               Ator(r, npc, 0.6, A.e),
               Ator(a, "RNA", 0.6, A.e),
               Ator(d, "DNA", 0.6, A.e)]
        rot = [
               Fala(m, "Não consigo sair daqui", r, None),
               Fala(r, "Atenção Maria, veja o DNA", d, None),
               Fala(d, texto, a, lambda *_: a.entra(c)),
               Fala(a, "Vamos lá galera! Produzindo proteínas!", m, None),
               Fala(m, "Nossa! Quantas proteínas diferentes são produzidas!", d, None),
               Fala(d, "Realmente! Aqui somos produtivos, sempre fazendo muitas coisas.", m, None),
               Fala(m, "Alguém me explica como se sai daqui!", None, self.cena_parede)
               ]
        Roteiro(c, rot, ele,None)
        
    def cena_parede(self, *_):
        c = self.parede=Cena(img=PAREDE)
        m, r = self.maria, self.npc
        self.acabou = 2
        self.npc.entra(self.parede)
        self.maria.entra(self.parede)
        self.parede.vai()
        #self.parede.esquerda=self.nucleo
        npc = "Dr. Robert"
        ele = [Ator(r, npc, 0.6, A.e), Ator(m,"Maria", 0.4, A.e)]
               
        rot = [
               Fala(r, "Marque os processos que o DNA executa para a produção de proteína", m, None),
               Fala(m, "Se eu acertar, vai ter um jeito de sair daqui?.", r, None),
               Fala(r, "Se você acertar os processos, irá ganhar uma molécula de ATP", None, self.pergunta),
               ]
        Roteiro(c, rot, ele,None)
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
    
        c = self.organela=Cena(img=ORGANELA)
        g = self.complexog=Elemento(img=COMPLEXOG, x=350, y=150, w=200, h=200, cena=c)
        n = self.npc=Elemento(img=NPC, x=450, y=450, cena=c)
        self.acabou = 2
        m = self.maria=Elemento(img=MARIA, x=210, y=350, w=200, h=200, cena=c)
        r = self.rosalinda=Elemento(img=ROSALINDA, x=0, y=350, w=200, h=200, cena=c)
        vai_reticulo = Elemento(SETA, tit="Conheça melhor o Retículo Endoplasmático clicando nesta seta", x=20, y=150,
        vai=self.viagem_reticulo, cena=self.organela)
        self.organela.vai()
        #self.parede.esquerda=self.nucleo
        npc = "Dr. Robert"
        self.ele = [Ator(m,"Maria", 0.4, A.e), Ator(r, "Dr. Rosalinda", 0.6, A.e), Ator(n,npc, 0.4, A.e)]
               
        rot = [
               Fala(m, "Quem é você?", r, None),
               Fala(r, "Maria, olhe a estrutura ao seu lado.", n, None),
               Fala(n, "Quem a descobriu foi um histologista italiano, ele deu uma parte do seu nome para essa organela", m, None),
               Fala(m, "E esta seta vermelha, para que serve?", r, None),
               Fala(r, "É a porta para entrar em uma viagem de conhecimento do Retículo Endoplasmático! Eu recomendo!", m, None),
               Fala(m, "Sim, mas Dr. Robert, qual é o nome deste cientista? Será que ele pode me ajudar a sair daqui?", n, None),
               Fala(n, "É bem possível que ele ajude, mas você terá que acertar o seu nome", None, self.pergunta),
               ]
        Roteiro(c, rot, self.ele,None)
        
    def mariafala(self, *_):
        m, n, r = self.maria, self.npc, self.rosalinda
        self.organela.vai()
        rot = [
               Fala(m, "De volta a Citonópolis! Onde estavamos mesmo?", r, None),
               Fala(r, "Estávamos observando esta fascinante organela, com muitas dobras.", n, None),
               Fala(n, "Quem a descobriu foi um histologista italiano, ele deu uma parte do seu nome para essa organela", m, None),
               Fala(m, "Sim, mas Dr. Robert, qual é o nome deste cientista? Será que ele pode me ajudar a sair daqui?", n, None),
               Fala(n, "É bem possível que ele ajude, mas você terá que acertar o seu nome", None, self.pergunta),
               ]
        Roteiro(self.organela, rot, self.ele,None)
        
    def viagem_reticulo(self, *_):
        from stacy.main import Reticulo
        Reticulo(voltar=self.mariafala)
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
    # Fase3().parte_3()
    #Fase3() #.parte_2()
    Fase5()
