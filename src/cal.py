"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 -[x] If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 -[x] If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 -[x] If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

print(len(sys.argv))
print( sys.argv[0])

d = datetime.now()
cal = calendar.TextCalendar()

if len(sys.argv) == 1 :
  m = d.month
  y = d.year

elif len(sys.argv) == 2:
  m = int(sys.argv[1])
  y = d.year

elif len(sys.argv) == 3:
  m = int(sys.argv[1])
  y = int(sys.argv[2])

else:
  format_err
  exit()
  
print(calendar.month(y, m))
