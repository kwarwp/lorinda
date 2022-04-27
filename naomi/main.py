# lorinda.naomi.main.py
from _spy.vitollino.main import Cena, Elemento,Texto, STYLE,JOGO
from courtney.main import MOCHILA
from tracy.main import Personagem
from anastasia.main import Swap
STYLE.update(width=1000, height="600px")

PAREDE = "https://i.imgur.com/ZAoCT4o.png"
SEMFUNCAO = "https://i.imgur.com/u7zMLPW.png"
GOLGI = "https://i.imgur.com/PUbco5w.png"
class Fase6:
    def __init__(self,*_):
        STYLE.update(width=1000, height="600px")

        def pegou_atp(ev=None):
            ATP = "https://i.imgur.com/k0Az1Ts.png"
            self.ATP = Elemento(img=ATP, tit="ATP", x=600, y=500, cena=self.parede, drag=True)
        NPC = "https://imgur.com/VcPXMYC.png"
        RIBOSSOMA = "https://i.imgur.com/Tf5yrKb.png"
        LISOSSOMA = "https://i.imgur.com/g0OplxP.png"
        MARIA = "https://i.imgur.com/4yrnNgS.png"
        CELULAR = "https://www.neoenergia.com/pt-br/te-interessa/meio-ambiente/PublishingImages/fotos/covid-virus-bacteria.png"
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
        self.movente = Elemento(img=GOLGI, w=260, h=260, cena=self.parede,
            style={"transition": "left 5s, top 5s"})
        self.movente = Elemento(img=LISOSSOMA, x=30, y=180, w=60, h=60, cena=self.parede,
            style={"transition": "left 5s, top 5s"})
        self.movente.elt.ontransitionend = self.persegue_maria
        self.movente1 = Elemento(img=LISOSSOMA, w=60, h=60, x=180, y=140, cena=self.parede,
            style={"transition": "left 5s, top 5s"})
        self.organela = Elemento(img=RIBOSSOMA, x=400, y=400, w=60, h=60, cena=self.parede,
            style={"transition": "opacity 2s"})
        self.placa_organela = Elemento(img=SEMFUNCAO, x=375, y=380, w=80, h=30, cena=self.parede,
            style={"transition": "opacity 2s"})
        self.maria = Elemento(img=MARIA, x=600, y=390,w=150,h=150, cena=self.parede, # vai=self.usou_o_celular,
            style={"transition": "left 4s"})
        self.maria.elt.ontransitionend = self.encosta_maria
        txt0 = ('De repente Maria vê uma bolinha se desprendo do complexo de golgi,'
            'ela encosta numa organela que está com uma placa escrito sem função,'
            'a bolinha vem na direção dessa organela e destrói a organela.')
        txt = ('Maria vê uma organela que está com uma placa escrito sem função'
            ' e vai ver do que se trata.')
        Texto(self.parede, txt, foi=self.move_maria).vai()
        self.acabou = 2
        # self.pergunta()
        
    def pegou_atp(self, ev=None):
        ATP = "https://i.imgur.com/k0Az1Ts.png"
        self.ATP = Elemento(img=ATP, tit="ATP", x=600, y=500, cena=self.parede, drag=True)
        self._parede_vai()
        
    def usou_o_celular(self, atp, ev=None):
        txt = ('Eles são os lisossomos. São estruturas arredondadas e ricas em enzimas digestivas.'
        ' Essas enzimas são produzidas pelo retículo endoplasmático rugoso e depois enviadas para o complexo golgiense,'
        ' onde são armazenadas em pequenas vesículas. Essas vesículas se soltam e originam os lisossomos.'
        ' Essa organela é fundamental nos processos de fagocitose e pinocitose, em que a célula captura partículas através de pseudópodes para sua nutrição ou para destruir possíveis agentes' 
        ' nocivos')
        Texto(self.parede, txt, foi=self.vai_embora).vai()
        self.ATP.x = -1000
        
    def vai_embora(self, ev=None):
        self.movente.elt.ontransitionend = Fase7
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
        conselho = "Pegue um ATP da mochila e jogue nos vírus e bactérias."
        self.multi = Texto(self.parede, conselho).vai()

    def move_maria(self, ev=None):
        self.maria.x=400

    def encosta_maria(self, ev=None):
        txt = ('Ela encosta nessa organela e '
        'de repente vê umas bolinhas se desprendendo do complexo de Golgi.'
            ' As bolinhas vem na direção da organela e a destrói. Elas atacam Maria, que corre.')
        Texto(self.parede, txt, foi=self.mover).vai() if self.matou_organela else None
        # self.matou_organela = False

    def pede_socorro(self, ev=None):
        txt = ('Socorro NPC!')
        Texto(self.parede, txt).vai()

    def foge_maria(self, ev=None):
        self.maria.x=800


    def persegue_maria(self, ev=None):
        self._persegue_maria() if self.matou_organela else None
        self.matou_organela = False


    def _persegue_maria(self, ev=None):
        self.maria.elt.ontransitionend = self.pede_socorro
        self.placa_organela.o = 0
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
            
