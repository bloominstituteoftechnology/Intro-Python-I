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
import time

x = time.localtime()

datetime.date
if len(sys.argv) == 3:
    calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]))
else:
    calendar.prmonth(int(x[0]),int(x[1]))



#print("the month is {0} and the year is {1}".format(year, month))
#print("The length is:", len(sys.argv))
#calendar.prmonth(int(year), int(month))
