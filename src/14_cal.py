"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
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

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# print(calendar.weekheader(3))
# print(calendar.firstweekday())
# print()

# print(calendar.month(2020, 7))

# print(calendar.monthcalendar(2020, 7))
# print(calendar.calendar(2020))

# day_of_the_week = calendar.weekday(2020, 7, 3)
# print(day_of_the_week)

# is_leap = calendar.isleap(1492)
# print(is_leap)
months = {v: k for k, v in enumerate(calendar.month_name)}
print(months)
now = datetime.now()
# print(now)
def calendar_page(year= now.year, month= now.month):
    print(calendar.month(year, month))


calendar_page()
calendar_page(1776, months["July"])
