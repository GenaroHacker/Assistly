import kivy

from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty

import time_tools

from sql_interface import CreateTableIfNotExist
from sql_interface import InsertRecord
from sql_interface import ReadLastRecord
from sql_interface import CheckIfChangesAreAllowed






CreateTableIfNotExist()


class MyTextInput(TextInput):
    max_characters = NumericProperty(0)
    def insert_text(self, substring, from_undo=False):
        if len(self.text) > self.max_characters and self.max_characters > 0:
            substring = ""
        TextInput.insert_text(self, substring, from_undo)


class MyGrid(GridLayout):
    textinput_month = ObjectProperty(None)
    label_month = ObjectProperty(None)
    textinput_week = ObjectProperty(None)
    label_week = ObjectProperty(None)
    textinput_day = ObjectProperty(None)
    label_day = ObjectProperty(None)
    my_button = ObjectProperty(None)

    #initialize variables or perform other operations that need to be done after the kv file has been read
    def on_kv_post(self, base_widget):
        self.RefreshLabels()


    def SendButton(self):
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

        self.RefreshLabels()


    def RefreshLabels(self):
        label_properties = {
            "month": [self.label_month, "TableMonth", time_tools.GetMonth()],
            "week": [self.label_week, "TableWeek", time_tools.GetWeek()],
            "day": [self.label_day, "TableDay", time_tools.GetDayOfTheYear()]
            }

        for i in ["month", "week", "day"]:
            try:
                label_properties[i][0].text = ReadLastRecord("Chronos", label_properties[i][1])[3]
            except IndexError:
                label_properties[i][0].text = ""




class architectureApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    architectureApp().run()