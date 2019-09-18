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
import pytz
from pytz import timezone


# __________ M A I N ________________
#   accepts user input of the form
#    `14_cal.py month [year]`

if __name__ == '__main__':

    # get current time in pacific timezone
    pacific = timezone('US/Pacific')
    time = datetime.today().astimezone(pacific)
    year = time.year
    month = time.month

    weekday = time.isoweekday()
    dow = {1: 'MONDAY',
           2: 'TUESDAY',
           3: 'WEDNESDAY',
           4: 'THURSDAY',
           5: 'FRIDAY',
           6: 'SATURDAY',
           7: 'SUNDAY'}
    for key, value in dow.items():
        if key == weekday:
            weekday = value

    hour = time.hour

    # ___ instantiate calendar obj ____
    cal = calendar.TextCalendar(calendar.SUNDAY)

    # ___ find # arguments ____
    args = []
    for arg in sys.argv[1:]:
        args.append(arg)

    # ___ args == 0  --> current month/year cal
    if len(args) == 0:
        print(cal.formatmonth(year, month))

    if len(args) == 1:
        if int(args[0]) not in range(1, 13):
            print('Invalid Month specified. Enter a month between 1-12')
        else:
            print(cal.formatmonth(year, int(args[0])))
    if len(args) == 2:
        if int(args[0]) not in range(1, 13):
            print('Invalid Month specified. Enter a month between 1-12')
        else:
            if int(args[1]) not in range(1000, 6001):
                print('Invalid Year specified. Enter a year between 1000-6000')
            else:
                print(cal.formatmonth(int(args[1]), int(args[0])))
    if len(args) > 2:
        print('Too many parameters specified. Enter only month or year')
