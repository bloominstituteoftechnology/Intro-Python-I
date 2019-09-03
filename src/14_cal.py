"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
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
"""

import sys
import calendar
from datetime import datetime


# ____________ MAIN _______________
#  Accepts user input of the form 
#  "14_cal.py month [year]"

if __name__ == "__main__":

    month = datetime.now().month
    yr = datetime.now().year

    args = []
    for arg in sys.argv[1:]:
        args.append(int(arg))

    # ___ Assuming 1st value is month and 2nd is year

    if len(args) == 0:  
        print(calendar.TextCalendar().prmonth(yr, month))

    elif len(args) == 1:
        if args[0] not in range(1,13):
            print('Invalid month given. Please enter a value from 1 to 12.')
        else:
            month = args[0]
            print(calendar.TextCalendar().prmonth(yr, month))

    elif len(args) == 2:
      if args[0] not in range(1,13):
            print('Invalid month given. Please enter a value from 1 to 12.')
      if args[1] not in range(1500,3000):
            print('Invalid year given. Please enter a value from 1500 to 3000.')
      else:
            month = args[0]
            yr = args[1]
            print(calendar.TextCalendar().prmonth(yr, month))

