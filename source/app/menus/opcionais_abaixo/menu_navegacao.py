# coding utf-8
# author: Lucas Gyan Coloda

from kivy.uix.gridlayout import GridLayout
from source.app.padroes.botao import Botao
from kivy.utils import get_color_from_hex as hexa


class MenuNavegador(GridLayout):
    def __init__(self, **kwargs):
        super(MenuNavegador, self).__init__(**kwargs)

        # definicoes iniciais
        self.size_hint = (1, 1)
        self.pos = (0, 0)
        self.rows = 1
        self.cols = 3

        # botao para tabelas
        self.botao_tabela = Botao()
        self.botao_tabela.color = hexa("#2b47ff")
        self.botao_tabela.text = "Tabelas"

        # botao adicionar algo
        self.botao_adicionar = Botao()
        self.botao_adicionar.color = hexa("#ffe32b")
        self.botao_adicionar.font_size = 60
        self.botao_adicionar.text = "+"

        # botao para balancas
        self.botao_balanca = Botao()
        self.botao_balanca.color = hexa("#2b47ff")
        self.botao_balanca.text = "Balanças"

        # adicao dos widgets
        self.add_widget(self.botao_tabela)
        self.add_widget(self.botao_adicionar)
        self.add_widget(self.botao_balanca)
