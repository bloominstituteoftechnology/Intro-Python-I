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

year = input('Enter Year: ')
month = input('Enter Month: ')

#def printMonth(year, month):
 #   print(calendar.month(int(year), int(month)))

#printMonth(year,month)

textCalendar = calendar.TextCalendar(firstweekday=6)

today = datetime.datetime.now()
currentYear = today.year
currentMonth = today.month

if len(sys.argv) > 2:
    printMonth = textCalendar.formatmonth(int(sys.argv[1]), int(sys.argv[2]))
else:
    printMonth = textCalendar.formatmonth(currentYear, currentMonth)



#print(sys.argv[1])

print(printMonth)