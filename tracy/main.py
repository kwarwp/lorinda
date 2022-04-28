# lorinda.tracy.main.py
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
NPC="https://imgur.com/VcPXMYC.png"
ENIGMA= "https://i.imgur.com/pwI7UL8.png"
NUCLEO="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
PAREDE="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
ORGANELA="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
COMPLEXOG="https://i.imgur.com/hU2mulx.png" # trocar essa imagem
RNA= "https://i.imgur.com/khPaSvV.png" # trocar essa imagem


class Personagem(Elemento):
    def __init__(self, img=MARIA, x=300, y=400, w=180, h=200, afala="", responde=None, **kwargs):
        super().__init__(img=img, x=x, y=y, w=w, h=h, **kwargs)
        self.afala = afala
        self.responde = responde
        
    def fala(self, cena=None, responde=None, texto=""):
        Texto(self.cena, texto if texto else self.afala, foi=responde if responde else self.responde).vai()



class Fase3():
    def __init__(self):
        self.laboratorio=Cena(img=LABORATORIO)
        def rosalinda_fala(_=0):
            rosalinda = ("Rosalinda: As proteínas são muito importantes, para a nossa saúde e beleza!"
            " Precismos estuda-las, para nos manter saudáveis, fortes e bonitas. ")
            Texto(self.laboratorio, rosalinda, foi=self.some).vai()
            
        fala = ('Maria: Oi,  Dr. Rosalinda sou sua fã, li todos os seus livros e seu artigo'
        ' sobre "Direcionamento de Proteínas", ou seja, como as proteínas percorrem toda a célula')
        self.maria = Personagem(responde=rosalinda_fala, afala=fala)
        self.maria.entra(self.laboratorio)
        self.maria.fala()
        #self.maria=Elemento(img=MARIA, x=300, y=400, w=180, h=200, tit='oi,  Dr. Rosalinda sou sua fã, li todos os seus livros e seu artigo sobre "Direcionamento de Proteínas", ou seja, como as proteínas percorrem toda a célula')
        self.rosalinda=Elemento(img=ROSALINDA, x=100, y=400, w=180, h=200, tit="as proteínas são muito importantes, para a nossa saúde e beleza! Precismos estuda-las, para nos manter saudáveis, fortes e bonitas. ")
        self.rosalinda.entra(self.laboratorio)
        self.laboratorio_1 = Cena(img= LABORATORIO_1)
        # self.laboratorio.direita=self.laboratorio_1
        self.laboratorio.direita=Cena(vai=self.some)
        self.laboratorio.vai()
    
    def some (self, ev=0):
        def sumir(ev=0):
            self.rosalinda.x=-100000
        self.laboratorio_1.vai()
        self.laboratorio_1.esquerda=self.laboratorio
        self.rosalinda.entra(self.laboratorio_1)
        fala_rosalinda = "sim claro"
        self.rosalinda.vai = Texto(self.laboratorio_1, fala_rosalinda, foi=sumir).vai
        #self.elt.onclick = some
        self.maria.entra(self.laboratorio_1)
        maria_texto=("Maria: Sim, elas são importantes. Então quer dizer que se eu não me alimentar bem,"
        " posso ter cabelos, unhas e pele feias?") 
        self.maria.fala(self.laboratorio_1,responde=self.parte_2, texto= maria_texto) 
        self.rosalinda.tit= ""
        self.laboratorio_1.direita=Cena(vai=self.parte_2)
        #rosalinda some 
    
    def parte_2(self, ev=0):
        self.laboratorio_2= Cena(img=LABORATORIO_2)
        texto = ("Roboide: Você não deve esquecer do seu verdadeiro propósito buscar,"
                 " desvendar um grande enigma celular. Você deve sempre lembrar que para uma célula funcionar,"
                 " todas as suas organelas conectadas devem estar. Quando uma proteína conseguir transportar,"
                 " livre você estará!")
        #self.laboratorio_1.direita=self.laboratorio_2
        self.laboratorio_2.vai()
        self.laboratorio_2.esquerda=self.laboratorio_1
        self.maria.entra(self.laboratorio_2)
        maria_texto= "Maria:  Como ela desapareceu?"
        self.npc= Personagem(img=NPC,x=0, y=400,w=160,h=160, afala=texto, responde=self.parte_3)
        self.maria.fala(self.laboratorio_2,responde=self.npc.fala, texto=maria_texto) 
        
        self.npc.entra(self.laboratorio_2)
        self.laboratorio_2.direita=Cena(vai=self.parte_3)
    
    def parte_3(self):
        self.laboratorio_3=Cena(img=LABORATORIO_3)
        self.laboratorio_3.vai()
        #self.laboratorio_2.direita=self.laboratorio_3
        self.laboratorio_3.esquerda=self.laboratorio_2
        self.npc.entra(self.laboratorio_3)
        self.maria.entra(self.laboratorio_3)
        self.npc.afala = "Roboide: ele não é muito simpático"
        self.npc.responde = self.parte_4
        maria_texto= "Maria:   quem é você?"
        self.dna=Personagem(img= DNA, y=400,x=200, responde=self.npc.fala, afala="COMO, VOCÊ NÃO SABE MEU NOME? DE QUE PLANETA VOCÊ É?EU SOU O MAIORAL! ")
        self.dna.entra(self.laboratorio_3)
        self.maria.fala(self.laboratorio_3,responde=self.dna.fala, texto=maria_texto) 
        self.laboratorio_3.direita=Cena(vai=self.parte_4)

    def parte_4(self):
        self.laboratorio_4=Cena(img=LABORATORIO_4)
        self.laboratorio_4.vai()
        self.laboratorio_4.esquerda=self.laboratorio_3
        self.dna.entra(self.laboratorio_4)
        self.npc.entra(self.laboratorio_4)
        self.maria.entra(self.laboratorio_4)
        self.dna.afala="vá estudar garota!"
        self.dna.responde = self.parte_5
        self.npc.afala=" Responda o enigma: Sou constituído por letras, que se encaixam perfeitamente, seguindo uma determinada ordem. Quando tem algum erro, pode provocar uma doença ou mutação."
        self.npc.responde = self.dna.fala
        self.npc.fala()
        self.laboratorio_4.direita=Cena(vai=self.parte_5)
        
        #GABARITO DNA  (ácido dexoxirribonucleico) COMO PODEMOS COLOCAR ISSO ??

    def parte_5(self):
        from anastasia.main import Swap
        self.laboratorio_5=Cena(img=LABORATORIO_5)
        self.laboratorio_5.vai()
        text = Texto(self.laboratorio_5, "foi!", foi=Fase4)
        Swap(JOGO,ENIGMA,self.laboratorio_5, x=50, y=50, w=500,h=500, venceu=text)
        
