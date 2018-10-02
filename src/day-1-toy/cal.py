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
import calendar
from datetime import datetime 

def drawCalendar(*args):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print("once")
    if len(args) < 2:
        now = datetime.now()
        print( type(now.year), type(now.month))
        return cal.prmonth(now.year, now.month)
    else:
        return cal.prmonth(args[0], args[1])


print(drawCalendar())
print(drawCalendar(2018, 9))