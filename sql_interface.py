import sqlite3
from sql_core import CreateTable
from sql_core import InsertRecord
from sql_core import InsertSeveralRecords
from sql_core import ReadRecords
from sql_core import ReadLastRecord
from sql_core import UpdateRecord
from sql_core import RemoveRecord
from sql_core import RunCommand



def CreateTableIfNotExist():
    try:
        tables_parameters = [
            ["MONTH", "THEME", "TableMonth"],
            ["WEEK", "HABIT", "TableWeek"],
            ["DAY", "OBJECTIVE", "TableDay"]
            ]

        for i in tables_parameters:
            columns = """
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    YEAR INTEGER,
                    """ + i[0] + """ INTEGER,
                    """ + i[1] + """ VARCHAR(50)"""

            CreateTable("Chronos",i[2],columns)
    except sqlite3.OperationalError:
        pass



def CheckIfChangesAreAllowed():
    import time_tools
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