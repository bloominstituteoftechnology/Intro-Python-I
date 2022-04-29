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

args = sys.argv[1:]
count = len(sys.argv[1:])

# Figuring out how to write this logic in python took a little longer than I'd like to admit lol
if count > 2 or not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("py 14_cal.py [month] [year] ###USE NUMBERS")
    sys.exit()

# I'll assume user is playing fair past this point (aka,
# no 3 digit month or year shorter/longer than 4 digits)
thisMonth = int(sys.argv[1]) if count <= 2 else datetime.now().month
thisYear = int(sys.argv[2]) if count == 2 else datetime.now().year

print(calendar.month(thisYear, thisMonth))