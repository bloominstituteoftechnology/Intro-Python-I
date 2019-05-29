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
from calendar import TextCalendar
from datetime import datetime

f = input(
    '\n\nplease enter comma seperated numbers like this MM,YYYY or MM\n\n--> ').split(',')


def filtered_input(g):
    for i in g:
        try:
            isinstance(int(i), int)
        except ValueError:
            g.remove(i)
            filtered_input(g)
    try:
        if len(f) == 2:
            if len(f[1]) == 4 and (len(f[0]) == 2 or len(f[0]) == 1):
                print(TextCalendar().prmonth(int(f[1]), int(f[0])))
            else:
                raise Exception('here')
        elif len(f) == 1 and (len(f[0]) == 1 or len(f[0]) == 2):
            today = datetime.today()
            print(TextCalendar().prmonth(int(today.year), int(f[0])))
        else:
            raise Exception('aqui')
    except Exception as error:
        print(error)
        # print('please input date data seperated by a comma like this MM,YYYY or MM')


filtered_input(f)
