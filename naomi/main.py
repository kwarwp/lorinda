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
        MARIA = "https://i.imgur.com/4yrnNgS.png"
        CELULAR = "https://i.imgur.com/hUBdEPI.jpg"
        MOCHILA.esvazia_mochila()
        MOCHILA.ganha_atp()
        #MOCHILA.quando_pega(pegou_atp)

        self.parede = Cena("https://i.imgur.com/sGoKfvs.jpg")
        self.parede.vai()
        self._parede_vai = self.parede.vai
        self.parede.vai = self.pegou_atp
        #self.NPC = Elemento(img=NPC, x=800, cena=self.parede, vai=self.aconselha)
        self.NPC = Elemento(img=NPC, x=800, cena=self.parede, vai=self.pegou_atp)
        self.celular = Elemento(img=CELULAR, x=800, y=500, w=100, h=100, cena=self.parede,
        drop={'ATP': self.usou_o_celular})
        self.movente = Elemento(img=RIBOSSOMA, cena=self.parede,
            style={"transition": "left 5s, top 5s"})
        self.movente1 = Elemento(img=RIBOSSOMA, y=100, cena=self.parede,
            style={"transition": "left 5s, top 5s"})
        self.maria = Elemento(img=MARIA, x=300, y=400, cena=self.parede, vai=self.usou_o_celular,
            style={"transition": "left 4s"})
        txt = ('De repente Maria vê uma bolinha se desprendo do complexo de golgi,'
            'ela encosta numa organela que está com uma placa escrito sem função,'
            'a bolinha vem na direção dessa organela e destrói a organela.')
        Texto(self.parede, txt, foi=self.mover).vai()
        self.acabou = 2
        # self.pergunta()
        
    def pegou_atp(self, ev=None):
        ATP = "https://i.imgur.com/k0Az1Ts.png"
        self.ATP = Elemento(img=ATP, tit="ATP", x=600, y=500, cena=self.parede, drag=True)
        self._parede_vai()
        
    def usou_o_celular(self, atp, ev=None):
        txt = ('Na pesquisa vc descobre que é o ribossoma. Ao chamar pelo nome eles vão embora')
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

    def mover(self, ev=None):
        self.movente.x=600
        self.movente.y=400
        self.movente1.x=600
        self.movente1.y=400
        self.maria.x=800
        
    def resposta(self, rep):
        if rep == "A":
            Texto(self.parede, "ganhou um ATP!").vai()
        else:
            Texto(self.parede, "Ops não acertou", foi=self.pergunta).vai()
            
            
        
Move()