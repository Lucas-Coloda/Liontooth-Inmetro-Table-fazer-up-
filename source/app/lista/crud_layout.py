# coding utf-8
# author: Lucas Gyan Coloda

from kivy.uix.pagelayout import PageLayout
from source.app.padroes.botao import Botao


class CrudLayout(PageLayout):
    def __init__(self, **kwargs):
        super(CrudLayout, self).__init__(**kwargs)
        self.size_hint = (1.0, 1.0)
        self.border = 50
        self.page = 0

        # botao de selecionar
        self.selecionar = Botao()
        self.selecionar.background_color = (1,1,1,1)

        # botao de selecionar
        self.editar = Botao()
        self.editar.text = "Editar"
        self.editar.background_color = (.50,.50,.50,1)

        # botao de selecionar
        self.excluir = Botao()
        self.excluir.text = "Deletar"
        self.excluir.background_color = (.50,.50,.50,1)

        self.add_widget(self.selecionar)
        self.add_widget(self.editar)
        self.add_widget(self.excluir)
