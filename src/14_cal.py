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

# for arg in sys.argv:
#   print(arg)

cal = calendar.TextCalendar()

# function to print the calendar month defaults are the current month/year
def printCal(month = datetime.today().month, year = datetime.today().year):
  # check to see if month passed in is valid
  if (month < 1 or month > 12):
    print("Enter a valid month between 1-12")
    return
  # check to see if the year is valid
  elif (year < 1 or year > 9999):
    print("Enter a valid year between 1-9999")
    return
  cal.prmonth(year, month)

# check to see if the arguments are passed in
if (len(sys.argv) > 1 and len(sys.argv) < 4):
  month = int(sys.argv[1])
  # check to see if there are 2 arguments or not
  if (len(sys.argv) != 3):
      # print only the month
      printCal(month)
  else:
    # get the year value and print year and month
    year = int(sys.argv[2])
    printCal(month, year)
else:
  # print this months calender
  printCal()