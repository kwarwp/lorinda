
{'date': 'Thu Apr 01 2021 17:05:14.204 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 7
  class fase3():
                ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Apr 07 2021 15:04:24.737 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 17
  self.laboratorio=Cena(img=LABORATORIO)
  ^
IndentationError: expected an indented block
'''},
{'date': 'Wed Apr 07 2021 15:08:20.449 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 18
  self.maria=Elemento(img=MARIA, tit="oi,  Dr. Rosalinda sou sua fã, li todos os seus livros e seu artigo sobre "Direcionamento de Proteínas", ou seja, como as proteínas percorrem toda a célula")
                                                                                                                  ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Apr 07 2021 15:09:02.249 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 42
  self.npc= Elemento(img=NPC, tit " Você não deve esquecer do seu verdadeiro propósito buscar, desvendar um grande enigma celular. Você deve sempre lembrar que para uma célula funcionar, todas as suas organelas conectadas devem estar. Quando uma proteína conseguir transportar, livre você estará!")
                                   ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Apr 07 2021 15:54:22.830 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 66
  self.laboratorio_3.direita=Cena(vai=self.parte_3)
  ^
IndentationError: unexpected indent
'''},
{'date': 'Wed Apr 07 2021 16:03:07.816 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 84
  fase3()parte_5()
          ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Apr 07 2021 16:03:19.44 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 84
    fase3().parte_5()
  module <module> line 82
    Swap(JOGO,ENIGMA,self.laboratorio_4)
TypeError: 'module' object is not callable
'''},