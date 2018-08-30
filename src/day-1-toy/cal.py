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

# y = input("Enter the year (YYYY): ")
# m = input("Enter the month (M or MM - Sep=9, Oct=10): ")

# c = calendar.TextCalendar()
# str = c.formatmonth(int(y), int(m))
# print(str)

import datetime

if len(sys.argv) > 2:
    yr = sys.argv[1]
    mo = sys.argv[2]
else:
    yr = datetime.datetime.now().year
    mo = datetime.datetime.now().month

cc = calendar.TextCalendar()
str = cc.formatmonth(int(yr), int(mo))
print(str)