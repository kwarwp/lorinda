# lorinda.natalia.main.py Leniaaaaah(não mexer)
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
from _spy.vitollino.main import Inventario as inv

STYLE["width"] = 800
STYLE["height"] = "600px"

ZEZINHO = "https://i.imgur.com/94lhgKo.png"
ROSALINDA = "https://i.imgur.com/qvuwHvs.png"
CASA = "https://www.tudoconstrucao.com/wp-content/uploads/2014/12/casa-de-praia-colorida-simples.jpg"
QUADROS = "https://staticcdns3.bidu.com.br/jamal/uploads/2016/11/06164925/3b1.jpg"
QUADROS1 = "https://staticcdns3.bidu.com.br/jamal/uploads/2016/11/06164925/3b1.jpg"
TOUR = "https://s2.glbimg.com/zYpJy77kEUuJR3sRh3kiTdzZ4Bk=/620x455/e.glbimg.com/og/ed/f/original/2014/02/27/cj688paisagismo130.jpg"
COFRE = "https://a-static.mlcdn.com.br/618x463/cofre-concretado-com-boca-de-lobo-ct30bl-30x36x26-segredo-mecanico-cofresventura/cofresventura/5030/aeae22f74a1dac4ebacb09409c0875bd.jpg"
HEREDOGRAMA = "https://pt-static.z-dn.net/files/d71/7bf7ab4461bea11a7a1c561ed2584a48.png"
PERGAMIHO = "https://i.pinimg.com/originals/df/6c/76/df6c765f7019656350531c4a4eff5e11.png"

class gameg():

        casa = Cena( img = CASA)
        zezinho = Elemento( img = ZEZINHO, tit= "bOA TARDE, SOU ZEZINHO E VIM PARA A ENTREVISTA" ,
        style=dict (left=200, top=350, width=200, height="200px",))
        rosalinda = Elemento( img = ROSALINDA, tit= "OLÁ, SOU ROSALINDA,vAMOS COMEÇAR A ENTREVISTA?" ,
        style=dict (left=400, top=350, width=300, height="200px",))
        zezinho.entra(casa)
        rosalinda.entra(casa)
        
        quadros = Cena( img = QUADROS)
        casa.direita=quadros
        quadros.esquerda=casa
        zezinho.entra(quadros)#colocar mesnagem confusa de zezinho em relação aos quadros
        rosalinda.entra(quadros)
        
        tour= Cena( img = TOUR)
        quadros.direita=tour
        tour.esquerda=quadros
        zezinho.entra(tour)#zezinha volta para ver o quadros pois ficou encafifado
        rosalinda.entra(tour)#recebe um telfonema e diz que zezinho pode ficar a vontade, mas ela tera que se ausentar
        
        quadros1= Cena( img = QUADROS1)
        tour.direita=quadros1
        zezinho.entra(quadros1)#zezinho ajeita o quadro e quando irá arrumar outro quadro e ele está muito pesado, ao tirar da parde encontra um cofre
        cofre = Cena(img = COFRE)# ESSE COFRE PRECISA TER UM HEREDPGRAMA PARA ABRIR
        #NAO ENTENDI A GAVETA COM LETRAS
        heredograma= Elemento( img = HEREDOGRAMA)# ESTAR COMO UM QUADRO
        #LEMBROU DE UMA AULA NA FIO CRUZ
        #OLHOU NOVAMENTO NO COFRE E TINHA UMAS LETRAS EMBARALHAS
        #ABRIU O COFRE E PEGOU UM PAPEL
        
        quadros1.direita=pergaminho
        pergaminho = Cena (img = PERGAMINHO)
        pergaminho.esquerda=quadros
        zezinho.entra(pergaminho)
        #informações sobre o heredograma
        
        
        
        
        
        
        casa.vai()
gameg()        
        
        
