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

# From lecture:

# Read out arguments

args = sys.argv
print(f"args: {args}")

# If no args supploed...
# Print a text calednar for current month and year
# If 1 arg is supploed...
# Check if it's an int 1-12, print oout cal for that month, current year
# If 2 args are supplied...
# Check if 1 is int 1-12, check if 2 is an int
# Print out calendar for that month and year
# Otherwise, print an error with usage hint

date = datetime.today()
mm = date.month
yy = date.year

if len(args) == 1:
    # month = datetime.today().month
    # year = datetime.today().year
    # calendar.prmonth(year, month)
    pass
elif len(args) == 2:
    mm = int(args[1])
    # year = datetime.today().year
    # calendar.prmonth(year, month)
elif len(args) == 3:
    mm = int(args[1])
    yy = int(args[2])
    # calendar.prmonth(year, month)
else:
    print("something has gone terribly wrong. try again!")
    exit()

calendar.prmonth(yy, mm)


# My incorrect way:

# date = datetime.today()


# def cal(mm, yy):
#     if mm == "":
#         mm = date.month
#     else:
#         mm = int(mm)
#     if yy == "":
#         yy = date.month
#     else:
#         yy = int(yy)

#     print(calendar.month(yy, mm))


# mm = input("Enter Month (1 - 12): ")
# yy = input("Enter year (yyyy): ")

# cal(mm, yy)
