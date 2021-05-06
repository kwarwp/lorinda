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
class inventario:
     def __init__(self):
        self.mochila=Cena(img=MOCHILA)
        self.mochila.vai()
        self.corda= Elemento(img=CORDA)
        self.corda_inv= Elemento(img=CORDA)
        # self.corda_inv.vai=self.mostra_corda
        inv.bota(self.corda_inv)
        
        self.faca= Elemento(img=FACA)
        self.faca_inv= Elemento(img=FACA)
        # self.faca_inv.vai=self.mostra_faca
        
        self.fogo=Elemento(img=FOGO)
        self.fogo_inv=Elemento(img=FOGO)
        # self.fogo_inv=self.mostra_fogo
        
        self.kit=Elemento(img=KIT)
        self.kit_inv=Elemento(img=KIT)
        #self.kit_inv=self.mostra_kit
        
        self.mapa=Elemento(img=MAPA)
        self.mapa_inv=Elemento(img=MAPA)
        
        self.bussula=Elemento(img=ELEMENTO)
        self.bussula_inv=Elemento(img=ELEMENTO)

MOCHILA=inventario()

        