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
import calendar as cal
from datetime import datetime as dt

num_args = len(sys.argv)

if num_args == 1:
  print(cal.monthcalendar(dt.now().year, dt.now().month))
elif num_args == 2:
  print(cal.monthcalendar(dt.now().year, int(sys.argv[1])))
elif num_args == 3:
  print(cal.monthcalendar(int(sys.argv[2]), int(sys.argv[1])))
else:
  print("If no input: returns current month's calendar, if one arg is input: returns month calendar of current year, if two args input: return month calendar of year")