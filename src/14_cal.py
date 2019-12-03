import sys
import calendar
from datetime import datetime

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

args = sys.argv[1:]
today = datetime.today()


def display_calendar():
    if (
      len(args) == 2 and
      args[0].isdigit() and
      int(args[0]) > 0 and
      int(args[0]) <= 12 and
      args[1].isdigit()
      ):
        month = int(args[0])
        year = int(args[1])
        print(calendar.month(year, month))
    elif (
      len(args) == 1 and
      args[0].isdigit() and
      int(args[0]) > 0 and
      int(args[0]) <= 12
      ):
        month = int(args[0])
        year = today.year
        print(calendar.month(year, month))
    elif len(args) == 0:
        month = today.month
        year = today.year
        print(calendar.month(year, month))
    else:
        print(
          "display_calendar() expects no more than two arguments,"
          "the first an integer between 1 and 12 representing the month,"
          "the second if given an integer representing the year."
          )


display_calendar()
