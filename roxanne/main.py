# lorinda.roxanne.main.py
from _spy.vitollino.main import Cena,Elemento,Texto 
from _spy.vitollino.main import Inventario as inv

SANDUICHE = "https://www.estudopratico.com.br/wp-content/uploads/2016/12/o-palacio-do-planalto-sede-do-poder-executivo-federal-1200x675.jpg"
ESCOLA = "https://www.hypeness.com.br/wp-content/uploads/2019/09/escla4.jpg"
HOMEM_ARANHA = "https://static3.tcdn.com.br/img/img_prod/460977/pre_venda_boneco_homem_aranha_spider_man_advanced_suit_marvel_s_spider_man_ps4_vgm31_escala_1_6_hot__41848_1_20190313160645.png"
BOB_ESPONJA = "https://cdn-ofuxico.akamaized.net/img/upload/noticias/2020/02/27/bob-esponja-episodio-especial-melhores-momentos-nickelodeon_372085_36.jpg"

def jujuba():
      sanduiche = Cena(img=SANDUICHE)
      escola = Cena(img=ESCOLA)
      homem_aranha = Elemento(img=HOMEM_ARANHA)
      bob_esponja = Elemento (img=BOB_ESPONJA)
      sanduiche.direita=escola
      escola.esquerda=sanduiche
      homem_aranha.entra(sanduiche)
      bob_esponja.entra(escola)
      
      sanduiche.vai
      
jujuba() 