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

# If more than 2 extra args given, print warning and exit
if len(sys.argv) > 3:
  print('Too many arguments. 14_cal.py expects either to be called with no arguments, \n\
    with a numeric month, or with a numeric month followed by a year')
  sys.exit()

# initialize month and year to current values
month = datetime.today().month
year = datetime.today().year

# if 2 additional arguments passed in, set year to year argument
if len(sys.argv) > 2:
  year = int(sys.argv[2])

# if at least 1 additional argument passed in, set month to month argument
if len(sys.argv) > 1:
  month = int(sys.argv[1])

# initialize calendar and print month
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(theyear=year,themonth=month)