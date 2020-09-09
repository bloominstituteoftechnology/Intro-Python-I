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

argumentCount = len(sys.argv) - 1 # ignore script name at [0]

today = datetime.today()

if argumentCount == 0:
    # print calendar for current month
    print(calendar.month(today.year, today.month))

if argumentCount == 1:
    # print calendar for specified month (in current year)
    monthArg = int(sys.argv[1])
    print(calendar.month(today.year, monthArg))

if argumentCount == 2:
    # print calendar for specified month and year
    monthArg = int(sys.argv[1])
    yearArg = int(sys.argv[2])
    print(calendar.month(yearArg, monthArg))

if argumentCount > 2:
    # print usage info
    output = "Usage:\n"
    output += "`14_cal.py [month] [year]`\n\n"
    output += "No arguments will output current month\n"
    output += "Single argument will output selected month, in current year\n"
    output += "Pass month and year to print any month of any year"
    print(output)