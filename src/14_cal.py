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
from calendar import TextCalendar
from datetime import datetime

current_year = datetime.now().year
cal_input = input("Please input year and month (XXXX XX): ").strip().split(" ")

if len(cal_input) < 2 and len(cal_input) > 0:
    TextCalendar().prmonth(current_year, int(cal_input[0]))
else:
    TextCalendar().prmonth(int(cal_input[0]), int(cal_input[1]))
print(current_year)
print(cal_input)








