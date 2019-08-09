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

args = sys.argv

month = datetime.today().month
year = datetime.today().year

print(args)

if len(args) == 2:
    try:
        args[1] = int(args[1])
    except ValueError:
        args[1] = 0

if len(args) == 3:
    try:
        args[2] = int(args[2])
    except ValueError:
        args[2] = 0

if len(args) == 1:
    calendar.TextCalendar().prmonth(year, month)
elif len(args) == 2 and int(args[1]) > 0 and int(args[1]) <= 12:
    month = int(args[1])
    calendar.TextCalendar().prmonth(year, month)
elif len(args) == 2 and int(args[1]) <= 0 or int(args[1]) > 12:
    print("Second argument should be a number greater than 0 and less than or equal to 12")
elif len(args) == 3 and int(args[1]) > 0 and int(args[1]) <= 12 and int(args[2]) == 4:
    month = int(args[1])
    year = int(args[2])
    calendar.TextCalendar().prmonth(year, month)
elif len(args) == 3 and int(args[1]) <= 0 or int(args[1]) > 12 or int(args[2]) != 2:
    print("Second argument should be greater than 0 and less than or equal to 12")
    print("Third argument should be 4 digits long")
else:
    print("Error must have a format [month] [year]")
