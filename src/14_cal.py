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

def date_program():
    cal = calendar.TextCalendar()
    month = 0
    year = 0

    input_date = input('Enter the numeric values of the month and year separated by commas: ').split(', ')

    if len(input_date) == 2:
        if input_date[0].isdigit() and input_date[1].isdigit():
            print(cal.formatmonth(int(input_date[1]), int(input_date[0])))
            return
        else:
            invalid_input(46)
    elif len(input_date) == 1:
        now = datetime.now()
        if input_date != ['']:
            if input_date[0].isdigit():
                print(cal.formatmonth(now.year, int(input_date[0])))
                return
            else:
                invalid_input()
        elif input_date == ['']:
            print(cal.formatmonth(now.year, now.month))
            return
        else:
            print(f'input date is {input_date}')
            invalid_input(53)
    else:
        invalid_input(59)

def invalid_input(line):
    print(f'This is not the correct format, please type in month and year like so: 8, 2019 (on line {line})')
    date_program()

date_program()
