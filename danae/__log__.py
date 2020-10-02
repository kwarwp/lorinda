
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
{'date': 'Tue Sep 29 2020 12:49:40.73 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 16
    sanct = Sala(*[CENA % parede for parede in SANCT]) 
TypeError: __init__() takes 6 positional argument but more were given
'''},
{'date': 'Tue Sep 29 2020 13:07:28.554 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 16
    sanct = Sala(*[CENA % parede for parede in SANCT]) 
TypeError: __init__() takes 6 positional argument but more were given
'''},
{'date': 'Tue Sep 29 2020 13:31:53.247 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 16
  capel = [Cena(CENA % parede) for parede in CAPEL])
                                                   ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Sep 29 2020 17:00:35.272 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 30
    TheCave()
  module <module> line 26
    self.e_placa = Elemento(self.placa, cena=sanct.leste)
NameError: name 'Elemento' is not defined
'''},
{'date': 'Tue Sep 29 2020 17:10:50.672 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 29
  self.e_jero = Elemento(self.jero, x=380, y=210, w=110, y=220, cena=sanct.leste)
                                                          ^
SyntaxError: keyword argument repeated
'''},
{'date': 'Tue Sep 29 2020 21:41:30.833 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 56
  self.e_jerom.entra(local)        self.e_vecruz.x = 800
                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Oct 02 2020 13:07:41.389 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 155
    TheCave()
  module <module> line 34
    self.sao_jeronimo()
  module <module> line 56
    self.e_jerom.vai = fala.vai
AttributeError: 'TheCave' object has no attribute 'e_jerom'
'''},
{'date': 'Fri Oct 02 2020 17:43:21.674 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 103
  class Altares
                ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Oct 02 2020 17:43:31.175 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 212
    main()
  module <module> line 208
    Altares(sala, sala, sala)
NameError: name 'sala' is not defined
'''},
{'date': 'Fri Oct 02 2020 17:45:14.361 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 212
    main()
  module <module> line 207
    atrio.norte.vai()
NameError: name 'atrio' is not defined
'''},
{'date': 'Fri Oct 02 2020 17:45:31.209 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 212
    main()
  module <module> line 208
    Altares(sala, sala, sala)
  module <module> line 106
    self.icone = Elemento(self.jero, x=360, y=214, w=147, h=250, tit="icone", drag=True)
AttributeError: 'Altares' object has no attribute 'jero'
'''},
{'date': 'Fri Oct 02 2020 17:47:06.935 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 214
    main()
  module <module> line 210
    Altares(sala, sala, sala)
  module <module> line 117
    self.altar_estudio = Elemento(MARCA, x=480, y=100, w=150, h=250, o=0.2, cena=sala.norte,
AttributeError: 'Altares' object has no attribute 'oracao_estudio'
'''},
{'date': 'Fri Oct 02 2020 20:40:12.767 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 120
  def ora(
                                                                                ^
SyntaxError: invalid syntax
'''},