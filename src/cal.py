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

argc = len(sys.argv) # number of arguments given to the command line

if argc == 2:
	# not enough args were given
	month = None
	year = int(sys.argv[1])
elif argc == 3:
	# month and year are given
	month = int(sys.argv[1])
	year = int(sys.argv[2])
else:
	# error check for incorrect inputs
	print("usage: cal.py [month] year")
	sys.exit(1)

# set Sunday to be the first day of the week
calendar = calendar.TextCalendar(6) # generate a string formatted calendar

if month != None:
	calendar.prmonth(year, month) # print month's calendar
else:
	calendar.pryear(year) # print calendar for the whole year










