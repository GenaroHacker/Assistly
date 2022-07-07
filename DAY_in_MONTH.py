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



#The function return the current day
def get_current_day():
    import datetime
    return datetime.datetime.now().day
