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

msg = input("Enter year(YYYY format) and month(MM format): ").split(" ")
print(msg)

def cal(*args):

  year = datetime.now().year
  month = datetime.now().month

  print(msg)
  if len(args) == 1:
    print(calendar.month(year, month))
  elif len(args) == 2:
    print(calendar.month(int(args[0]), int(args[1])))
  # elif len(args) == 3:
  #   print(calendar.month(int(args[0]), int(args[1])))
  else:
    print("Error: Input the YEAR(YYYY) format and MONTH(M or MM)")

cal(*msg)
