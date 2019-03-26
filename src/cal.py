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


month = input("Select a month: ")
year = input("What year is it: ")

if month == "" and year == "":
    month = datetime.today().strftime('%m')
    year = datetime.today().strftime('%Y')
    print(calendar.month(int(year), int(month)))
elif year == "" and month != None:
    if month.isdigit():
        year = datetime.today().strftime('%Y')
        print(calendar.month(int(year), int(month)))
    else:
        print('Month should be a number.')
elif month == "" and year != None:
    if year.isdigit():
        month = datetime.today().strftime('%m')
        print(calendar.month(int(year), int(month)))
    else:
        print('Year should be a number.')
else:
    if month.isdigit() and year.isdigit():
        print(calendar.month(int(year), int(month)))
    else:
        print('Month and Year should be Numbers.')
