from source.app.introducao.introducao import Introducao
from source.app.menus.menu_inicial.menu_inicial import MenuInicial
from source.app.padroes.backgroung import Background

from kivy.uix.floatlayout import FloatLayout


class Manager(FloatLayout):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)

        # definicoes iniciais
        self.size_hint = (1.0, 1.0)
        self.canvas = Background()

        # ponto inicial
        self.introducao = Introducao()
        self.introducao.botao.on_press = self.introducao_menu
        self.add_widget(self.introducao)

    '''
    Os itens abaixo fazem toda a troca de layouts usando botoes dentro dos filhos
    foram implementados desta maneira para que os layouts nao sobrecarreguem a 
    memoria do aparelho sendo adicionados e excuidos um de cada vez, para isso e 
    necessario recriar  os widgets assim em uma propriedade com o self e entao 
    adicionar oseventos de clique com botao
    '''

    def introducao_menu(self):
        self.remove_widget(self.introducao)
        self.menu_inicial = MenuInicial()
        self.add_widget(self.menu_inicial)
