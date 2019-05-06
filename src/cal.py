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

input = input("Please enter a month and year (example: 8 2019):").split(' ')
now = datetime.now()
if len(input) == 1 and input[0]== ' ':
  
  calendar = calendar.TextCalendar()
  calendar.prmonth(now.year, now.month)

elif len(input) == 1 and int(input[0]) <= 12 and int(input[0]) > 0:
  month = int(input[0])
  print(month)
  calendar = calendar.TextCalendar()
  calendar.prmonth(now.year, month)

elif len(input) == 2:
  month = int(input[0])
  year = int(input[1])
  calendar = calendar.TextCalendar()
  calendar.prmonth(year, month)
else:
  print('Please enter a month and year (example: 9 2019)')

