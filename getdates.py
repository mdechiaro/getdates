#!/usr/bin/python
import datetime
def get_dates(year, month, day):
    """
    function returns dates associated with a given day for month and year.
    """
    days = {'mon':0,'tue':1,'wed':2,'thu':3,'fri':4,'sat':5,'sun':6}
    if day in days:
        d = datetime.date(year, month, 1)
        days = days[day] - d.weekday()

        # fast-forward to next week if day does not exist in the first week.
        if days < 0:
            d += datetime.timedelta(days = 7)

        d += datetime.timedelta(days)

        # if the first value is the last month, then skip it.  
        if d.month == month - 1:
            d += datetime.timedelta(days = 7)

        while d.month == month:
            yield d
            d += datetime.timedelta(days = 7)

