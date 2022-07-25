def current_month_days():
    #The function return the current year
    def get_current_year():
        import datetime
        return datetime.datetime.now().year

    #The function return the current month
    def get_current_month():
        import datetime
        return datetime.datetime.now().month

    #The function return the number of days the current month has
    def get_days_in_month(year, month):
        import calendar
        return calendar.monthrange(year, month)[1]

    return get_days_in_month(get_current_year(), get_current_month())

def get_current_day():
    import datetime
    return datetime.datetime.now().day

def get_mondays_in_month():
    import datetime
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    mondays = []
    for day in range(1, current_month_days()):
        if datetime.datetime(year, month, day).weekday() == 0:
            mondays.append(day)
    return mondays

if __name__ == "__main__":
    print(current_month_days())
    print(get_current_day())
    print(get_mondays_in_month())