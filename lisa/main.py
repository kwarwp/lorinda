# lorinda.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE, Texto
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"
GRUPO_ESTUDANTES="https://static.lenovo.com/br/landings/estudantes/assets/img/lenovo-educational-banner.png"
DRA_ROSALIND="https://blog.ipog.edu.br/wp-content/uploads/2017/10/m%C3%A9dico.jpg"
EQUIPAMENTO="https://comps.canstockphoto.com.br/equipamento-m%C3%A9dico-desenho-vetor-eps_csp55846331.jpg"
LABORATORIO="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/InvestigadoresUR.JPG/350px-InvestigadoresUR.JPG"
#colocar imagens das células
class celulas():
    alunos= Elemento(GRUPO_ESTUDANTES,  x=460, y=250, w=150, h=80)
    rosalind= Elemento(DRA_ROSALIND,  x=400, y=250, w=150, h=80, Texto " Aqui é um castelo da ciênca onde vcs poderam aprender, descobrir e inventar")
    maquina= Elemento(EQUIPAMENTO,  x=360, y=250, w=150, h=80)
    laboratorio= Cena(LABORATORIO, Texto " Bem vindo ao laborátorio de ciências, aqui aprendemos e estudamos células")
    rosalind.entra(laboratorio,)
    alunos.entra(laboratorio)
    laboratorio.vai()
    rosalind.fala="Olá, me chamo Rosalind. Hoje acompanharei vocês por este passeio pelas células!"# ver se não vai chocar com o que eu colequei nesse personagem acima 
    fala.vai()
celulas()

class Fase1():
laboratorio= Cena(img =  LABORATORIO)
procarionte= Elemento(img= PROCARIONTE, Texto= " oi eu sou uma célula procarionte,e me chama assim pq eu tenho apenas uma célula no meu corpo")
eucarionte= Elemento(img= EUCARIONTE, Texto= "eu sou uma célula procarionte e sou igual a vcs humanos pq meu corpo é cheio de células")
trypanosoma_cruzi= Elemento(img=TRYPANOSOMA_CRUZI, Texto = "a galera não gosta muito de mim pq dizem que eu sou parasita e que causa uma doença no coração, mas é que o coração grande é tão quentinho"
)
neuronio=Elemento(img= NEURONIO, Texto ="eus ou bem complicado, pois eu fico na cabeça e passo informação pelo corpo, imagina como eu devo ser feito")
bacteria = Elemento(img= BACTERIA, Texto ="olá eu sou uma pessoa simples, igual arroz pois combino com tudo e posso estar em qualquer lugar, sempre tem espaço para mim")
espermatozoide= Elemento(img=  ESPERMATOZOIDE, Texto = "eu sou quem dá a origem dos humanos, então imagina como devo ser dificil e complexo me estudar") 
hemacia= Elemento(img= HEMACIA, Texto= "eu sou o transporte da galera, carrego muita coisa, imagina como sou")
elodea= Elemento(img= ELODEA, Texto ="eu vivo na agua e sou muito importante para a manutenção do ambiente marinho, posso ser encoderijo , comida ou o2")
celula_calciforme= Elemento(img= CELULA_CALCIFORME,Texto = "eu fico no instestino delgado eu tenho diversas funções, uma dela pe revestir com muco para proteger onde estou")
npc= Elemento(img= NPC,Texto = "você precisa descobrir quem é procarionte para a próxima fase")
"""resposta certa é a bactéria"""
laboratorio.vai()
Fase1()

class Fase2():



