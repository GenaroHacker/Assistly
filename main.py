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
        if self.textinput_month.text != '' and self.update_month_enabled == True:
            txt = "INSERT INTO TableMonth VALUES (NULL,{year},{month},'{theme}')"
            my_sql_command = txt.format(year = time_tools.GetYear(), month = time_tools.GetMonth(), theme = self.textinput_month.text)
            InsertRecord("Chronos", my_sql_command)
            self.update_month_enabled = False










class architectureApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    architectureApp().run()