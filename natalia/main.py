# lorinda.natalia.main.py Leniaaaaah(não mexer)
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
from _spy.vitollino.main import Inventario as inv

STYLE["width"] = 800
STYLE["height"] = "600px"

ZEZINHO = "https://i.imgur.com/94lhgKo.png"
ROSALINDA = "https://i.imgur.com/qvuwHvs.png"
CASA = "https://www.tudoconstrucao.com/wp-content/uploads/2014/12/casa-de-praia-colorida-simples.jpg"

class gameg():

        casa = Cena( img = Casa)
        zezinho = Elemento( img = ZEZINHO)
        rosalinda = Elemento( img = ROSALINDA)
        zezinho.entra(casa)
        rosalinda.entra(casa)
        
        casa.vai()
gameg()        
        
        
