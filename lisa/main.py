# lorinda.lisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"
GRUPO_ESTUDANTES="https://static.lenovo.com/br/landings/estudantes/assets/img/lenovo-educational-banner.png"
DRA_ROSALIND="https://blog.ipog.edu.br/wp-content/uploads/2017/10/m%C3%A9dico.jpg"
EQUIPAMENTO="https://comps.canstockphoto.com.br/equipamento-m%C3%A9dico-desenho-vetor-eps_csp55846331.jpg"
LABORATORIO="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/InvestigadoresUR.JPG/350px-InvestigadoresUR.JPG"
RUA= "https://www.marica.rj.gov.br/wp-content/uploads/2019/01/2019_01_22_Pavimentacao_Rua_Farol_Ponta_Negra-CLARILDO-5.jpg"
ESTRANHA= "https://images-na.ssl-images-amazon.com/images/I/51orI6c%2BfJL._AC_SX425_.jpg"
CASA= "https://img.freepik.com/vetores-gratis/uma-casa-de-dois-andares_1308-16176.jpg?size=626&ext=jpg"
PACOTE = "https://images.vexels.com/media/users/3/146255/isolated/lists/9eacf7cedc0893ff8192c1db0e5c6326-caixa-fechada-com-sinais-de-pacote.png"
RUA2 = "https://s2.glbimg.com/40lwYrB5jZXWB8XJpY4dIFFE94M=/0x0:5546x3927/1008x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2020/J/W/98WwrvRgqpmm8AUAzC2g/jb-hoje-marquinhos-.jpg"
MARIA = "https://s2.glbimg.com/ixg1qdFwUhzjnAlwXBnv0PP3h-s=/620x520/top/e.glbimg.com/og/ed/f/original/2020/07/30/grazi_1.jpeg"
FIOCRUZ = "https://s2.glbimg.com/NIPby_eu2LH5UTy-uSA5Cp_jJJU=/0x0:1280x720/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/i/X/S95he4TOWvMfdXBFABFw/fiocruz.jpg"
CHEFE = "https://s2.glbimg.com/zoU5JtDc323S8zHeujtX5YIXKP8=/620x430/e.glbimg.com/og/ed/f/original/2020/03/14/gettyimages-1130312146.jpg"
CORREDOR = "https://dicionario.priberam.org/images/dplp/corredor.jpg"
LAMINA = "https://www.splab.com.br/imagens/informacoes/lamina-vidro-escavada-02.jpg"
LABORATORIO ="https://www.unimedjaboticabal.coop.br/wp-content/uploads/2019/07/unimed-jaboticabal-laboratorio-750x500.jpg"
#colocar imagens da class apresentação 
class apresentacao():
    def __init__(self):
        casa = Cena(img = CASA)#maria vai para fio cruz
        maria= Elemento(img= MARIA, x=460, y=250, w=150, h=80)
        rua= Cena(img= RUA)
        estranha= Elemento(img= ESTRANHA, texto= "Guarde e proteja esse pacote com sua própria vida")
        pacote=Elemento(img=PACOTE)
        casa.direta=rua
        rua.esquerda=casa
        #maria.entra(rua)
        #coloquei .vai() em alguns
        #maria.entra(rua) 
        rua2=Cena(img= RUA2)
        rua.direita= rua2
        rua2.esquerda=rua
        #maria.entra(rua2)
        estranha.entra(rua2)#entrega o pacote e some
        pacote=Elemento(img= PACOTE)
        fiocruz= Cena(img=FIOCRUZ)
        pacote.entra(rua2)
        rua2.direta=fiocruz
        fiocruz.esquerda=rua2
        chefe=Elemento(img=CHEFE)
        laboratorio= Cena(img= LABORATORIO)
        #microscopio = Elemento(img = MICROSCOPIO)
        # cartaz= Elemento(img= CARTAZ)
        #chefe.entra(fiocruz)
        #será que assim vai? colocar separado? mas se colocar assim os dois textos vão aparecer
        #juntos, não
        #maria abre o pacote e encontra uma lâmina
        lamina=Elemento(img= LAMINA)
        #maria vai para um laboratório, mas antes passa por um corredor
        corredor= Cena(img= CORREDOR)
        fiocruz.direita= corredor
        corredor.esquerda=fiocruz
        
   
    def entrou_maria(*_):
        maria.entrou(casa)
        maria.vai= Texto(casa," olá me chamo Maria e amo estudar biologia e lutar pelos direitos das mulheres")
    def entrou_rua(*_):
        maria.entrou(rua)
        maria.vai= Texto(rua, "estou indo para FIOCRUZ, acho que vou conseguir um estágio lá, uip")
    def entrou_rua2(*_):
        maria.entra(rua2)
        maria.vai= Texto(rua2, "parece uma pessoa estranha, não quero aceitar nada dela")
    def entra_fiocruz(*_):
        chefe.entra(fiocruz)
        chefe.vai= Texto(fiocruz, "Boa tarde Maria, temos um tempo antes da entrevista, fique a vontade...se quiser pode explorar os laboatórios para estudar")
        maria.entra(fiocruz)
        maria.vai=Texto(fiocruz,"nossa um pedaço de vidro, tenho um tempo antes da entrevista do estagio a moça disse que eu poderia ficar nos laboratórios estudando")
    
    def entrou_laboratorio(*_):
        maria.entra(laboratorio)
        maria.vai= Texto(laboratorio, "aqui tem uns equipamentos para ver esse vidro, escolha qual vc acha melhor")
    def entrou_lamina(*_):
        lamina.entra(laboratorio)
        lamina.vai= Texto(laboratorio,  "nossa um pedaço de vidro, tenho um tempo antes da entrevista do estagio a moça disse que eu poderia ficar nos laboratórios estudando")
    def entrou_microscopio(*_):
        microscopio.entra(laboratorio)
        microscopio.vai= Texto(laboratorio, " olá, eu sou utilizado para ver coisas que o olho humano não ve ")
    """ colocar outros equipamentos de laboratório"""
    def entrou_cartaz(*_):
        cartaz,entra(laboratorio)
        cartaz.vai=Texto(laboratorio, "para se usar o microscópio faça isso...")
    
    """arrastar e colocar a lâmina no microscópio e então aparece um um ciclone que a leva para dentro da célula, 
    ela grita e pergunta onde estou""" 
    

