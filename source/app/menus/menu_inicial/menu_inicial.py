# coding utf-8
# author: Lucas Gyan Coloda

from kivy.uix.floatlayout import FloatLayout
from source.app.menus.opcionais_abaixo.menu_navegacao import MenuNavegador
from source.app.lista.tabelas import ListaDeTabela



class MenuInicial(FloatLayout):
    def __init__(self, **kwargs):
        super(MenuInicial, self).__init__(**kwargs)
        self.size_hint = (1.0, 1.0)

        self.atual = ListaDeTabela()

        self.menu_baixo = MenuNavegador()
        self.menu_baixo.size_hint = (.95, .09)

        self.add_widget(self.atual)
        self.add_widget(self.menu_baixo)
