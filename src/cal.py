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
import datetime

year = datetime.date.today().year
month = datetime.date.today().month

if len(sys.argv) == 1:
  print(calendar.month(year, month))
elif len(sys.argv) == 2:
  print(calendar.month(2019, int(sys.argv[1])))
elif len(sys.argv) == 3:
  print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
else:
  print("Please use this program like so: python cal.py [month(as a number)] [year]")