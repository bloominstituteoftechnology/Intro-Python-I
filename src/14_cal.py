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

def ck_mon(month):
    if month >= 1 and month <= 12:
        return True

    print("err: Month should be between 1 and 12\n")
    return False


def ck_year(year):
    if year >= MINYEAR and year <= MAXYEAR:
        return True

    print(f'err: Year should be between {MINYEAR} and '
          f'{MAXYEAR}\n')
    return False


def print_usage():
    print("Refer to below usage instructions.\n")
    print("Print calendar of current month:")
    print("python 14_cal.py\n")
    print("Print calendar for month within current year:")
    print("python 14_cal.py <month>\n")
    print("Print calendar for month and year:")
    print("python 14_cal.py <month> <year>")
    exit(1)


current_datetime = datetime.now()
year = current_datetime.year
month = current_datetime.month

if len(sys.argv) == 1:
    print("Printing current month\n")

elif len(sys.argv) == 2:
    if not ck_mon(int(sys.argv[1])):
        print_usage()

    month = int(sys.argv[1])

elif len(sys.argv) == 3:
    if not ck_mon(int(sys.argv[1])):
        print_usage()

    month = int(sys.argv[1])

    if not ck_year(int(sys.argv[2])):
        print_usage()

    year = int(sys.argv[2])
else:
    print_usage()


textCalendar = calendar.TextCalendar(firstweekday=0)
textCalendar.prmonth(year, month)