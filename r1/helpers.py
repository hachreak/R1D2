import datetime as dt
from six import itertools as it

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return it.izip_longest(*args, fillvalue=fillvalue)


def today():
    return dt.date.today()


def first_day_of_this_week():
    t = today()
    return t - dt.timedelta(days=t.weekday())
