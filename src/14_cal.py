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

for arg in sys.argv:
    print(arg)

d = datetime(1989, 12, 1).today()


def calApp(month=d, year=d):
    global calendar
    print(calendar.TextCalendar().formatmonth(year, month))


try:
    user_entered = input(
        "Enter nothing, a month, or in order a month and year separated by comma: ").split(',')
    calApp(*[int(i) for i in user_entered if user_entered != ['']])

except:
    print("Enter nothing, a month, or both a month and year separated by comma in that order--do not enter more, or not integers")
