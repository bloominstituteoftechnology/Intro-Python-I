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

def myCalendar(): 
  y = input("Input the year : ")
  if y:
    y = int(y)
    m = int(input("Input the month (using a number): "))
  else:
    print("\nCurrent calendar:")
    now = datetime.now()
    y = now.year
    m = now.month
  print("\n")
  print(calendar.month(y, m))
myCalendar()

# from datetime import datetime
# now = datetime.now()
# print(now) # 2018-12-21 22:07:31.859149
# current_year = now.year
# current_month = now.month