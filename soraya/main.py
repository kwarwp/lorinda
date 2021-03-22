# lorinda.soraya.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
from _spy.vitollino.main import INVENTARIO as inv 
MARACANA ="https://colunadofla.com/wp-content/uploads/2019/09/maracana-1.jpg"
PICAPAU ="https://i.pinimg.com/originals/b7/52/36/b752361500109d29744c4d872330d9c7.png"
VILA_DE_KONOHA ="https://nerdhits.com.br/wp-content/uploads/2020/06/Konohagakure.jpg"
SONIC ="https://i.pinimg.com/originals/0b/61/b5/0b61b5543bcf94207bb8a9c08a6e99bb.png"
class teste():
    def __init__ (self):
    self.maracana= Cena(img=MARACANA)
    self.vila_de_konoha= Cena(img=VILA_DE_KONOHA)
    self.sonic= Elemento(img=SONIC)
    self.picapau= Elemento(img=PICAPAU)
    self.picapau.entra(self.maracana)
    self.sonic.entra(self.vila_de_konoha)
    self.maracana.direita=self.vila_de_konoha
    self.vila_de_konoha.esquerda=self.maracana
    