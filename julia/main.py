# lorinda.julia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import inventario as inv

LILY = "https://i.imgur.com/UGyg7N2.png"
NENA = " https://i.imgur.com/SZ2Q8yp.png"
PEROLA = " https://i.imgur.com/CWuMMvW.png"
JACKSON = " https://i.imgur.com/XeNSqrz.png"
LEILA = " https://i.imgur.com/Vpw3hbY.png"
MATA = ""
ESCOLA = ""
TUCANO = "https://i.imgur.com/mS9ASAx.png"
CORDA =""
FACA =""
ISQUEIRO =""
KIT =""
MAPA =""
BUSSULA =""


class revista1():
    def __init__(self):
    self.escola=Cena(img=ESCOLA, Texto= "um grupo de amigos estudavam e se divertiam juntos e além disso,  tinham poderes especiais, entretanto por conta de uma pandemia, toda a população humana foi obrigada a viver em isolamento." 
                                        "Após dois anos de confinamento a vacina foi descoberta, após a vacinação em massa, os estudantes voltaram a se encontrar. Os amigos, que moravam mais perto da Mata Atlântica, na cidade de São Paulo"
                                        "começaram a perceber o sumiço de alguns animais, e se reuniram para desvendar esse mistério!")
    self.mata=Cena(img=MATA,Texto= ")
    self.lily=Elemento(img=LILY)
    self.nena=Elemento(img=NENA)
    self.perola=Elemento(img=PEROLA)
    self.jackson=Elemento(img=JACKSON)
    self.leila=Elemento(img=LEILA)
    self.lily.entra(self.escola)
    self.nena.entra(self.escola)
    self.perola.entra(self.escola)
    self.jackson.entra(self.escola)
    self.leila.entra(self.escola)
    
    self.escola.direita=self.mata
    self.mata.esquerda=self.escola
    self.nena.entra(self.mata)
    self.perola.entra(self.mata)
    self.jackson.entra(self.mata)
    
    self.escola.vai()
revista():
    
    