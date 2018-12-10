from kivy.graphics import Color, Rectangle, Canvas


class Background(Canvas):
    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)
        self.size_hint = (1.0, 1.0)

        with self.before:
            Color(1, 1, 1)
            self.fundo = Rectangle()

        self.fundo.size = (1980, 1220)

