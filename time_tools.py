import datetime

def GetWeek():
    return datetime.datetime.now().isocalendar()[1]

def GetMonth():
    return datetime.datetime.now().month

def GetYear():
    return datetime.datetime.now().year

def GetDayOfTheYear():
    return datetime.datetime.now().timetuple().tm_yday

def GetYesterday():
    return (datetime.datetime.now() - datetime.timedelta(days=1)).timetuple().tm_yday

def GetTomorrow():
    return (datetime.datetime.now() + datetime.timedelta(days=1)).timetuple().tm_yday

#The following function takes a tuple with a year and a day like (2022, 239) and transform it into a datetime.datetime object
#then it sums 2 days to it and returns a tuple with the year and the day of the year of the new date
def GetDayPlusTwo(year_and_day):
    given_date = datetime.datetime(year_and_day[0], 1, 1) + datetime.timedelta(days=year_and_day[1] - 1)
    new_date = given_date + datetime.timedelta(days=2)
    return (new_date.year, new_date.timetuple().tm_yday)



if __name__ == "__main__":
    print(GetWeek())
    print(GetMonth())
    print(GetYear())
    print(GetDayOfTheYear())
    print(GetYesterday())
    print(GetTomorrow())
    print(GetDayPlusTwo((2022, 15)))