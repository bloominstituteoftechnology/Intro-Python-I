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

today = datetime.now()
cal = calendar.TextCalendar(firstweekday=6)

# if (len(sys.argv) == 1):
#   cal.prmonth(today.year, today.month)
# elif (len(sys.argv) == 2):
#   cal.prmonth(today.year, int(sys.argv[1]))
# elif (len(sys.argv) == 3):
#   cal.prmonth(int(sys.argv[2]), int(sys.argv[1]))
# else:
#   print('Please format arguments in the following way: `14_cal.py month [year]`')

def user_input():
    print("This progam returns the month and year that is passed in. If month and year are left blank it returns the current month and year")
    month_input = input('What month? ')
    year_input = input("What year? ")
    if month_input == "":
        month_input = today.month
    if year_input == "":
        year_input = today.year
    print(f'{month_input} / {year_input}')


user_input()