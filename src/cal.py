"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
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

num_of_args = len(sys.argv)
if num_of_args == 1:
    month = datetime.now().date().month
    year = datetime.now().date().year
elif num_of_args == 2:
    month = int(sys.argv[1])
    year = datetime.now().date().year
else:
    month = int(sys.argv[1])
    year = int(sys.argv[2])

cal = calendar.TextCalendar()
print(cal.formatmonth(year, month, w=0, l=0))
