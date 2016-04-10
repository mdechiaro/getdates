#!/usr/bin/python
"""
Function for getting the dates associated with a given day for the month and
year.
"""
import datetime
def get_dates(year, month, day):
    """
    Generator function returns dates associated with a given day for month
    and year.

    Args:
        year  (int): year in integer format
        month (int): month in integer format (1-12)
        day   (str): day in abbreviated string format (mon-sun)
    """
    days = {'mon':0, 'tue':1, 'wed':2, 'thu':3, 'fri':4, 'sat':5, 'sun':6}

    # pylint: disable=invalid-name
    if day in days:
        # start at the beginning of the month
        d = datetime.date(year, month, 1)
        days = days[day] - d.weekday()

        # fast-forward to next week if day does not exist in the first week.
        if days < 0:
            d += datetime.timedelta(days=7)

        d += datetime.timedelta(days)

        # if the first value is the last month, then skip it.
        if d.month == month - 1:
            d += datetime.timedelta(days=7)

        while d.month == month:
            yield d
            d += datetime.timedelta(days=7)

