import sqlite3
from sql_core import CreateTable
from sql_core import InsertRecord
from sql_core import InsertSeveralRecords
from sql_core import ReadRecords
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
