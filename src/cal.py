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


def check_year(year):
    min_year = calendar.datetime.MINYEAR
    max_year = calendar.datetime.MAXYEAR

    return min_year <= int(year) <= max_year


def check_month(month):
    return 1 <= int(month) <= 12


def error_msg():
    return "Usage: cal.py [month=1..12] [year=1..9999]"


l = len(sys.argv)
now = datetime.now()

if l == 2:
    if check_month(sys.argv[1]):
        month = int(sys.argv[1])
        year = now.year
    else:
        sys.exit(error_msg())
elif l == 3:
    if check_month(sys.argv[1]) and check_year(sys.argv[2]):
        month = int(sys.argv[1])
        year = int(sys.argv[2])
    else:
        sys.exit(error_msg())
else:
    year = now.year
    month = now.month

tc = calendar.TextCalendar()
tc.prmonth(year, month)
