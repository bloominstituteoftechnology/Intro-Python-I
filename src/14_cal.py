"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# save the arguments passed to the script
arguments = sys.argv
c = calendar.TextCalendar(calendar.SUNDAY)
if arguments.__len__() == 1:
  # The user passed no arguments so just show the calendar for this month and year
  str = c.formatmonth(datetime.now().year, datetime.now().month)
  print(str)
elif arguments.__len__() == 2:
  month = arguments[1]
  str = c.formatmonth(datetime.now().year, int(month))
  print(str)
elif arguments.__len__() == 3:
  month = arguments[1]
  year = arguments[2]
  str = c.formatmonth(int(year), int(month))
  print(str)
else:
  print('The arguments expected for this script are the month and year in numerical format.')
  print('Using no arguments will display a calendar for the current month and year')