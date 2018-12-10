from kivy.uix.button import Button


class Botao(Button):
    def __init__(self, **kwargs):
        super(Botao, self).__init__(**kwargs)
        self.font_name = "Montserrat"
        self.background_color = (0, 0, 0, 1)
        self.color = (0, 0, 0, 1)
        self.font_size = 25
        self.text = "null"
        self.halign = "center"
