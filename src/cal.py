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

arg_len = len(sys.argv)

if arg_len == 1:
    print(datetime.today().strftime("%m"))
elif arg_len == 2:
    print(calendar.month(datetime.today().year, int(sys.argv[1])))
elif arg_len == 3:
    print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
else:
    print("Please provide valid arguments")