GLICOSE = "https://i.imgur.com/vgrC2fM.png"
RIBOSSOMA = "https://i.imgur.com/Tf5yrKb.png"
MITOCONDRIA = "https://i.imgur.com/YpXXhJF.png"
MARIA = "https://i.imgur.com/4yrnNgS.png"
ESCURO = "https://i.imgur.com/cQogon6.jpg"
CELULA = "https://i.imgur.com/ujAF00x.jpg"
CICLONE = "https://i.imgur.com/BC6X7ho.gif"

class Fase7():
    def __init__(self, _=0):
        def faz_luz(_, ev=None):
            self.escuro.x = -10000
            self.mitocondria.o = 1
            self.glicose.x = -10000
            self.entra_redemoinho()
        self.celula = Cena(CELULA)
        self.celula.vai()
        self.escuro = Elemento(ESCURO, x=0, y=0, w=1000, h=600, o=0.92, cena=self.celula)
        self.mitocondria = Elemento(MITOCONDRIA, x=20, y=40, w=950, h=550, o=0.1, cena=self.celula,
            drop = {"glicose": faz_luz})
        self.glicose = Elemento(GLICOSE, x=0, y=100, tit = "glicose", drag = True,
            w=100, h=100)
        afala = "Ribossomo: Porque perdi minha outra parte e preciso encontrá-la. Eu preciso produzir proteínas"
        self.ribossoma = Personagem(RIBOSSOMA, x=200, y=750, w=90, h=90, afala=afala,
            responde=self.ribossomo_fala)
        afala = "Maria: Ribossomo, por que você está triste?"
        self.maria=Personagem(img=MARIA, x=500, y=150, w=200, h=300, afala=afala, responde=self.ribossoma.fala)
        self.glicose.entra(self.celula)
        self.ribossoma.entra(self.celula)
        self.maria.entra(self.celula)
        self.maria.fala()
        
    def ribossomo_fala(self, _=0):
        afala = "Você está em cima de uma mitocôndria. Acople a molécula de glicose para liberar energia e acender a luz, assim o ribossomo poderá encontrar sua outra parte."
        self.glicose_fake = Personagem(GLICOSE, x=-10000, y=100,w=100, h=100, afala=afala)
        afala = "Ribossomo: Maria, olhe onde você está..."
        self.ribossoma = Personagem(RIBOSSOMA, x=300, y=200, w=90, h=90, afala=afala,
            responde=self.glicose_fake.fala)
        afala = "Maria: Mas está tudo escuro, como vamos achar?"
        # self.maria=Personagem(img=MARIA, x=400, y=200, w=100, h=200, afala=afala, responde=self.ribossoma.fala)
        self.maria.afala = afala
        self.maria.responde = self.ribossoma.fala
        self.glicose_fake.entra(self.celula)
        self.glicose.entra(self.celula)
        self.ribossoma.entra(self.celula)
        self.maria.entra(self.celula)
        self.maria.fala()
        
    def anda_redemoinho(self, _=0):
        self.redemoinho.x = 1500
        self.maria.x = 1500
        self.maria_double.x = 1500
        self.maria_double.elt.style.transform = "rotate(200deg)"
  
    def main(self,_=0):
        self.parede=cena = JOGO.c('https://i.imgur.com/ujAF00x.jpg').vai()
        t = JOGO.n(cena, 'É isto! A Parede Celular!',foi=self.maria_sai)
        Swap(JOGO, PAREDE, cena, w=700,h=200,x=50,y=150,dw=7,dh=2, venceu=t) 
    
    def maria_sai(self):
        self.maria.entra(self.parede)
        #self.parede.vai()
        self.maria.responde=self.outro_redemoinho
        self.maria.fala()
         
    def outro_redemoinho(self):
        afala = 'De novo, este redemoinho louco?'
        self.redemoinho = Elemento(CICLONE, x=0, y=0, w=600, h=600, o=0.8, cena=self.parede,
        style= {"transition": "left 6s"})
        self.redemoinho.elt.ontransitionend = Fase11
        self.redemoinho.entra(self.parede)
        self.maria.afala = afala
        self.maria.responde = self.anda_redemoinho
        self.maria_double=Elemento(img=MARIA, x=500, y=300, w=200, h=300, cena=self.parede,
        style= {"transition": "left 6s, transform 1s"})
        self.redemoinho.entra(self.parede)
        self.maria.entra(self.parede)
        self.maria.fala()
    def entra_redemoinho(self, _=0):
        #from amanda.main import main
        afala = "Maria: eu finalmente consegui sair desse lugar"
        self.redemoinho = Elemento(CICLONE, x=0, y=0, w=600, h=600, o=0.8, cena=self.celula,
        style= {"transition": "left 6s"})
        self.redemoinho.elt.ontransitionend = self.main
        self.maria.afala = afala
        self.maria.responde = self.anda_redemoinho
        #self.maria.x = 600
        self.maria_double=Elemento(img=MARIA, x=500, y=300, w=200, h=300, cena=self.celula,
        style= {"transition": "left 6s, transform 1s"})
        self.redemoinho.entra(self.celula)
        self.maria.entra(self.celula)
        self.maria.fala()
   
    def ribossomofala(self):
        self.mitocondria=Cena(img=MITOCONDRIA)
        self.mitocondria.vai()
        self.ribossomo=Personagem(img=RIBOSSOMA,x=0, afala="No caminho eu te explico...")
        self.maria=Personagem(img=MARIA, afala="Mas está tudo escuro, como vamos achar?",responde=self.ribossomo)
        self.maria.entra(self.mitocondria)
        self.ribossomo.entra(self.mitocondria)
       
        self.maria.fala()
        self.ribossomo.fala()
#if __name__ == "__main__":            
    #Fase6()  
 
LABORATORIO="https://i.imgur.com/g3wt0Vb.jpg"
CICLONE = "https://i.imgur.com/BC6X7ho.gif"
class Fase11():
    def __init__(self, *_):
        self.laboratorio=Cena(img=LABORATORIO)
        afala="ufaa, graças a vocês consegui sair citanópolis  "
        self.maria=Personagem(img= MARIA,afala=afala,responde=self.the_end )
        self.maria.entra(self.laboratorio)
        self.laboratorio.vai()
        self.maria.fala()
        

        
        
    def the_end(self, _=0):
        #from amanda.main import main
        afala = "Maria: Ufa! Eu finalmente consegui sair desse lugar. Sua missão agora é ensinar aos outros, tudo o que aprendeu sobre organelas celulares."
        end="https://i.imgur.com/PGl5zCl.jpg"
        self.the_end = Elemento(end, x=0, y=0, w=600, h=600, o=0.8, cena=self.laboratorio)
        
        
if __name__ == "__main__": 
    Fase6()
    
    #Move()