# lorinda.julia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import inventario as inv

LILY = "https://i.imgur.com/UGyg7N2.png"
NENA = " https://i.imgur.com/SZ2Q8yp.png"
PEROLA = " https://i.imgur.com/CWuMMvW.png"
JACKSON = " https://i.imgur.com/XeNSqrz.png"
LEILA = " https://i.imgur.com/Vpw3hbY.png"
MATA = ""
ESCOLA = "https://png.pngtree.com/png-clipart/20190726/ourlarge/pngtree-cartoon-hand-drawn-yellow-school-building-illustration-png-image_1570994.jpg"
TUCANO = "https://i.imgur.com/mS9ASAx.png"
CORDA ="https://i.imgur.com/sD6vJLJ.png"
FACA =" https://i.imgur.com/T6W0qHH.png"
FOGO =" https://i.imgur.com/oH55GvU.png"
KIT =" https://i.imgur.com/ZVrPHcl.png"
MAPA ="https://i.imgur.com/dXllrys.png"
BUSSULA =" https://i.imgur.com/5OMt7f2.png"


class revista1():
    def __init__(self):
        self.escola=Cena(img=ESCOLA)
        Texto(self.escola, "um grupo de amigos estudavam e se divertiam juntos e além disso,  tinham poderes especiais, entretanto por conta de uma pandemia, toda a população humana foi obrigada a viver em isolamento." 
                                        "Após dois anos de confinamento a vacina foi descoberta, após a vacinação em massa, os estudantes voltaram a se encontrar. Os amigos, que moravam mais perto da Mata Atlântica, na cidade de São Paulo"
                                        "começaram a perceber o sumiço de alguns animais, e se reuniram para desvendar esse mistério!").vai()
        self.mata=Cena(img=MATA)
        Texto(self.mata, "caracteristicas dos personagens , click para descobrir seu personagem").vai()
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
        self.nena.entra(self.mata, tit="Olá eu sou a Nena, eu amo cuidar do planeta, sou organixa e monitoro tudo, por isso que eu trouxe uma bússula")
        self.perola.entra(self.mata, tit= "Olá,eu sou a Pérola,eu sou bastante forte e sou da equipe de resgate do meu bairro, por isso eu trouxe o kit de primeiros socorros)
        self.lily.entra(self.mata, tit="Olá eu sou a Lily Raquel, eu sou bem otimista e desbravadora, por isso trouxe um facão")
        self.jackson.entra(self.mata, tit ="Olá eu sou o Jackson,me colocaram como líder do grupo,pois ")
        self.leila.entra(self.mata)
    
        self.escola.vai()
revista():
    
    