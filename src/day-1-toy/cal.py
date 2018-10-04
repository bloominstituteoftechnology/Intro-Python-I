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
import calendar
from datetime import datetime 

args = len(sys.argv)
print(args,"args")
# def drawCalendar(year = None, month= None):
#     cal = calendar.TextCalendar(calendar.SUNDAY)
#     print("once")
#     if month is None or year is None:
#         now = datetime.now()
#         print( type(now.year), type(now.month))
#         return cal.prmonth(now.year, now.month)
#     else:
#         return cal.prmonth(year, month)


# print(drawCalendar())
# print(drawCalendar(year = 2018, month = 9))

def drawCalendar(*args):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    if len(args) < 2:
        now = datetime.now()
        #print( type(now.year), type(now.month))
        return cal.prmonth(now.year, now.month)
    else:
        return cal.prmonth(args[0], args[1])


print(drawCalendar())
print(drawCalendar(2018, 9))



