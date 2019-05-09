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

err = print("Month and year must be entered in the format: mm [yyyy]")

import sys
import calendar
from datetime import datetime

if len(sys.argv) == 1:
    m = datetime.now().month
    y = datetime.now().year
elif len(sys.argv) == 2:
    if sys.argv[1].isdigit() and len(sys.argv[1]) == 2 and int(sys.argv[1]) < 13:
        m = sys.argv[1]
        y = datetime.now().year
    else:
        err
        exit()
elif len(sys.argv) == 3:
    if sys.argv[1].isdigit() and len(sys.argv[1]) == 2 and int(sys.argv[1]) <= 12 and sys.argv[2][1:5].isdigit() and len(sys.argv[2]) == 6:
        (m) = sys.argv[1]
        (y) = sys.argv[2][1:5]
    else:
        err
        exit()
else:
    err
    exit()
print(calendar.month(int(y), int(m)))
