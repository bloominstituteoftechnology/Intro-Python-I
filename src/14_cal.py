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

# default_month = datetime.today().month
# default_year = datetime.today().year
# def date(*nums):
#   if len(nums) == 2:
#     mm = int(nums[0])
#     yy = int(nums[1])
#     print(calendar.month(yy, mm))
#   elif len(nums) == 1:
#     mm = int(nums[0])
#     print(calendar.month(default_year, mm))
#   else: 
#     print(calendar.month(default_year, default_month))
# if len(sys.argv) == 3:
#   date(sys.argv[1], sys.argv[2])
# elif len(sys.argv) == 2:
#   date(sys.argv[1])
# else:
#   date()




#receive user input as agrument input(not using the input function)
num_args = len(sys.argv)

#init instance of the text calendar class
cal = calendar.TextCalendar()

month = datetime.now().month
year = datetime.now().year
  # if user specified no args: print current month and year
if num_args == 1:
  # month = datetime.now().month
  # year = datetime.now().year
 # cal.prmonth(year, month)
  pass
  # if user specified one arg: assume that arg is the month, print that month of the current year
elif num_args == 2:
  month = int(sys.argv[1])
  # year = datetime.now().year
  #cal.prmonth(year, month)
  # if user specified two args: print that month and year
elif num_args == 3:
  month = int(sys.argv[1])
  year = int(sys.argv[2])
  
 
  #otherwise print a usage in args
else:
  print('usage: cal.py [month] [year]')
  sys.exit(1)

cal.prmonth(year, month)

  






