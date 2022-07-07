from calendar import week

from numpy import divide
from DAY_in_MONTH import get_current_day
from DAY_in_MONTH import current_month_days

print(get_current_day())
print(current_month_days())



class someDay:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.week = week

    def get_week(self):
        return self.week


#example
day = someDay(1, 1, 2020)

print(day.get_week())

