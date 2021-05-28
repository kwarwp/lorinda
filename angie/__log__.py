
{'date': 'Fri May 28 2021 09:58:50.963 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 22
    suj = [Elemento(SUJ, x=int(200+ 170*cos(tt*D30-D90))-25, y=int(200-170*sin(tt*D30-D90))-25,
TypeError: unsupported operand type(s) for **: 'dict' and 'dict'
'''},