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
from datetime import date
import sys

def printMonth(year, month):
    print (calendar.TextCalendar().prmonth(year,month))

print ("Argv is ", sys.argv)
arguments = sys.argv[1:]
print ("Changed Argv is ", arguments)

l = len(arguments)
if l == 0:
    #print this month and year cval
    year = date.today().year
    month = date.today().month
    printMonth(year, month)

elif l == 1:
    month = int(arguments[0])
    year = date.today().year
    printMonth(year, month)

    #print month of this year
elif l == 2:
    month, year = arguments
    printMonth(int(year),int(month))
else:
    print ("Invalid syntax : Usage 14_cal.py month [year]")


x= date(2019, 5, 17)
print(x)