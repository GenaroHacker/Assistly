import kivy
from sql_interface import CreateTableIfNotExist
from kivy.app import App
from mygrid import MyGrid
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.lang import Builder

CreateTableIfNotExist()

class CustomPopupMonth(Popup):
    pass

class CustomPopupWeek(Popup):
    pass

class CustomPopupDay(Popup):
    pass

class mygridarchitectureApp(App):
    def build(self):
        layout = MyGrid(cols=1, padding=10, spacing=10,
                size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        return root

    def ShowPopupMonth(self):
        p = CustomPopupMonth()
        p.open()

    def ShowPopupWeek(self):
        p = CustomPopupWeek()
        p.open()

    def ShowPopupDay(self):
        p = CustomPopupDay()
        p.open()

if __name__ == "__main__":
    mygridarchitectureApp().run()

