# coding utf-8
# author: Lucas Gyan Coloda

from kivy.uix.gridlayout import GridLayout
from source.app.lista.crud_layout import CrudLayout


class ListaDeTabela(GridLayout):
    def __init__(self, **kwargs):
        super(ListaDeTabela, self).__init__(**kwargs)

        # definicoes iniciais
        self.size_hint = (1, 1)
        self.pos = (0, 0)
        self.cols = 1

        # pegar lista de tabelas do banco
        simulacao_banco = ["tabela1", "tabela2", "tabela3", "tabela4", "tabela5"]

        for a in simulacao_banco:
            self.temporario = CrudLayout()
            self.temporario.selecionar.text = a
            self.add_widget(self.temporario)
