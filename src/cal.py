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
import sys
import datetime
cal = calendar.TextCalendar(calendar.SUNDAY)

if len(sys.argv) > 2:
	year = int(sys.argv[1])
	month = int(sys.argv[2])
else:
	date = datetime.datetime.now()
	year = date.year
	month = date.month

print(cal.formatmonth(month, year))	
