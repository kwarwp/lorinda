# lorinda.sarah.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, Popup, INVENTARIO
from collections import namedtuple
Ator = namedtuple('Elenco','ator nome mini alinha')
Fala = namedtuple('Fala','ator fala prox age')  # , defaults=(None,)*4)
A = namedtuple('Ali','e m d')(-1, 0, 1)

class Roteiro:
    def __init__(self, cena, roteiro, elenco=(), foi=None, loc=(0, 0)):
        self.dic_ator = {a.ator: a for a in elenco}
        self.local = loc
        _prox = zip(roteiro, roteiro[1:] + [Fala(None, "", None, None)])
        self.foi = foi if foi else lambda *_: None
        roteiro = [Fala(a, f, g if g else (p.ator if p else None), x) for [a, f, g, x], p in _prox]
        self.rotid = ''.join(ator_.nome[0] if ator_.nome else '_' for ator_ in elenco)+f"@{len(roteiro)}"
        self.rotsiz = len(roteiro)
        # print(list(prox))
        # print(roteiro)
        # return
        self.elenco, self.roteiro = elenco, roteiro
        self._foi = lambda *_: None
        script = self
        for _ator in elenco:
            _ator.ator.vai = self.nada
            _ator.ator.tit = _ator.nome
            _ator.ator.elt.style.filter = "brightness(30%)"
        protagonista = elenco[0].ator if elenco else roteiro[0].ator
        self.atores = [ator.ator for ator in elenco] if elenco else [ator.ator for ator in roteiro]
        protagonista.vai = self.segue
        protagonista.elt.style.filter = "brightness(100%)"

        class Falar(Texto):
            def __init__(self, ator, fala, prox, act=None, mini=1, **kwarg):
                self.ator, self.fala, self.prox = ator, fala, prox
                self._foi = act or self.nada
                minih = 100/mini
                self.mini = Elemento(ator.img, cena=cena, x=-60, w=ator.w, h=ator.h * mini, tipo=f"100% {100/mini}%",
                                     style=dict(top="", bottom="100%", margin="-150px -minih"))
                super().__init__(cena, fala, **kwarg)

            def esconde(self, *_):
                self.mini.elt.remove()
                self.ator.elt.style.filter = "brightness(30%)"
                script.testa(self.prox)
                # script.segue()
                # super().esconde()
                self._foi()

            def vai(self, *_):
                from browser import document, html
                super().vai()
                #Popup.POP.div <= self.mini.elt
                document["__baloon__"] <= self.mini.elt
                document["__baloon__"] <= html.DIV(self.ator.tit, 
                style=dict(position="absolute", bottom="100%", left=self.ator.w - 60, background="white", padding="5px"))
                self.ator.elt.style.filter = "brightness(5%)"
                self.ator.vai = self.nada

            @property
            def foi(self):
                return self._foi

            @foi.setter
            def foi(self, value):
                self._foi = value

            def nada(self, *_):
                pass

        self._fala = Falar

    def nada(self, *_):
        pass

    def segue(self, *_):
        ator, fala, prox, action = self.scripter()
        casa, carta = self.local
        score = dict(casa=casa, carta=carta, move="dialogo", ponto=self.rotsiz-len(self.roteiro), valor=self.rotid)

        # ator.elt.style.filter = "brightness(30%)"
        fala = self._fala(ator, fala, prox, action, mini=self.dic_ator[ator].mini)  # .vai()
        INVENTARIO.score(**score)
        if prox:
            prox.vai = self.segue
        fala.vai()

    def testa(self, prox, *_):
        if self.roteiro:
            prox.elt.style.filter = "brightness(100%)"
        else:
            for ato in self.atores:
                ato.elt.style.filter = "brightness(100%)"
            self.foi()

    def scripter(self, *_):
        return self.roteiro.pop(0)
