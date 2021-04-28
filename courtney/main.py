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
        inv.bota(self.mochila_inv)
        
    def mostra_mochila(self, _=0):
        self.cena_anterior = inv.cena
        self.mochila.vai()
        
    def fecha_mochila(self, _=0):
        self.cena_anterior.vai()
        
    def calcula_moeda(self):
        moedas = len(self.moedas)
        return dict(x=(moedas % 10) * 60, y=(moedas // 10) * 60)
        
    def ganha_atp(self):
        xy = self.calcula_moeda()
        Elemento(self.ATP, cena=self.mochila, w=50, h=50, **xy)
        self.moedas.append(self.ATP)
        
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