class Fase4():  # SEM NENHUMA IMAGEM
    def __init__(self):
        self.rna=Personagem(img=RNA, x=0,afala= "RNA:Vamos lá galera, produzindo proteínas ",responde=self.fala_npc) #aparece depois do dna
        self.dna=Personagem(img=DNA,x=100 ,afala= "DNA:só eu trabalho aqui, vou ter que criar um RNA para me ajudar",responde=self.rna.fala)
        self.npc=Personagem(img=NPC,x=200, afala= "Roboide: Atenção garota, veja o DNA",responde=self.dna.fala)
        self.maria=Personagem(img=MARIA, afala="Maria: não consigo sair daqui",responde=self.npc.fala)
        self.nucleo=Cena(img=NUCLEO)
        self.nucleo.vai()
        self.parede=Cena(img=PAREDE)
        
        
        self.maria.entra(self.nucleo)
        #self.nucleo.direita=self.parede
        self.parede.esquerda=self.nucleo
        
        self.npc.entra(self.nucleo)
        self.dna.entra(self.nucleo)
        self.rna.entra(self.nucleo)
        self.maria.fala()
        self.nucleo.direita=Cena(vai=self.npc)
        
    def fala_npc(self):
        self.maria1=Personagem(img=MARIA,afala="Marque os processos que o DNA executa para a produção de proteína")
        self.npc.afala="se vc acertar os processos irá ganhar moléculas de atp"
        self.maria.afala="nossas, quantas proteínas diferentes são formadas"
        self.maria.responde=self.npc.fala
        self.npc.responde=self.maria1.fala
        self.npc.entra(self.parede)
        self.maria.entra(self.parede)
        self.maria1.entra(self.parede)
        
        self.parede.vai()
        self.maria.fala()
        
        self.maria1.responde=self.pergunta
      
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
            Texto(self.parede, "Ops não acertou", foi=self.pergunta).vai()

class Fase5():
    def __init__(self):
        self.organela=Cena(img=ORGANELA)
        self.rosalinda=Elemento(img=ROSALINDA,x=200,y=400)
        self.rosalinda.entra(self.organela)
        self.organela.vai()
        self.complexog=Personagem(img=COMPLEXOG,x=0, afala="Sou uma organela, ué",responde=self.mariafala)
        self.maria=Personagem(img=MARIA, afala="Maria: quem é você? ",responde=self.complexog.fala)
        self.maria.entra(self.organela)
        self.complexog.entra(self.organela)
        self.organela.direita=Cena(vai=self.mariafala) 
        Texto(self.organela,"Maria, olhe a estrutura",foi=self.maria.fala).vai()
        
    def mariafala(self,ev=0):
        self.organela=Cena(img=ORGANELA)
        self.organela.vai()
        self.npc=Personagem(img=NPC,x=0, afala="Vim da Itália, era histologista, dei uma parte do meu nome para essa organela.Qual é meu nome?",responde=self.pergunta)
        self.maria=Personagem(img=MARIA, afala="Sim, mas qual é seu nome? Pode me ajudar a sair daqui",responde=self.npc.fala)
        self.maria.entra(self.organela)
        self.npc.entra(self.organela)
        self.acabou = 2
        self.maria.fala()
    def pergunta(self, ev=None):
        if self.acabou == 0:
            return
        self.acabou -= 1
        self.multi = Texto(self.organela, "Qual o meu nome?",
                           foi=self.resposta, A= "Lisossomo", B= "Peroxissomo ", C= "Complexo de Golgi", D= "Ribossomo").vai()

    def mover(self, ev=None):
        self.movente.x=800
    def resposta(self, rep):
        from naomi.main import Fase7
        if rep == "C":
            Texto(self.organela, "Ganhou um ATP!", foi=Fase7).vai()
        else:
            Texto(self.organela, "Ops não acertou", foi=self.pergunta).vai()
        
        

if __name__ == "__main__":
    #Fase3()
    #Fase4()
    Fase5()
