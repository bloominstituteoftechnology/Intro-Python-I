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
from colorama import Fore
from colorama import Style


def print_calendar():

    today = datetime.today()
    args = sys.argv

    my_calendar = calendar.TextCalendar()

    month = today.month
    year = today.year

    try:
        if len(args) == 1:
            month = today.month
            year = today.year

        elif len(args) == 2:
            month = int(args[1])
            year = today.year

            if month < 1 or month > 12:
                print(
                    f"{Fore.RED}Month value must be between [1 - 12].{Style.RESET_ALL}")
                return

        elif len(args) > 2:
            month = int(args[1])
            year = int(args[2])

    except ValueError:
        print(
            f"{Fore.RED}To view specific month's calendar, run the file with [month] and [year] parameters.{Style.RESET_ALL}")
        return

    print(my_calendar.formatmonth(year, month))


print_calendar()

# def print_calendar(year=today.year, month=today.month):

#     day = today.day

#     my_calendar = calendar.TextCalendar()

#     my_cal = ''
#     for item in my_calendar.itermonthdays4(year, month):
#         # item = (YYYY, M, DD, Day of week 0-6)

#         my_day = ' ' + str(item[2])
#         if item[1] != month:
#             my_day = f'{Fore.BLACK}{my_day}{Style.RESET_ALL}'
#         if len(str(item[2])) == 1:
#             my_day = '  ' + str(item[2])
#         if item[2] == day:
#             my_day = f'{Fore.GREEN}{my_day}{Style.RESET_ALL}'
#         my_cal = my_cal + my_day
#         if item[3] == 6:
#             my_cal = my_cal + '\n'

#     print(my_cal)


# print_calendar()
