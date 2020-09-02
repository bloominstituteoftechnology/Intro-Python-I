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

calendar.setfirstweekday(6)

m = datetime.now().month
y = datetime.now().year
inputexample = f'Input should be a numerical month and year, example: {m} {y}'



#sets default value current date
calInput = {"month": m, "year": y}

# checks sys.argv for argv amount to change calInput accordingly
if len(sys.argv)>2:
  calInput = {"month": sys.argv[1], "year": sys.argv[2]}
else:
  if len(sys.argv)>1:
    calInput = {"month": sys.argv[1], "year": y}

# checks for both year and month input
if calInput["month"] != '' and calInput["year"] != '':
    #checks if month in a number
    try:
        int(calInput["month"])
    except ValueError:
        print(inputexample)
        sys.exit()
    #checks if month in a real month
    if int(calInput["month"]) not in range(1, 13):
        print(inputexample)
        sys.exit()
    else:
        m = int(calInput["month"])
    #checks for year
    if len(calInput) > 1:
        #checks if year is a number
        try:
            int(calInput["year"])
        except ValueError:
            print(inputexample)
            sys.exit()
        #sets year to input year
        y = int(calInput["year"])

print( calendar.month(y, m))