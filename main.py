import kivy
from kivy.app import App
from sql_interface import CreateTableIfNotExist
from mygrid import MyGrid

CreateTableIfNotExist()

class mygridarchitectureApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    mygridarchitectureApp().run()