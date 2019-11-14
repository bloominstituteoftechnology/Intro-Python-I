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
from datetime import date

sysArgLen = len(sys.argv)

dt_year, dt_month, _ = str(date.today()).split("-")

def cal(year, month):
    return calendar.month(int(year), int(month))

if(sysArgLen == 1):
    print(cal(dt_year, dt_month))
elif(sysArgLen == 2):
    month = sys.argv[1]
    print(cal(dt_year, month))
elif(sysArgLen == 3):
    month = sys.argv[1]
    year = sys.argv[2]
    print(cal(year, month))
else:
    print("Please include 1 or 2 arguments!")
