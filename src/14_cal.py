"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html
OR:
https://www.w3resource.com/python/module/calendar/ 

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

# We need to get the month and year
date = datetime.now()

month, year = date.month, date.year

# print(date, month, year)


calendar.setfirstweekday(calendar.SUNDAY) #Sets the first weekday to Sunday

# print(calendar.month(date.year, date.month))
if len(sys.argv) == 1:
  calendar.prmonth(date.year, date.month)

elif len(sys.argv) == 2:
  calendar.prmonth(date.year, int(sys.argv[1]))

elif len(sys.argv) == 3:
  calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]))

else:
  print('expected: filename month year')
  sys.exit(1)

def infoget(args):
  scrip, *args = sys.argv
  if not args:
    rend_cal()
  elif len(args) == 1:
    month = int(args[0])
    rend_cal(month)
  elif len(args) == 2:
    month = int(args[0])
    year = int(args[1])
    rend_cal(month, year)
  else:
    print(utilization())