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

if args > 1 :
    month = int(sys.argv[1])
    year = int(sys.argv[2])
else:
    month = datetime.today().month
    year = datetime.today().year

# Separate arguments with spaces. example: python cal.py 5 2030 will return the calender for May, 2030.
# Running with no arguments will return current month.

print(calendar.TextCalendar().formatmonth(year, month))
