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

def print_calendar(month, year):
  if 1 <= month and month <=  12:
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(theyear = year, themonth = month)
  else:
    sys.exit("Invalid month")

args = sys.argv

month = datetime.today().month
year = datetime.today().year

if len(args) == 1:
  print_calendar(month, year)
elif len(args) == 2 :
  month = int(args[1])
  print_calendar(month, year)
elif len(args) == 3:
  month = int(args[1])
  year = int(args[2])
  print_calendar(month, year)
else:
  sys.exit("Wrong number of args")