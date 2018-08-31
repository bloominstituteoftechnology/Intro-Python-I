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

sal = len(sys.argv)

if sal == 2:
    month = None
    year = int(sys.argv[1])
elif sal == 3:
    month = int(sys.argv[1])
    year = int(sys.argv[2])
else:
    print("\n usage: cal.py month(optional) year \n")
    month = datetime.today().month
    year = datetime.today().year
    # sys.exit(1)

myCal = calendar.TextCalendar(firstweekday=6)

if month != None:
    myCal.prmonth(year, month)
else:
    myCal.pryear(year)

#USAGE, cd INTO DIR.  TYPE "python cal.py [#MONTH, OPTIONAL] [#YEAR]"