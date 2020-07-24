# lorinda.kathryn.main.py
from_supy.vitolino.main.import Cena,Elemento,Texto, STYLE
form_supy.vitolino.main.import Inventario as inv

STYLE["Width"] = 800
STYLE["height"] = "600px"

#CENA 1 VERBO LEMBRAR HEREDITARIEDADE

SALA_FIOCRUZ = "http://supygirls.pythonanywhere.com"
ROSALINDA = "https://i.imgur.com/qvuwHvs.png"
ZEZINHO = "https://i.imgur.com/94lhgKo.png"
NPC = " https://i.imgur.com/NEG2o8W.jpg"
PERGAMINHO = "https://i.imgur.com/Xe3zdhP.jpg"
PESSOA_BRANCA_CABELO_LISO_OLHOS_VERDES = "https://i.imgur.com/6vgubFm.jpg"
PESSOA_NEGRA_CABELO_BLACK_OLHOS_CASTANHOS = "https://i.imgur.com/wtpBiVS.jpg"
PESSOA_RUIVA_PELE_BRANCA_CABELO_VERMELHO = "https://i.imgur.com/ZcfLShe.jpg"
CRIANCA_BRANCA_CABELO_LISO_OLHOS_VERDES = "https://i.imgur.com/ISvWiD4.jpg"
CRIANCA_NEGRA_CABELO_BLACK_OLHOS_CASTANHOS = "https://i.imgur.com/qoGRKc8.jpg"
CRIANCA_RUIVA_PELE_BRANCA_CABELO_VERMELHO = "https://i.imgur.com/DtSbcLh.jpg"
QUADRO_1_PESSOA_BRANCA_CABELO_LISO_OLHOS_VERDES = "https://i.imgur.com/6vgubFm.jpg"
QUADRO_2_PESSOA_RUIVA_PELE_BRANCA_CABELO_VERMELHO = "https://i.imgur.com/6vgubFm.jpg"
QUADRO_3_PESSOA_RUIVA_PELE_BRANCA_CABELO_VERMELHO = "https://i.imgur.com/ZcfLShe.jpg"
QUADRO_4_CRIANCA_BRANCA_CABELO_LISO_OLHOS_VERDES = "https://i.imgur.com/ISvWiD4.jpg"
QUADRO_5_CRIANCA_NEGRA_CABELO_BLACK_OLHOS_CASTANHOS = "https://i.imgur.com/qoGRKc8.jpg"
QUADRO_6_CRIANCA_RUIVA_PELE_BRANCA_CABELO_VERMELHO = "https://i.imgur.com/DtSbcLh.jpg"
MUSEU_DA_VIDA = "https://i.imgur.com/s4ZBrRv.jpg"
DNA = "https://www.facebook.com/Projeto-SupyGirls-2062797764002029"
Genes = "https://i.imgur.com/SBcbyUc.gif"
Caixa de enigma = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR6joEvEOfFUM8XeYOGB5xZNKAvpvVkyxejzA&usqp=CAU"
nucleotideo DNA = "https://static.docsity.com/documents_pages/notas/2010/08/25/e5bcbeb3ff59af5f4b1528a2a1aed613.png"
Cofre = "https://static.vecteezy.com/system/resources/previews/000/269/461/non_2x/closed-cartoon-treasure-chest-vector.jpg"
Abrir cofre = "https://image.freepik.com/vetores-gratis/cofre-do-tesouro-dos-desenhos-animados-aberto_26659-11.jpg"
PenDrive = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fbr.123rf.com%2Fphoto_54600423_%25C3%25ADcone-da-unidade-flash-usb-no-estilo-dos-desenhos-animados-isolado-no-fundo-branco.html&psig=AOvVaw0HXXKKU33SN2mlVo8NvDUD&ust=1595692819971000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKDJspWh5uoCFQAAAAAdAAAAABAD"
garrafinhapocaomagica = "https://i.pinimg.com/originals/69/4d/0e/694d0e28c8f9afe60797b2c7deaa4844.jpg
casafiocruz = "https://agencia.fiocruz.br/sites/agencia.fiocruz.br/files/u34/coc_peterilicciev.jpg"
chave embaixo do tapete = "https://i1.wp.com/blog.maxximapatrimonial.com.br/wp-content/uploads/2018/10/where-not-to-leave-your-keys-1024x683.jpg?resize=1024%2C683&ssl=1"
homem negro cabelos crespos olhos castanhos nariz medio e boca larga = "https://i.pinimg.com/236x/21/c3/47/21c347c81dea45b488fb25c54a513333--top-mens-hairstyles-dread-hairstyles.jpg"
mulher negra cabelos cacheados olhos pretos nariz medio boca larga = "https://4.bp.blogspot.com/_R8LkKSvcN4c/TUBKXXOUZDI/AAAAAAAAaVc/tUoN1-9LjXc/s1600/1%2Ba%2Ba%2Ba%2Bc%2Bcrespo%2Bnegras.jpg"
Menina  Branca Cabelo liso Nariz grande olhos verdes boca pequena = "https://i.pinimg.com/originals/b9/b7/4e/b9b74edff8157f22e49e38802df54676.jpg"

# O CÓDIGO DO MINE GAME ENTRA AQUI?
class primeira_fase():

sala_fiocruz = Cena(img= SALA_FIOCRUZ)
rosalinda = Elemento( img = ROSALINDA, tit= "Tenho que me apresar, preciso de dinheiro para continuar minha pesquisa." ,
        style=dict (left=400, top=350, width=300, height="200px",))
npc = Elemento(img= NPC)
pergaminho = Elemento(img=PERGAMINHO)
pessoa_branca_cabelo_liso = Elemento(img= PESSOA_BRANCA_CABELO_LISO_OLHOS_VERDES)
pessoa_negra_cabelo-black = Elemento (img = PESSOA_NEGRA_CABELO_BLACK_OLHOS_CASTANHOS)
pessoa_ruiva_pele_branca_cabelovermelho = Elemento (img = PESSOA_RUIVA_PELE_BRANCA_CABELO_VERMELHO)
crianca_branca-cabelo-liso_olhos_verdes = Elemento (img = CRIANCA_BRANCA_CABELO_LISO_OLHOS_VERDES)
crianca_negra_cabelo_black_olhos_castanhos = Elemento (img = CRIANCA_NEGRA_CABELO_BLACK_OLHOS_CASTANHOS)
crianca_ruiva_pele_branca_cabelo_vermelho = Elemento (img = CRIANCA_RUIVA_PELE_BRANCA_CABELO_VERMELHO )

#CENA 2 VERBO ENTENDER HEREDITARIEDADE

MUSEU_DA_VIDA = Cena

O NPC DEVERÁ APRESENTAR AS SEGUINTES DICAS ORGANIZAR AS PALAVRAS UTILIZANDO A ORDEM CORRETA DE ENTENDIMENTO




Nucleotídeos

Características

Organismo

Sequência correta

Abrir cofre

PenDrive

Poção mágica

Super poderes
