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

def main():
    if len(sys.argv) == 1:
        # no inputs prints the current month of the current year
        month = datetime.today().month
        year = datetime.today().year

        print(calendar.month(year, month))

    elif len(sys.argv) == 2:
        #assume month is passed render calendar for that month current year
        #TODO this is a fragile mvp. Add exception handling
        month = datetime.strptime(sys.argv[1], '%m').month
        year = datetime.today().year

        print(calendar.month(year, month))

    elif len(sys.argv) == 3:
        # print month and year passed in by users
        #TODO this is fragile mvp. add exception handling
        month = datetime.strptime(sys.argv[1], '%m').month
        year = datetime.strptime(sys.argv[2], '%Y').year

        print(calendar.month(year, month))

    else:
        #TODO consider making this a call out to use -h or --help
        usage = '''Too many arguments, please consider the following usage:
14_cal.py - Display current month of current year
14_cal.py [month] - Display [month] of current year, eg 14_cal.py 12
14_cal.py [month] [year] - Display [month] of [year] eg 13_cal.py 12 1935'''
        print(usage)

if __name__ == "__main__":
    main()