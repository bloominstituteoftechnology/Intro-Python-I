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
import datetime
import sys

currentDate = datetime.datetime.now()
print('DateNow: {}'.format(currentDate))
m, y = None, None
print('\n Month: {0}\n Year: {1}\n'.format((m), (y)))

for i in range(1, len(sys.argv)):
    if int(sys.argv[i]) < 12 and int(sys.argv[i]) >= 0:
        m = sys.argv[i]
    elif int(sys.argv[i]) > 12:
        y = sys.argv[i]

if m and y:
    calendar.prmonth(int(y), int(m))
elif m:
    calendar.prmonth(currentDate.year, int(m))
elif y:
    calendar.prcal(int(y))
elif not m and not y:
    calendar.prmonth(currentDate.year, currentDate.month)
