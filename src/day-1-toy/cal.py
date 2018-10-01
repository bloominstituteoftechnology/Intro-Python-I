# Use the 'calendar' module to draw calendars to the console
# https://docs.python.org/3.6/library/calendar.html
#
# Use the sys module to look for command line arguments in the `argv` list
# variable.
import sys
import calendar
import datetime
arguments=sys.argv
# If the user specifies two command line arguments, month and year, then draw
# the calendar for that month.
if len(arguments)==3:
    month=arguments[1]
    year=arguments[2]
    print(calendar.month(int(year),int(month)))
else:
    date=datetime.date.today().isoformat().split('-')
    month=date[1]
    year=date[2]
    print(calendar.month(int(year),int(month)))

# Stretch goal: if the user doesn't specify anything on the command line, show
# the calendar for the current month. See the 'datetime' module.
# Hint: this should be about 15 lines of code. No loops are required. Read the
# docs for the calendar module closely.

import sys
