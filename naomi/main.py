# lorinda.naomi.main.py
from _spy.vitollino.main import Cena, Elemento,Texto, STYLE
from courtney.main import MOCHILA
STYLE.update(width=1000, height="600px")

class Move:
    def __init__(self):
        
        def pegou_atp(ev=None):
            ATP = "https://i.imgur.com/k0Az1Ts.png"
            self.ATP = Elemento(img=ATP, tit="ATP", x=600, y=500, cena=self.parede, drag=True)
        NPC = "https://i.imgur.com/slnDrGI.png"
        RIBOSSOMA = "https://i.imgur.com/Tf5yrKb.png"
        LISOSSOMA = "https://i.imgur.com/g0OplxP.png"
        MARIA = "https://i.imgur.com/4yrnNgS.png"
        CELULAR = "https://i.imgur.com/hUBdEPI.jpg"
        MOCHILA.esvazia_mochila()
        MOCHILA.ganha_atp()
        #MOCHILA.quando_pega(pegou_atp)

        self.parede = Cena("https://i.imgur.com/sGoKfvs.jpg")
        self.parede.vai()
        self.matou_organela = True
        self._parede_vai = self.parede.vai
        self.parede.vai = self.pegou_atp
        self.NPC = Elemento(img=NPC, x=800, cena=self.parede, vai=self.aconselha)
        #self.NPC = Elemento(img=NPC, x=800, cena=self.parede, vai=self.pegou_atp)
        self.celular = Elemento(img=CELULAR, x=800, y=500, w=100, h=100, cena=self.parede,
        drop={'ATP': self.usou_o_celular})
        self.movente = Elemento(img=LISOSSOMA, w=60, h=60, cena=self.parede,
            style={"transition": "left 5s, top 5s"})
        self.movente.elt.ontransitionend = self.persegue_maria
        self.movente1 = Elemento(img=LISOSSOMA, w=60, h=60, x=200, cena=self.parede,
            style={"transition": "left 5s, top 5s"})
        self.organela = Elemento(img=RIBOSSOMA, x=300, y=400, w=60, h=60, cena=self.parede,
            style={"transition": "opacity 2s"})
        self.maria = Elemento(img=MARIA, x=600, y=400, cena=self.parede, vai=self.usou_o_celular,
            style={"transition": "left 4s"})
        self.maria.elt.ontransitionend = self.encosta_maria
        txt0 = ('De repente Maria vê uma bolinha se desprendo do complexo de golgi,'
            'ela encosta numa organela que está com uma placa escrito sem função,'
            'a bolinha vem na direção dessa organela e destrói a organela.')
        txt = ('Maria vê uma organela que está com uma placa escrito sem função,'
            'e vai ver o do que se trata.')
        Texto(self.parede, txt, foi=self.move_maria).vai()
        self.acabou = 2
        # self.pergunta()
        
    def pegou_atp(self, ev=None):
        ATP = "https://i.imgur.com/k0Az1Ts.png"
        self.ATP = Elemento(img=ATP, tit="ATP", x=600, y=500, cena=self.parede, drag=True)
        self._parede_vai()
        
    def usou_o_celular(self, atp, ev=None):
        txt = ('Na pesquisa vc descobre que é o lisossoma. Ao chamar pelo nome eles vão embora')
        Texto(self.parede, txt, foi=self.vai_embora).vai()
        self.ATP.x = -1000
        
    def vai_embora(self, ev=None):
        self.movente.x=-600
        self.movente.y=-400
        self.movente1.x=200
        self.movente1.y=-400
    
    def pergunta(self, ev=None):
        if self.acabou == 0:
            return
        self.acabou -= 1
        self.multi = Texto(self.parede, "processos corretos?",
                           foi=self.resposta, A= "a b", B= "b c", C= "c d", D= "b d").vai()
    def aconselha(self, ev=None):
        conselho = "Pegue um ATP da mochila e jogue no celular"
        self.multi = Texto(self.parede, conselho).vai()

    def move_maria(self, ev=None):
        self.maria.x=340

    def encosta_maria(self, ev=None):
        txt = ('Ela encosta na organela que está com a placa escrito sem função.'
        'De repente Maria vê umas bolinhas se desprendo do complexo de golgi,'
            'as bolinhas vem na direção dessa organela e destrói a organela.')
        Texto(self.parede, txt, foi=self.mover).vai() if self.matou_organela else None
        # self.matou_organela = False

    def foge_maria(self, ev=None):
        self.maria.x=800


    def persegue_maria(self, ev=None):
        self._persegue_maria() if self.matou_organela else None
        self.matou_organela = False


    def _persegue_maria(self, ev=None):
        self.organela.o = 0
        self.movente.x=700
        self.movente.y=400
        self.movente1.x=650
        self.movente1.y=400
        self.maria.x=800

    def mover(self, ev=None):
        self.movente.x=300
        self.movente.y=400
        self.movente1.x=300
        self.movente1.y=400
        # self.maria.x=400
        
    def resposta(self, rep):
        if rep == "A":
            Texto(self.parede, "ganhou um ATP!").vai()
        else:
            Texto(self.parede, "Ops não acertou", foi=self.pergunta).vai()

class Fase7()
    def __init__(self):
        self.mitocondria=Cena(img=MITOCONDRIA)
        self.mitocondria.vai()
        self.glicose=Personagem(img=GLICOSE, x=0, afala"")
        self.ribossomo=Personagem(img=RIBOSSOMO,x=200,afala"Ribossomo:Porque perdi minha outra parte e preciso encontrá-la. Eu preciso gerar proteínas",responde=self.ribossomofala)
        self.maria=Personagem(img=MARIA, afala"Maria: por que você está triste?",responde=self.ribossomo)
        self.maria.entra(self.mitocondria)
        self.ribossomo.entra(self.mitocondria)
       
        self.maria.fala()
        self.ribossomo.fala()
   
    def ribossomofala(self):
        self.mitocondria=Cena(img=MITOCONDRIA)
        self.mitocondria.vai()
        self.ribossomo=Personagem(img=ribossomo,x=0, afala="No caminho eu te explico...",responde=)
        self.maria=Personagem(img=MARIA, afala="Mas está tudo escuro, como vamos achar?",responde=self.ribossomo)
        self.maria.entra(self.mitocondria)
        self.ribossomo.entra(self.mitocondria)
       
        self.maria.fala()
        self.ribossomo.fala()
if __name__ == "__main__":            
     
    #Move()