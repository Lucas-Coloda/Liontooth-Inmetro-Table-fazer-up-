# coding utf-8
# author: Lucas Gyan Coloda

from kivy.uix.gridlayout import GridLayout

class ListaDeTabela(GridLayout):
    def __init__(self, **kwargs):
        super(ListaDeTabela, self).__init__(**kwargs)
        self.size_hint = (1.0, 1.0)

        # definicoes iniciais
        self.size_hint = (1, 1)
        self.pos = (0, 0)
        self.cols = 1