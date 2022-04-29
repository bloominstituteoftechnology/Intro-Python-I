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

def month_year(month, year):
  cal = calendar.TextCalendar()
  print(cal.formatmonth(year, month)) 

print(sys.argv)
print("If you want to call the calendar for specific month and year, you should add that to the initial call to run the file. For example: 'python 14_cal.py month year'. The year is optional")

if(len(sys.argv) == 1):
  month_year(month = int(datetime.now().month), year = int(datetime.now().year))
elif(len(sys.argv) == 2):
  month_year(month = int(sys.argv[1]), year = int(datetime.now().year))
elif(len(sys.argv) == 3):
  month_year(month = int(sys.argv[1]), year = int(sys.argv[2]))