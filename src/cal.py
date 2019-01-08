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
import datetime

current = datetime.datetime.now()
cal = calendar.TextCalendar()
arg = sys.argv

if (len(arg) == 3):
  print(cal.formatmonth(int(arg[2]), int(arg[1])))
else:
  print(cal.formatmonth(int(current.year), int(current.month)))

# elif (len(arg) == 2): #year
#   print(cal.pryear(int(arg[1])))
