
{'date': 'Wed May 06 2020 21:49:19.463 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 17
  cientista=Elemento (img=CIENTISTA)
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed May 06 2020 21:49:36.706 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 17
  cientista= lemento (img=CIENTISTA)
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed May 06 2020 21:50:09.422 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 17
  cientista= Elemento (img=CIENTISTA)
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed May 06 2020 22:32:30.874 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 21
    class VINTEDOIS():
  module <module> line 30
    haha=Labirinto (norte=sala1,leste=sala2,oeste=sala3,sul=sala4)
TypeError: __init__() got an unexpected keyword argument 'norte'
'''},