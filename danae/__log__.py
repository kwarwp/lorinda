
{'date': 'Tue Sep 29 2020 12:27:34.341 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  from _spy.vitollino.main import Cena, Sala STYLE
                                                  ^
SyntaxError: trailing comma not allowed without surrounding parentheses
'''},
{'date': 'Tue Sep 29 2020 12:47:47.109 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 23
    TheCave()
  module <module> line 15
    atrio = Sala(*[CENA % parede for parede in INTER]) 
TypeError: __init__() takes 6 positional argument but more were given
'''},