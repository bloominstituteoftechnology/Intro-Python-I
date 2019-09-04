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
from datetime import date

m = input("Input the month : ")
y = input("Input the year : ")

if(len(y) == 0 and len(m) == 0):
  today = date.today()
  print(calendar.month(today.year, today.month))
  print("You did not enter any data, so you got todays date")
elif(int(m) < 0 or int(m) > 12):
  today = date.today()
  print(calendar.month(today.year, today.month))
  print("You entered an invalid month, so you got todays date")
else:
  print(calendar.month(int(y), int(m)))



# else:
#   print(calendar.month(int(y), int(m)))
# if month < 0 or month > 12 then default to current calendar
# elif month len > 2 send an error message
# if(len(y) == 0 and len(m) == 0):

#   print(calendar(today.year, today.month))
# else:
#   print(calendar.month(y, m))
# print(calendar(today.year, today.month))