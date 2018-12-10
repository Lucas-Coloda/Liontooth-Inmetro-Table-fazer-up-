from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex as hexa
from source.app.padroes.botao import Botao


class Introducao(FloatLayout):
    def __init__(self, **kwargs):
        super(Introducao, self).__init__(**kwargs)
        self.size_hint = (1.0, 1.0)

        # botao
        self.botao = Botao()
        self.botao.text = ""
        self.botao.pos = (0, 250)

        # texto liontooth
        self.texto = Label()
        self.texto.text = "LionTooth"
        self.texto.font_name = "Montserrat"
        self.texto.halign = "center"
        self.texto.font_size = 28
        self.texto.color = hexa("#ffe32b")
        self.texto.size_hint = (.5, 1)
        self.texto.pos = (1, 0)

        # texto liontooth
        self.texto2 = Label()
        self.texto2.text = "Inmetro Table"
        self.texto.font_name = "Montserrat"
        self.texto2.halign = "center"
        self.texto2.font_size = 28
        self.texto2.color = hexa("#2b47ff")
        self.texto2.size_hint = (.5, 1)
        self.texto2.pos = (160, 0)

        # adicao dos widgets
        self.add_widget(self.botao)
        self.add_widget(self.texto)
        self.add_widget(self.texto2)
