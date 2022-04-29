
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


def print_calendar(month=None, year=None):
    if month:
        try:
            month = int(month)
        except ValueError as e:
            return e
        except TypeError:
            return 'Enter a number'
    if year:
        try:
            year = int(year.strip('[]'))
        except ValueError as e:
            return e
        except TypeError:
            return 'Enter a number in brackets. i.e. "[5]"'

    if not month and not year:
        cal = calendar.TextCalendar()
        year = datetime.now().year
        month = datetime.now().month
        cal = cal.formatmonth(year, month)
        return cal

    if not year:
        cal = calendar.TextCalendar()
        year = datetime.now().year
        cal = cal.formatmonth(year, month)
        return cal

    else:
        cal = calendar.TextCalendar()
        cal = cal.formatmonth(year, month)
        return cal


if __name__ == "__main__":
    args = sys.argv[1:]
    month, year = None, None
    if args:
        if len(args) > 1:
            month = args[0]
            year = args[1]
        else:
            month = args[0]
    print(print_calendar(month, year))
