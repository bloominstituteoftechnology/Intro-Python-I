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

args = len(sys.argv[1:])
month = datetime.today().month
year = datetime.today().year


def month_check(month):
    if month > 12 or month == 0:
        return -1
    else:
        return 1


def year_check(year):
    if len(str(year)) == 4:
        return 1
    else:
        return -1


if args == 1:
    month = int(sys.argv[1])
    if month_check(month) == -1:
        print("please enter a valid month")
    else:
        print(calendar.TextCalendar().formatmonth(year, month))
elif args == 2:
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    if month_check(month) == -1 or year_check(year) == -1:
        print("please enter a valid month and year")
    else:
        print(calendar.TextCalendar().formatmonth(year, month))
elif args == 0:
    print(calendar.TextCalendar().formatmonth(year, month))
else:
    print("Please format your arguments like this: cal.py 11 1985")
