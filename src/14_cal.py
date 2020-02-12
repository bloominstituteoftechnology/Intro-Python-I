#!/usr/bin/env python3
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

# Get arguments
args = sys.argv

today = datetime.now()
current_month = today.month
current_year = today.year
time = today.time()

tc = calendar.TextCalendar(calendar.SUNDAY)
# text_cal_str = tc.formatmonth(current_year, current_month) # Fix this to take user input

# Ask for user input for the month and year
# Check if user input is empty -> If it is, default to current month and year
    # print(current_month)
# If only 1 argument is given, assume it's the month
    # Print calendar for the month given by the user and the current year
# If both arguments are given, print calendar for month and year given by the user

if len(args) == 1:
    # Print current month and year calendar
    tc.prmonth(current_year, current_month)
elif len(args) == 2:
    # Assume user entered month
    month_input = int(args[1])
    tc.prmonth(current_year, month_input)
elif len(args) == 3:
    # Print calendar to match user input
    month_input = int(args[1])
    year_input = int(args[2])
    tc.prmonth(year_input, month_input)
else:
    print("That format isn't recognized. Exmaple: '14__cal.py month year'")