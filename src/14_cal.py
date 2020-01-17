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
from datetime import datetime as date

# sys.argv

#Default arguments
#Functions
#User input

# #Create function with argument for string which then splits the string into
# # by whitespace and checks to see how many pieces are in the list, then
# # reads the strings as:
# # A) Filename, B) Month, and/or C) Year
# # The function then feeds these into an I/O read, a month input and a year
# # input if available. If the string does not contain a 3rd 'token' i.e. year,
# # the year will default to the current year.

def dates(string):
    x = string.split(' ')
    print(x)
    if x[0] == '14_cal.py':
        print(len(x))
        if len(x) == 2:
            month = x[1]
            if len(month) == 2:
                month_split = [int(d) for d in str(month)]
                print(month_split)
                if month_split[0] == 0:
                    if len(month_split) == 2:
                        month = [str(d) for d in month_split]
                        month = int(month[0] + month[1])
                        year = date.now().year
                        print(calendar.prmonth(year, month))
                    if len(month_split) == 1:
                        month = month_split[0]
                        year = date.now().year
                        print(calendar.prmonth(year, month))
                else:
                    month = [str(d) for d in month_split]
                    month = int(month[0] + month[1])
                    year = date.now().year
                    print(calendar.prmonth(year, month))
        if len(x) == 3:
            month = x[1]
            year = int(x[2])
            if len(month) == 2:
                month_split = [int(d) for d in str(month)]
                print(month_split)
                if month_split[0] == 0:
                    if len(month_split) == 2:
                        month = [str(d) for d in month_split]
                        month = int(month[0] + month[1])
                        print(calendar.prmonth(year, month))
                    if len(month_split) == 1:
                        month = month_split[0]
                        print(calendar.prmonth(year, month))
                else:
                    month = [str(d) for d in month_split]
                    month = int(month[0] + month[1])
                    print(calendar.prmonth(year, month))
    else:
        print('Please enter the proper format (HINT: ONLY 1 FILE'
              ' CAN BE SEARCHED AND ITS NAME IS 14_cal.py')


#User must enter 14_cal.py, month, and year separated by single spacing
user_input = input('Enter the filename followed by the month and the year; '
                   'separate each of the previous 3 items with a single space:')

dates(user_input)


