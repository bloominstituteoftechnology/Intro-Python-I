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
y = input('Give me a year (yyyy): ')
m = input('Give me a month (mm): ')
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(int(y), int(m))
print (str)


"""
Amy solution
```import calendar
import sys
import datetime

now = datetime.datetime.now()
cal = calendar.TextCalendar()
arg = sys.argv

if (len(arg) == 3):
    print(cal.formatmonth(int(arg[2]), int(arg[1])))
# This reverses the order of args,
# assuming that the user will enter month and then year.

else:
    print(cal.formatmonth(int(now.year), int(now.month)))```
"""

"""
csaba solution
import sys
import calendar
import datetime
import time

x = time.localtime()

datetime.date
if len(sys.argv) == 3:
    calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]))
else:
    calendar.prmonth(int(x[0]),int(x[1]))
"""

"""
Thuy solution
import sys
import calendar
import datetime


year = input("Enter year: ")
month = input("Enter month: ")
now = datetime.datetime.now()

if not year and not month:
    year = now.year
    month = now.month
elif not year:
    year = now.year
    month = int(month)
elif not month:
    month = now.month
    year = int(year)
else:
    year = int(year)
    month = int(month)
    
def printCal(year, month):
    print(calendar.month(year,month))


printCal(year, month)
"""

