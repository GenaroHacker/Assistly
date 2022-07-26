import datetime

def GetWeek():
    return datetime.datetime.now().isocalendar()[1]

def GetMonth():
    return datetime.datetime.now().month

def GetYear():
    return datetime.datetime.now().year

def GetDayOfTheYear():
    return datetime.datetime.now().timetuple().tm_yday


if __name__ == "__main__":
    print(GetWeek())
    print(GetMonth())
    print(GetYear())
    print(GetDayOfTheYear())