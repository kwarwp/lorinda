
{'date': 'Tue Jul 06 2021 21:54:22.248 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 73
  t = JOGO.n(cena, 'É isto! A Parede Celular!'
                                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Apr 27 2022 21:38:52.68 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 90
    main()
  module <module> line 76
    npc = Elemento(NPC, x=400, y=300, w=100, cena=cena, texto="fala", foi=self.jogar)
AttributeError: 'GUI' object has no attribute 'jogar'
'''},