apresentacao()
print (apresentacao)

#class Fase1():
#laboratorio= Cena(img =  LABORATORIO)
#procarionte= Elemento(img= PROCARIONTE, Texto= " oi eu sou uma célula procarionte,e me chama assim pq eu tenho apenas uma célula no meu corpo")
##trypanosoma_cruzi= Elemento(img=TRYPANOSOMA_CRUZI, Texto = "a galera não gosta muito de mim pq dizem que eu sou parasita e que causa uma doença no coração, mas é que o coração grande é tão quentinho"

#neuronio=Elemento(img= NEURONIO, Texto ="eus ou bem complicado, pois eu fico na cabeça e passo informação pelo corpo, imagina como eu devo ser feito")
#bacteria = Elemento(img= BACTERIA, Texto ="olá eu sou uma pessoa simples, igual arroz pois combino com tudo e posso estar em qualquer lugar, sempre tem espaço para mim")
#espermatozoide= Elemento(img=  ESPERMATOZOIDE, Texto = "eu sou quem dá a origem dos humanos, então imagina como devo ser dificil e complexo me estudar") 
#hemacia= Elemento(img= HEMACIA, Texto= "eu sou o transporte da galera, carrego muita coisa, imagina como sou")
#elodea= Elemento(img= ELODEA, Texto ="eu vivo na agua e sou muito importante para a manutenção do ambiente marinho, posso ser encoderijo , comida ou o2")
#celula_calciforme= Elemento(img= CELULA_CALCIFORME,Texto = "eu fico no instestino delgado eu tenho diversas funções, uma dela pe revestir com muco para proteger onde estou")
#npc= Elemento(img= NPC,Texto = "você precisa descobrir quem é procarionte para a próxima fase")
"""resposta certa é a bactéria"""
#laboratorio.vai()
#Fase1()

#class Fase2():



