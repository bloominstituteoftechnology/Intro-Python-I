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
from datetime import datetime, date, time

# def todays_date():
#   print(datetime.date(month, year))

month = input("enter month:")

month = int(month)
year = input("enter year: ")
year = int(year)
day = input("enter day: ")
day = int(day)

date = datetime.date.now()
# today = date.today()
#empty = input("")
#empty = int(empty)

# def validate_date(d):
#     try:
#         if len(d) == 10: 
#             datetime.strptime(d, '%m/%d/%Y')
#             return True
#         else: return False

#     except ValueError:
#         return False

# print(validate_date('2/26/1000'))






if input == month or year:
  print(datetime.date(year, month, day))
elif input == month and year:
  print(f"the month is: {month} and the year is: {year}")
elif input == "":
  print(date)
else:
  print("please enter a month or year")

