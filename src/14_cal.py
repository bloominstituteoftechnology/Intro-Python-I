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

import calendar
import sys
from datetime import date, datetime

date_input = sys.argv[1:len(sys.argv)]
todays_date = date.today()

if len(date_input) == 0:
    # Print calendar for current month
    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(todays_date.year, todays_date.month)
    print(str)
elif len(date_input) == 1:
    # Print that month for current year
    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(todays_date.year, int(date_input[0]))
    print(str)
elif len(date_input) == 2:
    # Print the calendar for that month and year specified
    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(int(date_input[1]), int(date_input[0]))
    print(str)
