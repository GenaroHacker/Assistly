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





CreateTableIfNotExist()


def CheckIfChangesAreAllowed():
    update_permissions = {"month": False, "week": False, "day": False}

    table_properties = {
        "month": ["TableMonth", time_tools.GetMonth()],
        "week": ["TableWeek", time_tools.GetWeek()],
        "day": ["TableDay", time_tools.GetDayOfTheYear()]
        }

    for i in ["month", "week", "day"]:
        last_record = (None, None, None, None)
        try:
            last_record = ReadLastRecord("Chronos", table_properties[i][0])
        except IndexError:
            #There is no record in the table
            update_permissions[i] = True
        if last_record[1] == time_tools.GetYear() and last_record[2] == table_properties[i][1]:
            #We have a record for this table
            update_permissions[i] = False
        else:
            #We don't have a record for this table
            update_permissions[i] = True

    return update_permissions
print(CheckIfChangesAreAllowed())







class MyGrid(GridLayout):
    textinput_month = ObjectProperty(None)
    label_month = ObjectProperty(None)
    textinput_week = ObjectProperty(None)
    label_week = ObjectProperty(None)
    textinput_day = ObjectProperty(None)
    label_day = ObjectProperty(None)
    my_button = ObjectProperty(None)

    def btn(self):
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