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

date = datetime.now()

cmd = input("Enter a number between 1-12 then add a space \
  and enter a year in YYYY format: ")
cmd = cmd.split()

if len(cmd) == 0:
    print(calendar.month(date.year, date.month))
elif len(cmd) == 1 and (int(cmd[0]) <= 12):
    month = int(cmd[0])
    print(calendar.month(date.year, month))
elif len(cmd) == 2 and (int(cmd[0]) <= 12) and (len(cmd[1]) == 4):
    month, year = (int(x) for x in cmd)
    print(calendar.month(year, month))
else:
    print('For the first number, please enter the month in a number from 1 - 12 format\
      and the year in YYYY format as the second number.')
