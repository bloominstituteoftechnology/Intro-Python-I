import sys
from datetime import datetime
import calendar as C

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


def calendar(month=None, year=None,  *argv, **keywords):
    c = C.TextCalendar(C.SUNDAY)
    d = datetime.now()
    # print(help(d))
    if (month == None and year != None) or (len(argv) > 0) or (len(keywords) > 0) or \
        (month != None and type(month) != int) or (year != None and type(year) != int) or \
            (type(month) == int and month < 1) or (type(month) == int and month > 12):
        print('args: int month, [int year]')
    elif month == None and year == None:
        c.prmonth(d.year, d.month)
    elif month != None and year == None:
        c.prmonth(d.year, month)
    else:  # month != None and year !=None:
        assert month != None and year != None, 'program logic error'
        c.prmonth(year, month)


calendar()
calendar(6)
calendar(7, 2020)
calendar(year=2021)
calendar("5")
