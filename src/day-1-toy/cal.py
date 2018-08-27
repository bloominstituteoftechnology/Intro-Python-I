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

todayDate = datetime.date.today()

if len(sys.argv) > 2:
    # sys.argv[0] is program name, sys.argv[1] is month sys.argv[2] is year
    myCalendar = calendar.TextCalendar(calendar.SUNDAY)
    str = myCalendar.formatmonth(int(sys.argv[2]), int(sys.argv[1]))
    print(str)
else:
    myCalendar = calendar.TextCalendar(calendar.SUNDAY)
    str = myCalendar.formatmonth(int(todayDate.year), int(todayDate.month))
    print(str)


