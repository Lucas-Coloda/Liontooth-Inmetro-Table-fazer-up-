# coding: utf-8
# author: Lucas Gyan Coloda

from kivy.app import App
from kivy.interactive import InteractiveLauncher
from source.app.manager.manager import Manager


class InmetroTableApp(App):
    def build(self):
        return Manager()


if __name__ == '__main__':
    inmetroTable = InmetroTableApp()
    inmetroTable = InteractiveLauncher(inmetroTable)
    inmetroTable.run()
