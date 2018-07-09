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
from datetime import date
from calendar import prmonth
from sys import argv # argv is a list of the arguments passed to a script (from the command line). https://docs.python.org/3/library/sys.html

today = date.today()

# if month and year are specified
if len(argv) == 3: 
    prmonth(int(argv[1]), int(argv[2])) #prmonth = print month; first int is year, second is month

    # EX - if in command line I type 'python cal.py 2018 8'
        # argv[0] = cal.py
        # argv[1] = 2018
        # argv[2] = 8


# if month and year are not specified (just running the file name)
elif len(argv) == 1:
    prmonth(today.year, today.month) # prints current month

else:
    print('Please enter a month and a date!')
