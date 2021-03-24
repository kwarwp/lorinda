# lorinda.libby.main.
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import inventario as inv 
CELULA_1 = "https://img.pebmed.com.br/wp-content/uploads/2018/09/26163836/bacteria-3662695_640-min.jpg"
CELULA_2 = "https://static.todamateria.com.br/upload/tc/ru/t_cruzi_1.jpg"
CELULA_3 = "https://img2.gratispng.com/20180602/bga/kisspng-plant-cell-cl-lula-eucariota-cl-lula-animal-animal-cell-5b1365ea94c884.3552609815279979306094.jpg"
CELULA_4 = "https://png.pngtree.com/png-vector/20191007/ourmid/pngtree-sperm-cells-icon-flat-style-png-image_1796531.jpg" 
CELULA_5 = "https://www.infoescola.com/wp-content/uploads/2020/01/celula-caliciforme-1029137758.jpg"
CELULA_6 = "https://static.biologianet.com/conteudo/images/os-neuronios-sao-constituidos-basicamente-por-um-corpo-celular-dendritos-axonio-5b3b696bc348e.jpg"
MOEDAS = "https://thumbs.dreamstime.com/z/moeda-do-jogo-com-folha-trevo-rela%C3%A7%C3%A3o-ouro-vetor-estilo-dos-desenhos-animados-isolado-114681804.jpg"
CICLONE = "https://static.todamateria.com.br/upload/55/65/556506fa96eca-ciclone.jpg"
MEMBRANA = "https://static.biologianet.com/2020/02/membrana-plasmatica.jpg"
NPC = ""
class fase2():
    def __init__(self):
    self.npc= Elemento(img= NPC)
    self.ciclone= Elemento(img= CICLONE)
    self.celula_1= Elemento(img= CELULA_1)
    self.celula_2= Elemento(img= CELULA_2)
    self.celula_3= Elemento(img= CELULA_3)
    self.celula_4= Elemento(img= CELULA_4)
    self.celula_5= Elemento(img= CELULA_5)
    self.celula_6= Elemento(img= CELULA_6)
    self.membrana= Cena(img= MEMBRANA)
    self.celula_1.entra(self.membrana)
    self.celula_2.entra(self.membrana)
    self.celula_3.entra(self.membrana)
    self.celula_4.entra(self.membrana)
    self.celula_5.entra(self.membrana)
    self.celula_6.entra(self.membrana)
    self.npc.entra(self.celula,Tit = "Observe atentamente essas imagens e coloque as letras correspondentes."
    "Cada imagem terá apenas três letras, arraste para a área correspondente da célula")    #não temos ainda a imagem da célula
    self.npc.entra(self.membrana,Tit = "Você precisa de moedas de ATP para sair dessa dimenção, para isso, precisamos excluir a célula procarionte")
    
    
    