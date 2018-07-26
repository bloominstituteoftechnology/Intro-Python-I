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

c = calendar.TextCalendar(calendar.SUNDAY)
if len(sys.argv) < 3:
  today = datetime.now()
  output = c.formatmonth(today.year, today.month)
  print(output)
else:
  output = c.formatmonth(int(sys.argv[1]), int(sys.argv[2]))
  print(output)

