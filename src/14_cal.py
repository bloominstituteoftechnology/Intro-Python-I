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

current_month = int(datetime.now().month)
current_year = int(datetime.now().year)

if len(sys.argv) <= 1:
    print(calendar.month(current_year, current_month))
elif len(sys.argv) == 2:
    print(calendar.month(current_year, int(sys.argv[1])))
elif len(sys.argv) == 3:
    print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
else:
    print(
        'If specifying a month, or both a month and year, the format is:\n\n"14_cal.py month [year]"\n\nwhere "month" is a number 1 through 12 representing that month, and "[year]" is optionally provided as a 4 digit number.')
