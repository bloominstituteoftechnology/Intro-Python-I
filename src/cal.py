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

now = datetime.datetime.now()
cal = calendar.TextCalendar()
arg = sys.argv

if (len(arg) == 3):
    print(cal.formatmonth(int(arg[2]), int(arg[1])))
# This reverses the order of args,
# assuming that the user will enter month and then year.

else:
    print(cal.formatmonth(int(now.year), int(now.month)))


# c = calendar.TextCalendar(calendar.THURSDAY)
# str = c.formatmonth(2025, 1)
# print(str)

# for day in calendar.day_name:
#     print(day)