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
import datetime
import calendar

now = datetime.datetime.now()

try:
  month = int(sys.argv[1])
except IndexError:
  month = now.month

try:
  year = int(sys.argv[2])
except IndexError:
  year = now.year

if month < 1 or month > 12:
  print("The 'month' argument should be an integer between 1 and 12, with 1 representing January, 2 representing February, and so forth.\nIf there are no arguments, the \'month\' and \'year\' will be the current month and year.\n\nSyntax:\npython3 cal.py <month> <year>\n")
  exit(1)

if year < datetime.MINYEAR or year > datetime.MAXYEAR:
  print(f'The \'year\' argument should be an integer between {datetime.MINYEAR} and {datetime.MAXYEAR}.\nThis argument is optional. If there is no \'year\' argument, \'year\' will be the current year.\n\nSyntax:\npython3 cal.py <month> <year>\n')
  exit(1)

cal = calendar.TextCalendar(calendar.SUNDAY)

"""
calendar.TextCalendar accepts a firstweekday parameter. You can pass a number 0 - 6, with 0 corresponding to Monday, and 6 to Sunday. Default is 0. Alternatively, you can use calendar.<DAY OF WEEK IN CAPS>, as found in https://www.guru99.com/calendar-in-python.html
"""

cal_str = cal.formatmonth(year, month)
print(cal_str)
