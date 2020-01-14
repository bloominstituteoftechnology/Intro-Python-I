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

def die(reason):
    print(reason)
    print("Usage: 14_cal.py [monthNoBrackets] [yearNoBrackets]")
    print('Note that year is optional - if omitted, will simply use the current year')
    exit()

month = 1
year = 1

def checkArgs():
    global month, year
    if len(sys.argv) > 3:
        die("Too many arguments")
    if len(sys.argv) > 1:
        try:
            month = int(sys.argv[1])
        except:
            die("Month must be an integer")
    if len(sys.argv) > 2:
        try:
            year = int(sys.argv[2])
        except:
            die("Year must be an integer")

    if month > 12 or month < 1:
        die("There are only 12 months!")


currentTime = datetime.today()
month = currentTime.month
year = currentTime.year
checkArgs()

if len(sys.argv) > 1:
    month = int(sys.argv[1])

if len(sys.argv) > 2:
    year = int(sys.argv[2])


mycal = calendar.TextCalendar()
mycal.firstweekday = 6
print(mycal.formatmonth(year, month))
