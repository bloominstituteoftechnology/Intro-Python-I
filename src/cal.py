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

argLength = len(sys.argv)

myCal = calendar.TextCalendar(calendar.SUNDAY)


if argLength == 3:
    month = sys.argv[1]
    year = sys.argv[2]
    stringCal = myCal.formatmonth(int(year), int(month))
elif argLength == 1:
    now = datetime.datetime.now()
    stringCal = myCal.formatmonth(now.year, now.month)

print(stringCal)
