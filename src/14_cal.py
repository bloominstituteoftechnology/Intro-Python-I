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
## set current month and year
currentMonth = datetime.today().month
currentYear = datetime.today().year

## create the calendar to display
calendar_create = calendar.TextCalendar(calendar.TUESDAY)
## no input from user
if len(sys.argv) == 1:
    print("Calendar created with current month!", calendar_create.formatmonth(currentYear, currentMonth))
## user inputs one argument, assume they meant month
elif len(sys.argv) == 2:
  try:
        month = int(sys.argv[1])
  except ValueError:
      print("Please enter an interger!")
  else:
    if int(sys.argv[1]) >= 12:
      print("Calendar Created with 1 arg!", calendar_create.formatmonth(currentYear, month))
      ## if user enters int > 13
    else:
      print("Enter interger lower than 13!")
elif len(sys.argv) == 3:
  try:
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    print(calendar_create.formatmonth(year, month))
  except ValueError:
    print("Please input for month and year")
else:
  print("Opps....something is broken")