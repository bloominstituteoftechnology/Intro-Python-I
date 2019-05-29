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
from datetime import datetime, MINYEAR, MAXYEAR

if len(sys.argv) == 1:
  print(datetime.now())

if len(sys.argv) == 2:
  month = sys.argv[1]
  if int(month) < 1 or int(month) > 12:
    print('Month must be between 1-12')
  else:
    calendar.TextCalendar.prmonth(datetime.now().year, month)

if len(sys.argv) == 3:
  month = sys.argv[1]
  year = sys.argv[2]
  if int(month) < 1 or int(month) > 12 or int(year) < MINYEAR or int(year) > MAXYEAR:
    print(f'Month must be between 1-12 & Year must be between {MINYEAR}-{MAXYEAR}')
  else:
    print(calendar.TextCalendar.prmonth(year, month))