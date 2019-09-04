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
user_inp = input("Input?")

inp_array = user_inp.split(" ")

if user_inp == "":
    print(calendar.month(datetime.today().year, datetime.today().month))
elif not all(x.isdigit() for x in inp_array) or len(inp_array) > 2 or int(inp_array[0]) > 12:
    print("Input must be in the format of Month Year. (e.g. 4 2019)\nIf no input is given, current month and year are "
          "assumed.\nIf one input is given, input month of current year is assumed.")
elif len(inp_array) == 1:
    print(calendar.month(datetime.today().year, int(inp_array[0])))
else:
    print(calendar.month(int(inp_array[1]), int(inp_array[0])))