# Use the 'calendar' module to draw calendars to the console
# https://docs.python.org/3.6/library/calendar.html
#
# Use the sys module to look for command line arguments in the `argv` list
# variable.
import sys
import calendar
import datetime
l = len(sys.argv)
args = sys.argv
print(args)
print(l)

if l == 3: 
  usercal = calendar.TextCalendar(firstweekday=6).formatmonth(int(args[2]), int(args[1]))
# else:  

#   current_month = datetime.date.month
#   current_year = datetime.date.year
#   usercal = calendar.TextCalendar(firstweekday=6).formatmonth(current_year, current_month)
print(usercal)
#
# If the user specifies two command line arguments, month and year, then draw
# the calendar for that month.

# Stretch goal: if the user doesn't specify anything on the command line, show
# the calendar for the current month. See the 'datetime' module.

# Hint: this should be about 15 lines of code. No loops are required. Read the
# docs for the calendar module closely.

