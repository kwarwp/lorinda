# lorinda.courtney.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv 

STYLE.update(width=600, height="600px")

class Mochila:
    MOCHILA = "https://i.imgur.com/N8eUQ2S.png"
    ATP = "https://i.imgur.com/k0Az1Ts.png"
    ADP = "https://i.imgur.com/XhUguZt.png"
    VOLTA = "https://i.imgur.com/PL5FFhk.png"
    def __init__(self):
        self.mochila = Cena(self.MOCHILA)
        self.mochila.vai()
        #self.atp = Elemento(self.ATP, cena=self.mochila)
        #self.adp = Elemento(self.ADP, cena=self.mochila, x=90)
        self.moedas = []
        self.mochila_inv = Elemento(self.MOCHILA)
        self.mochila_inv.vai = self.mostra_mochila
        self.mochila_fecha = Elemento(self.VOLTA, cena=self.mochila, x=0, y=550, w=600, h=50)
        self.mochila_fecha.vai = self.fecha_mochila
        self.pega_atp = lambda *_: None
        inv.bota(self.mochila_inv)
        
    def mostra_mochila(self, _=0, pega_atp=lambda *_: None):
        self.cena_anterior = inv.cena
        self.pega_atp = pega_atp
        self.mochila.vai()
        
    def fecha_mochila(self, _=0):
        self.cena_anterior.vai()
        
    def esvazia_mochila(self, _=0):
        inv.inicia()
        inv.bota(self.mochila_inv)
        
    def quando_pega(self, pega_atp=lambda *_: None, _=0):
        self.pega_atp = pega_atp
        
    def calcula_moeda(self):
        moedas = len(self.moedas)
        return dict(x=(moedas % 10) * 60, y=(moedas // 10) * 60)
        
    def ganha_atp(self):
        xy = self.calcula_moeda()
        Elemento(self.ATP, cena=self.mochila, w=50, h=50, vai=self._pega_atp, **xy)
        self.moedas.append(self.ATP)
        
    def _pega_atp(self, _=0):
        self.cena_anterior.vai()
        self.pega_atp()
        
    def ganha_adp(self):
        xy = self.calcula_moeda()
        Elemento(self.ADP, cena=self.mochila, w=50, h=50, **xy)
        self.moedas.append(self.ADP)
        

MOCHILA = Mochila()
if __name__ == "__main__":
    m = Mochila()
    m.ganha_adp()
    m.ganha_adp()
    m.ganha_adp()
    m.ganha_adp()
    m.ganha_adp()
    m.ganha_adp()
    m.ganha_adp()
    m.ganha_atp()
    m.ganha_atp()
    m.ganha_atp()
    m.ganha_atp()
    m.ganha_adp()