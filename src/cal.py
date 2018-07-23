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
import datetime

theYear = None
theMonth = None

x = calendar.TextCalendar(firstweekday=0)
now = datetime.datetime.now()
lengthOfArguments = len(sys.argv)

# def dump(obj):
#     for attr in dir(obj):
#         print("obj.%s = %r" % (attr, getattr(obj, attr)))

# dump(y)

if lengthOfArguments == 3:
    theYear = int(sys.argv[1])
    theMonth = int(sys.argv[2])
elif lengthOfArguments == 1:
    theYear = now.year
    theMonth = now.month

print('\n')
x.prmonth(theYear, theMonth, w=0, l=0)
print('\n')