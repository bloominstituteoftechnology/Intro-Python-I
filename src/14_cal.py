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

def cal():
  if len(sys.argv) == 1:
    d = datetime.now()
    cal = calendar.monthcalendar(d.year, d.month)
    render_cal(cal)

  if len(sys.argv) == 2:
    month = sys.argv[1]
    if not validate(month):
      err()
      return
    d = datetime.now()
    cal = calendar.monthcalendar(d.year, int(month))
    render_cal(cal)

  if len(sys.argv) == 3:
    month = sys.argv[1]
    year = sys.argv[2]
    if not validate(month, year):
      err()
      return
    cal = calendar.monthcalendar(int(year), int(month))
    render_cal(cal)

def validate(month, year = False):
  v = True
  if month:
    if month.isdigit() and 1 <= int(month) <= 12:
      v = True
    else:
      v = False

  if year:
    if v == False:
      return v
    if year.isdigit() and 1970 <= int(year) <= 2100:
      v = True
    else:
      v = False
  return v

def render_cal(cal):
  for d in cal:
    s = ""
    for w in d:
      s += str(w) + " "
    print(s)

def err():
  print(" ")
  print("Please specify correct format => \nint:Month = 1(Janurary) - 12(December) \nint:Year = 1970 - 2100 \nEx. \"14_cal.py 12 2019\"")
  print(" ")

cal()
