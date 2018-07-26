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

cal = calendar.TextCalendar(6)
if len(sys.argv) == 3:
  m = int(sys.argv[1])
  y = int(sys.argv[2])

  if 0 < m < 13:
    print(cal.formatmonth(y, m))
  else:
    print("Error: Invalid month")
elif len(sys.argv) > 1:
  print("Usage: python cal.py <mm> <yyyy>")
else:
  cur = datetime.date.today()
  print(cal.formatmonth(cur.year, cur.month))
