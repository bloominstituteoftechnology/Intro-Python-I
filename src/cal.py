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
from sys import argv
import calendar
from calendar import prmonth
import datetime
from datetime import date

today = date.today()
if len(argv) == 3:
    print(prmonth(int(argv[1]), int(argv[2])))

elif len(argv) == 1:
    print(prmonth(today.year, today.month))

else:
    print('Please enter a month and a date!')