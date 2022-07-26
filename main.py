import kivy

from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.properties import ObjectProperty

import time_tools

from sql_interface import CreateTableIfNotExist
from sql_interface import InsertRecord
from sql_interface import ReadLastRecord
from sql_interface import CheckIfChangesAreAllowed




CreateTableIfNotExist()



print(CheckIfChangesAreAllowed())







class MyGrid(GridLayout):
    textinput_month = ObjectProperty(None)
    label_month = ObjectProperty(None)
    textinput_week = ObjectProperty(None)
    label_week = ObjectProperty(None)
    textinput_day = ObjectProperty(None)
    label_day = ObjectProperty(None)
    my_button = ObjectProperty(None)







    def SetPrioritiesButton(self):
        table_properties = {
            "month": [self.textinput_month.text, "TableMonth", time_tools.GetMonth()],
            "week": [self.textinput_week.text, "TableWeek", time_tools.GetWeek()],
            "day": [self.textinput_day.text, "TableDay", time_tools.GetDayOfTheYear()]
            }

        for i in ["month", "week", "day"]:
            if table_properties[i][0] != '' and CheckIfChangesAreAllowed()[i] == True:
                txt = "INSERT INTO {table} VALUES (NULL,{year},{time_interval},'{theme}')"
                my_sql_command = txt.format(table = table_properties[i][1], year = time_tools.GetYear(), time_interval = table_properties[i][2], theme = table_properties[i][0])
                InsertRecord("Chronos", my_sql_command)























class architectureApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    architectureApp().run()