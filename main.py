import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from sql_interface import CreateTableIfNotExist


CreateTableIfNotExist()


class MyGrid(GridLayout):
    textinput_month = ObjectProperty(None)
    label_month = ObjectProperty(None)
    textinput_week = ObjectProperty(None)
    label_week = ObjectProperty(None)
    textinput_day = ObjectProperty(None)
    label_day = ObjectProperty(None)
    my_button = ObjectProperty(None)

    def btn(self):
        import time_tools
        from sql_interface import InsertRecord

        if self.textinput_month.text != '':
            txt = "INSERT INTO TableMonth VALUES (NULL,{year},{month},'{theme}')"
            my_sql_command = txt.format(year = time_tools.GetYear(), month = time_tools.GetMonth(), theme = self.textinput_month.text)


            InsertRecord("Chronos", my_sql_command)

class architectureApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    architectureApp().run()