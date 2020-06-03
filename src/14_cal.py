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

#how to accept input from the command line when running the file?

import sys
from datetime import datetime


month_list = ('January', 'February', 'March',
              'April', 'May', 'June', 'July',
              'August', 'September', 'October',
              'November', 'December')

year_list = range(1000,3000,1)

month = str(sys.argv[1][1:-1])

if month not in month_list:

    raise ValueError('Please input values in the following format: [Full Month Name] [Year]')

print("-----------------")

try:
    year = int(sys.argv[2][1:-1])
except IndexError:
    year = None

if year not in year_list:
    raise ValueError('Please input values in the following format: [Full Month Name] [Year]')

print(year)
print(month)


datetime_object = datetime.strptime(month, "%B")

month = datetime_object.month

import calendar

current_month = datetime.now().month
current_year = datetime.now().year

# if the user specifies one argument assume its a month and render the calendar
# for that month of the current year.

if year == None:
    c = calendar.TextCalendar(calendar.SUNDAY)
    rc = c.formatmonth(current_year, month)
    print("Calendar")
    print(rc)

# if the user specifies two arguments render the calendar for that month and year.

if year != None:
    c = calendar.TextCalendar(calendar.SUNDAY)
    rc = c.formatmonth(year, month)
    print("Calendar for month of current year")
    print(rc)

# otherwise print statement of expected format.
