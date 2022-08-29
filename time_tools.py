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

def GetDayPlusOne(year_and_day):
    given_date = datetime.datetime(year_and_day[0], 1, 1) + datetime.timedelta(days=year_and_day[1] - 1)
    new_date = given_date + datetime.timedelta(days=1)
    return (new_date.year, new_date.timetuple().tm_yday)

if __name__ == "__main__":
    print(GetWeek())
    print(GetMonth())
    print(GetYear())
    print(GetDayOfTheYear())
    print(GetYesterday())
    print(GetTomorrow())
    print(GetDayPlusOne((2022, 100)))