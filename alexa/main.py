# lorinda.alexa.main.py
#TASSIA- 3001 isabelle
from _spy.vitollino.main import Cena, Elemento, Labirinto
from _spy.vitollino.main import INVENTARIO as inv
#fase1
CIENTISTA="https://3.bp.blogspot.com/_YaD6P9li0m0/SOp_1mDcfPI/AAAAAAAAAHk/wGNocvYRjbY/s320/222px-Professor_Frink.png"
ESCADA="https://i.pinimg.com/originals/77/83/aa/7783aae2cd02f662c3344824ecd43287.jpg"
PRATELEIRA="https://img.elo7.com.br/product/original/1FC472F/aparador-de-livros-sangue-escorrendo-presente-de-natal.jpg"
CAMERA="https://hto.ifsp.edu.br/portal/images/IFSP/Cursos/Coord_Mec/Fotos/LaboratoriosMecanica/Imagem13.jpg"
SETAS="https://img.lovepik.com/element/40121/1672.png_860.png"
CORREDOR="https://www.dalcomad.com.br/wp-content/uploads/2018/08/socialpost7.png"
LABORATORIO="https://sites.usp.br/labvirofcfrp/wp-content/uploads/sites/700/2020/02/Eletroforese-300x225.png"
#fase2



#FASE3



class VINTEDOIS():
    #def __init__(self)
    cientista= Elemento (img=CIENTISTA)
    sala1= Cena (img=ESCADA)
    sala2= Cena (img=PRATELEIRA)
    sala3=Cena (img=CAMERA)
    setas= Elemento (img=SETAS)
    sala4=Cena (img=CORREDOR)
    sala5=Cena (img=LABORATORIO)
    haha=Labirinto (norte=sala1,leste=sala2,oeste=sala3,sul=sala4)
    cientista.entra(haha.norte)
    setas.entra(haha.sul)
    haha.norte.vai
    
VINTEDOIS()