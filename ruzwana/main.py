# lorinda.ruzwana.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv 

STYLE.update(width=600, height="600px")
CORDA ="https://i.imgur.com/sD6vJLJ.png"
FACA =" https://i.imgur.com/T6W0qHH.png"
FOGO =" https://i.imgur.com/oH55GvU.png"
KIT =" https://i.imgur.com/ZVrPHcl.png"
MAPA ="https://i.imgur.com/dXllrys.png"
BUSSULA =" https://i.imgur.com/5OMt7f2.png"
MOCHILA ="https://i.imgur.com/N8eUQ2S.png"

class Item:
    def __init__(self, img, cena):
        self.cena = cena
        self.item= Elemento(img=img)
        self.item_inv= Elemento(img=img)
        # self.corda_inv.vai=self.mostra_corda
        inv.bota(self.item_inv)
        self.item_inv.vai = self.mostra_item
        self.item.vai = self.some_item
        
    def mostra_item(self, _=0):
        self.item.entra(self.cena)
        
    def some_item(self, _=0):
        self.item.x = -10000



class inventario:
    def __init__(self):
        inv.inicia()
        self.mochila=Cena(img=MOCHILA)
        self.mochila.vai()
        self.corda= Item(img=CORDA, cena=self.mochila)
        self.faca= Item(img=FACA, cena=self.mochila)
        self.fogo= Item(img=FOGO, cena=self.mochila)
        self.kit= Item(img=KIT, cena=self.mochila)
        self.mapa= Item(img=MAPA, cena=self.mochila)
        self.bussula= Item(img=BUSSULA, cena=self.mochila)
        
    def mostra_corda(self, _=0):
        self.corda.entra(self.mochila)
        
    def some_corda(self, _=0):
        self.corda.x = -10000

MOCHILA=inventario()

        