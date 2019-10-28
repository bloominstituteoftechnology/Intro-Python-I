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

today = datetime.now()
cal = calendar.TextCalendar(firstweekday=0)

if len(sys.argv) > 3:
    print('Please provide input in the format of "14_cal.py [month] [year]".\nMonth needs to be between 1 and 12.\nYear is optional')
else:
    if len(sys.argv) == 0:
        print(cal.formatmonth(today.year, today.month))
    elif len(sys.argv) > 1:
        month = int(sys.argv[1])
        if month >= 1 and month <= 12:
            if len(sys.argv) > 3:
                year = int(sys.argv[2])
            else:
                year = today.year
            print(cal.formatmonth(year, month))
        else:
            print('Month needs to be between 1 and 12')

    






