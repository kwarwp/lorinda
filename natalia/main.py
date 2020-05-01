# lorinda.natalia.main.py Leniaaaaah(não mexer)
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
from _spy.vitollino.main import Inventario as inv

STYLE["width"] = 800
STYLE["height"] = "600px"

ZEZINHO = "https://i.imgur.com/94lhgKo.png"
ROSALINDA = "https://i.imgur.com/qvuwHvs.png"
CASA = "https://www.tudoconstrucao.com/wp-content/uploads/2014/12/casa-de-praia-colorida-simples.jpg"

class gameg():

        casa = Cena( img = CASA)
        zezinho = Elemento( img = ZEZINHO, tit= "bOA TARDE, SOU ZEZINHO E VIM PARA A ENTREVISTA" ,
        style=dict (left=200, top=350, width=200, height="200px",))
        rosalinda = Elemento( img = ROSALINDA, tit= "OLÁ, SOU ROSALINDA,vAMOS COMEÇAR A ENTREVISTA?" ,
        style=dict (left=400, top=350, width=300, height="200px",))
        zezinho.entra(casa)
        rosalinda.entra(casa)
        
        casa.vai()
gameg()        
        
        
