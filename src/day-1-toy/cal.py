# Use the 'calendar' module to draw calendars to the console
# https://docs.python.org/3.6/library/calendar.html
#
import sys
import calendar
import datetime

cal = calendar.TextCalendar(calendar.SUNDAY)
str = ""
month = 2
year = 2018
if (len(sys.argv) >= 2):
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    str = cal.formatmonth(year, month)
else:
    d = datetime.date.today()  # get todays date as a date object
    str = cal.formatmonth(d.year, d.month)

print(str)

# Use the sys module to look for command line arguments in the `argv` list
# variable.
#
# If the user specifies two command line arguments, month and year, then draw
# the calendar for that month.


# Stretch goal: if the user doesn't specify anything on the command line, show
# the calendar for the current month. See the 'datetime' module.

# Hint: this should be about 15 lines of code. No loops are required. Read the
# docs for the calendar module closely.
