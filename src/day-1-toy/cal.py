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

# sys is a python library.
import sys

import datetime

import calendar


today = datetime.datetime.today()
c = calendar.TextCalendar(calendar.SUNDAY)

year = input("Enter YEAR (yyyy): ")
month = input("Enter Month (mm): ")
cal_str = c.formatmonth(int(year), int(month))
print(cal_str)

""""
if (len(argv) == 3):
    print(cal.formatmonth(int(argv[1]), int(argv[2])))

elif(len(argv) == 1):
    print(prmonth(int(argv[2]), int(argv[1])))

else:
    print('Enter MONTH AND DATE')
    print(cal.formatmonth(int(today.year), int(today.month)))
"""



#def weekday(month, day, year):
#   return datetime.date(month, day, year).weekday()
