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

# Get length of command line arguments
arg_length = len(sys.argv)

# if length is more than 3, block execution and warn user
if arg_length > 3:
  print("Exessive number of arguments passed in, \n expected 2 arguments representing the desired day and year as numeric values")
  sys.exit()
# if inputed arguments are equal to 3 we assume those are numbers and pass them to the
# calendar module and get the month and year based on the arguments
elif arg_length == 3:
  print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
# if inputed arguments are equal to 2, that means no year has been specified, therefore
# we show the month specified by the user of the current year
elif arg_length == 2:
  print(calendar.month(datetime.now().year, int(sys.argv[1])))
# if no arguments have been provided, then we showcase the current month and year
else:
  print(calendar.month(datetime.now().year, datetime.now().month))