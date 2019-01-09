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
from datetime import datetime

l = len(sys.argv) #sys.argv is command line arguments

if l == 1:
  #user passed in no args
  month = datetime.now().month
  year = datetime.now().year
elif l == 2:
  #user passed in month
  month = int(sys.argv[1]) #command line inputs usually come in as strings
  year = datetime.now().year
elif l == 3:
  #user passed in month and year
  month = int(sys.argv[1])
  year = int(sys.argv[2])
else:
  #faulty input
  print("usage: cal.py [month] [year]")
  sys.exit(1) #exit program

cal = calendar.TextCalendar() #use textcalendar module
cal.prmonth(year, month) #prmonth prints month and year. built-in method

