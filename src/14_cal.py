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


# datetime expects an int
# .Calendar(firstweekday=0)

# note: check argv, and others
lenargv = len(sys.argv)

# - if no input
#     default to today's date. print method datetime.now().month and another with year
# - elif one input,
#     it's going to be the month and we're going to use the current year
# - elif two inputs,
#     the first will be the month, 2nd will be the year. will use those for the calendar.
# - else more than two inputs,
#     send error msg

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