"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
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

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime
x= input("Please enter a month then year in format MM/YYYY: ").split("/")
print(x)

if(len(x) == 0):
  xmonth = 8
  xyear = 2020
elif(len(x) ==1):
  xmonth = x[0]
  xyear = 2020
else:
  xmonth = x[0]
  xyear = x[1]
def outputDate(year=2020, month=8):
  today = calendar.Calendar(firstweekday=0)
  print(today.monthdatescalendar(year=year, month=month))

if(xmonth == "" and xyear == ""):
  outputDate(year=2020, month=8)
elif(xmonth == "" or xyear == ""):
  if(xmonth==""):
    outputDate(year = int(xyear), month=int(8))
  else:
    outputDate(year = int(2020), month=int(xmonth))
else:
  outputDate(year = int(xyear), month=int(xmonth))