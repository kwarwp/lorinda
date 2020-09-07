# lorinda.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"
GRUPO_ESTUDANTES="https://static.lenovo.com/br/landings/estudantes/assets/img/lenovo-educational-banner.png"
DRA_ROSALIND="https://blog.ipog.edu.br/wp-content/uploads/2017/10/m%C3%A9dico.jpg"
EQUIPAMENTO="https://comps.canstockphoto.com.br/equipamento-m%C3%A9dico-desenho-vetor-eps_csp55846331.jpg"
LABORATORIO="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/InvestigadoresUR.JPG/350px-InvestigadoresUR.JPG"

class celulas:
    alunos= Elemento(GRUPO_ESTUDANTES,  x=460, y=250, w=150, h=80)
    rosalind= Elemento(DRA_ROSALIND,  x=400, y=250, w=150, h=80)
    maquina= Elemento(EQUIPAMENTO,  x=360, y=250, w=150, h=80)
    laboratorio= Cena(LABORATORIO)
    rosalind.entra(laboratorio,)
    alunos.entra(laboratorio)
    laboratorio.vai()
    rosalind.fala="Olá, me chamo Rosalind. Hoje acompanharei vocês por este passeio pelas células!"
    fala.vai()
celulas()   