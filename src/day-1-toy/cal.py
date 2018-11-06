# Use the 'calendar' module to draw calendars to the console
# https://docs.python.org/3.6/library/calendar.html
#
# Use the sys module to look for command line arguments in the `argv` list
# variable.
#
# If the user specifies two command line arguments, month and year, then draw
# the calendar for that month.

# Stretch goal: if the user doesn't specify anything on the command line, show
# the calendar for the current month. See the 'datetime' module.

# Hint: this should be about 15 lines of code. No loops are required. Read the
# docs for the calendar module closely.

import sys
import datetime
import calendar


def cal():
    arguments = sys.argv[1:]
    now = datetime.datetime.now()
    month = now.month
    year = now.year

    if len(arguments) > 1:
        month = int(arguments[0])
        year = int(arguments[1])

    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(year, month, 3, 1)
    print(str)


cal()
