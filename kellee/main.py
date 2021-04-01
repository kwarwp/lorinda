# lorinda.kellee.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from _spy.vitollino.main import Inventario as inv 


MARIA = ""
ROSALINDA = "https://imgur.com/0Dv7w29"
LABORATORIO = ""

class fase3():
    def __init__(self):
    self.laboratorio=Cena(img=LABORATORIO)
    self.maria=Elemento(img=MARIA, tit="oi,  Dr. Rosalinda sou sua fã, li todos os seus livros e seu artigo sobre "Direcionamento de Proteínas", ou seja, como as proteínas percorrem toda a célula")
    self.rosalinda=Elemento(img=ROSALINDA, tit="as proteínas são muito importantes, para a nossa saúde e beleza! Precismos estuda-las, para nos manter saudáveis, fortes e bonitas. ")
    self.maria.entra(self.laboratorio)
    self.rosalinda.entra(self.laboratorio)