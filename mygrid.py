from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

import time_tools
from mytextinput import MyTextInput
from sql_interface import InsertRecord
from sql_interface import ReadLastRecord
from sql_interface import CheckIfChangesAreAllowed

from kivy.app import App



class MyGrid(GridLayout):
    widgets_heigth = 300
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
        App.get_running_app().show_popup()
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
                #Read last record from database
                text_for_label = ReadLastRecord("Chronos", label_properties[i][1])[3]
                text_for_label = text_for_label.split('\n')
                text_for_label = [line for line in text_for_label if line.strip()]
                text_for_label = '\n'.join(text_for_label)

                if i == "month":
                    label_properties[i][0].text = "Theme:\n" + text_for_label
    
                if i == "week":
                    label_properties[i][0].text = "Habit:\n" + text_for_label

                if i == "day":
                    label_properties[i][0].text = "Goal:\n" + text_for_label


                #If the record is not the same as the current time, then the record is outdated
                if time_tools.GetYear() != ReadLastRecord("Chronos", label_properties[i][1])[1] or label_properties[i][2] != ReadLastRecord("Chronos", label_properties[i][1])[2]:
                    label_properties[i][0].text = ""
            except IndexError:
                #There is no record in the table
                label_properties[i][0].text = ""
