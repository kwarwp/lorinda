# lorinda.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Style, Sala
from _spy.vitollino.main import inventario as inv

GRUPO.ESTUDANTES=""
DRA.ROSALIND=""
EQUIPAMENTO="'
LABORATORIO="'

class celulas():
alunos= Elemento(GRUPO.ESTUDANTES)
rosalind= Elemento(DRA.ROSALIND)
maquina= Elemento(EQUIPAMENTO)
laboratorio= Cena(LABORATORIO)
    rosalind.entra(laboratorio)
    alunos.entra(laboratorio)
    laboratorio.vai()
    rosalind.fala="Olá, me chamo Rosalind. Hoje acompanharei vocês por este passeio pelas células!"
    fala.vai()
     