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

argument = sys.argv
argumentLength = len(sys.argv)

print(argumentLength)
if argumentLength == 1:
  month = datetime.now().date().month
  year = datetime.now().date().year

elif argumentLength == 2:
  month = int(argument[1])
  year = datetime.now().date.year

elif argumentLength == 3:
  month = int(argument[1])
  year = int(argument[2])

else:
  print("To get calendar of the current month and year, don't pass in any arguments.\nTo get calendar of a specific month of this year, enter the month.\nTo get the calendar of a specific month of a specific year, enter the motnh and year.")

print(calendar.TextCalendar().formatmonth(2019, 10))  