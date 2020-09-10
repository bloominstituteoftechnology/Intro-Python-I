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

print("We can do it like this: ")

# num_args = len(sys.argv) - 1

# if num_args > 2:
#   print("Usage: 14_cal.py [month] [year]\n\n14_cal.py: error: too many arguments")
#   sys.exit()

#   mm = int(sys.argv[1]) if num_args > 0 else datetime.today().month
#   yy = int(sys.argv[2]) if num_args > 1 else datetime.today().year

#   print(calendar.month(yy, mm))

print("Or we can do it like this too =================================")

# Fetch command line arguments for this program:
num_args = len(sys.argv)

# User didn't pass in any arguments:
if num_args == 1:
  # get the current month and year:
  month = datetime.now().month
  year = datetime.now().year
  # Render the cal for that

  # User passed in one argument:
elif num_args == 2:
    # Assume the arg is the specified month
    # Render the cal for that month of the current year
    year = datetime.now().year
    month = int(sys.argv[1])  #index 0 is always the name of the program. NOt what we want right now.

# User passed in 2 arguments
elif num_args == 3:
  # Render the cal for the specified month and specified year.
  month = int(sys.argv[1])
  year = int(sys.argv[2])

# User passed in some other number of arguments:
else:
  # Print a usage statement 
  print("Usage: 14_cal.py [month] [year]")

  # exit the program
  sys.exit(1)  # 1 means that something incorrect happened in the program.

cal = calendar.TextCalendar()
cal.prmonth(year, month)

  # In order to try this we I have to enter this: /usr/local/bin/python3 "/Users/christianlorenzo/Library/Mobile Documents/com~apple~CloudDocs/Python Development/Intro-Python-I/src/14_cal.py"
  # And then leave a space and then enter the number for the month that I'm interested in printing out, or the number for the month and the year

