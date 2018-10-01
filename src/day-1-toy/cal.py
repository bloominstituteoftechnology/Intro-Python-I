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

c = calendar.TextCalendar()

if len(sys.argv) == 1:
  print("You entered no month or year, so we'll assume you mean this month and year\n")
  month = datetime.datetime.now().month
  year = datetime.datetime.now().year
  str = c.formatmonth(year,month)
  print(str)

elif len(sys.argv) == 2:
  print("You entered 1 input value..Please enter two value, the month and the year!\n")

elif len(sys.argv) == 3:
  print("You entered 3 values! Hooray \n")
  month = int(sys.argv[1])
  year = int(sys.argv[2])
  str = c.formatmonth(year,month)
  print(str)