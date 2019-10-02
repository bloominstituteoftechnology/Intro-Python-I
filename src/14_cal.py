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

print('this should show on the consol')
# print(f'this is {sys.argv}')
arguments = sys.argv
arg_len = len(arguments)

if arg_len == 3:
  year = int(arguments[2])
  month = int(arguments[1])

if arg_len == 2:
  month = int(arguments[1])
  year = datetime.now().date().year

if arg_len == 1:
  month = datetime.now().date().month
  year = datetime.now().date().year


cal = calendar.TextCalendar()
print(cal.formatmonth(year, month))
