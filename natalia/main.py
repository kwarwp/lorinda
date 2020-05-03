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
BIBLIOTECA = "https://www.ifpb.edu.br/cajazeiras/noticias/2018/05/saiba-o-que-muda-com-a-implantacao-da-rede-integrada-de-bibliotecas-do-ifpb/regulamento-da-biblioteca-colegio-salesiano-dom-bosco-cidade-alta.png/@@images/image.png"
LIVRO = "https://img2.gratispng.com/20180505/hzw/kisspng-circle-black-and-white-clip-art-5aed68ee811080.5110845515255083345287.jpg"
SALA = "https://gizmodo.uol.com.br/wp-content/blogs.dir/8/files/2011/08/bias1-4e558ed-intro-thumb-640xauto-24932-1280x720.jpg"
QUADRADO = "https://w1.ezcdn.com.br/rebalcomercial/fotos/grande/3250fg1/prato-raso-porcelana-26-cm-branco-quadrado-americana-germer-gmr-068.jpg"
QUADRADO1 = "https://t2.uc.ltmcdn.com/pt/images/2/6/3/exercicio_para_calcular_a_diagonal_de_um_quadrado_24362_4_600.jpg"
CIRCULO = "https://png.pngtree.com/png-clipart/20190223/ourlarge/pngtree-circulo-ros%C3%AA-gold-png-image_693439.jpg"
DOIS TRAÇOS
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
        
        biblioteca = Cena (img = BIBLIOTECA)
        pergaminho.direta= biblioteca
        livro = Elemento (img = LIVRO)
        livro.entra(biblioteca)
        #o livro irá abrir para uma pagina secreta
        
        sala = Cena (img = SALA)
        quadrado = Elemento (img = QUADRADO)
        quadrado1 = Elemento (img = QUADRADO1)
        circulo = Elemento (img = CIRCULO)
        dois_t = Elemento (img = DOIS_T)
        #FAZER COM QUE O JOGADOR POSSA MONTAR ESSE HEREDROGRAMA
        #COMADOS DE :ORGANIZE E MONTE
        # Rapidamente após de montar tudo, apareceu alguns nomes ao lado de cada desenho :
        #quadrado em branco - indivíduo do sexo masculino; esfera em branco - indivíduo do sexo feminino;
        # traço - casamento; quadrado com risco no meio - indivíduo falecido 
        # DEPOIS DE MONTAR APARECEU A PALAVRA MAPA
        """APARECER UMA ABERTURA NA PAREDE"""
        # EM UMA ESCRIVANINHA APARECE UM MAPA 
        
        
        #APARECE UM OUTRO HEREDOGRAMA PARA ANALISAR
        #MONTAR UM HEREDROGRAMA COM AS INDICAÇOES ABAIXO
        
        
        
        
        casa.vai()
gameg()        
        
        
