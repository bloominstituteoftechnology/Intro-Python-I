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

user_input = input('type month and year ')

li = user_input.split(' ')

date = datetime.now().strftime('%Y-%m')
dateli = date.split('-')
curcal = calendar.TextCalendar()

if len(li) == 1 and len(li[0]) == 0:                          - If no month provided by user
  print(curcal.formatmonth(int(dateli[0]), int(dateli[1]) ))  - Print current year and current month calendar
elif len(li) == 1 and len(li[0]) > 0:                         - If only month is provided
  print(curcal.formatmonth(int(dateli[0]), int(li[0]) ))      - Print current year and provided month calendar
elif len(li) == 2:                                            - if both month and year is provided
  print(curcal.formatmonth(int(li[1]), int(li[0]) ))          - print provided month and provided year calendar
else:
  print('Wrong format')
"""

import sys
import calendar
from datetime import datetime

import sys
import calendar
from datetime import datetime


if len(sys.argv) == 1 or len(sys.argv) > 3:
  print("Arguments should be given in the format: month [year]")
  exit()
a_month = int(sys.argv[1])
if len(sys.argv) == 3:
    a_year = int(sys.argv[2])
    print("\n")
    print(calendar.month(a_year, a_month))
elif len(sys.argv) == 2:
    print(calendar.month(datetime.now().year, a_month))
