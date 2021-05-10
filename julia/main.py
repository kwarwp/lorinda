# lorinda.julia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import INVENTARIO as inv

from ruzwana.main import inventario

STYLE["width"]=800
STYLE["heigth"]="200px"

LILY = "https://i.imgur.com/UGyg7N2.png"
NENA = " https://i.imgur.com/SZ2Q8yp.png"
PEROLA = " https://i.imgur.com/CWuMMvW.png"
JACKSON = " https://i.imgur.com/XeNSqrz.png"
LEILA = " https://i.imgur.com/Vpw3hbY.png"
MATA = "https://i0.wp.com/www.sosma.org.br/wp-content/uploads/2020/08/imagem1-1.jpg"
ESCOLA = "https://i.imgur.com/4PaLeQW.jpg"
TUCANO = "https://i.imgur.com/mS9ASAx.png"
CORDA ="https://i.imgur.com/sD6vJLJ.png"
FACA =" https://i.imgur.com/T6W0qHH.png"
FOGO =" https://i.imgur.com/oH55GvU.png"
KIT =" https://i.imgur.com/ZVrPHcl.png"
MAPA ="https://i.imgur.com/dXllrys.png"
BUSSULA =" https://i.imgur.com/5OMt7f2.png"
PLAY= ""


class revista1():
    def __init__(self):
        self.escola=Cena(img=ESCOLA)

        
        Texto(self.escola,"Num futuro distante, um grupo de amigos estudavam e se divertiam juntos e além disso,  tinham poderes especiais, entretanto por conta de uma pandemia, toda a população humana foi obrigada a viver em isolamento."
                        "Após dois anos de confinamento a vacina foi descoberta, após a vacinação em massa,"
                        "os estudantes voltaram a se encontrar. Os amigos, que moravam mais perto da Mata Atlântica, na cidade de São Paulo,"
                        "começaram a perceber o sumiço de alguns animais, e se reuniram para desvendar esse mistério!" ).vai()
        self.escola.vai()
        self.lily=Elemento(img=LILY,x=220,y=400,w=100,h=200)
        self.nena=Elemento(img=NENA,x=120,y=400,w=100,h=200)
        self.perola=Elemento(img=PEROLA,x=320,y=400,w=100,h=200)
        self.jackson=Elemento(img=JACKSON,x=420,y=400,w=120,h=220)
        self.leila=Elemento(img=LEILA,x=520,y=400,w=100,h=200)
        self.lily.entra(self.escola)
        self.nena.entra(self.escola)
        self.perola.entra(self.escola)
        self.jackson.entra(self.escola)
        self.leila.entra(self.escola)
        self.escola.direita=Cena(vai=self.amem)
    def amem(self):
        self.mata=Cena(img=MATA)
        inventario(cena=self.mata)
        self.mata.vai()
        Texto(self.mata, "caracteristicas dos personagens , click para descobrir seu personagem").vai()
        self.mata.esquerda=self.escola
        self.escola.direita=self.mata
        self.mata.esquerda=self.escola
        self.nena.entra(self.mata)
        self.nena.tit="Olá eu sou a Nena, eu amo cuidar do planeta, sou organixa e monitoro tudo, por isso que eu trouxe uma bússula"
        self.perola.entra(self.mata)
        self.perola.tit="Olá,eu sou a Pérola,eu sou bastante forte e sou da equipe de resgate do meu bairro, por isso eu trouxe o kit de primeiros socorros"
        self.lily.entra(self.mata)
        self.lily.tit="Olá eu sou a Lily Raquel, eu sou bem otimista e desbravadora, por isso trouxe um facão"
        self.jackson.entra(self.mata)
        self.jackson.tit="Olá eu sou o Jackson,me colocaram como líder do grupo,pois sou muito corajoso e bom em defesa, estou levando um mapa e corda "
        self.leila.entra(self.mata)
        self.leila.tit=" olá eu sou a leila, sou bem quieta e discreta, me pediram para trazer o fogo"
        self.mata.entra=Elemento(vai=self.personagem)

        
       
        
       
        Texto(self.mata,).vai()
        self.leila.entra(self.mata)
        
    
    
        self.escola.vai()
revista1()
    
    