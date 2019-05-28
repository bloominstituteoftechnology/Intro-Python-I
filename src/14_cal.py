"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
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
from datetime import MINYEAR, MAXYEAR


def check_month(month):
    if month >= 1 and month <= 12:
        return True

    print("ERROR: Month out of bound. Should be between 1 and 12\n")
    return False


def check_year(year):
    if year >= MINYEAR and year <= MAXYEAR:
        return True

    print(f'ERROR: Year out of bound. Should be between {MINYEAR} and '
          f'{MAXYEAR}\n')
    return False


def print_usage():
    print("Refer to below usage instructions.\n")
    print("To print calendar of current month")
    print("python 14_cal.py\n")
    print("To print calendar for specified month within current year")
    print("python 14_cal.py <month>\n")
    print("To print calendar for specified month and year")
    print("python 14_cal.py <month> <year>")
    exit(1)


current_datetime = datetime.now()
year = current_datetime.year
month = current_datetime.month

if len(sys.argv) == 1:
    print("Printing Calendar for current month\n")

elif len(sys.argv) == 2:
    # Check if month is within the range
    if not check_month(int(sys.argv[1])):
        print_usage()

    month = int(sys.argv[1])

elif len(sys.argv) == 3:
    # Check if month is within the range
    if not check_month(int(sys.argv[1])):
        print_usage()

    month = int(sys.argv[1])

    # Check if year is within the range
    if not check_year(int(sys.argv[2])):
        print_usage()

    year = int(sys.argv[2])
else:
    print_usage()


textCalendar = calendar.TextCalendar(firstweekday=0)
textCalendar.prmonth(year, month)
