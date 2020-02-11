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

Note: the user should provide argument input
(in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument
is optional, as this is a common convention in documentation.

This would mean that from the command line you would call
`python3 14_cal.py 4 2015` to print out a calendar for April in 2015,
but if you omit either the year or both values,it should use today’s date to
get the month and year.
"""

import sys
import calendar
from datetime import datetime

inputU = input('Enter date: [MM] [YYYY]')


def cal(inputU):
    """split input"""
    a = inputU.split(' ')

    if len(inputU) == 0 or inputU.isspace():
        """Case 1: user don't give any information"""
        print("You don't specify any input \n")
        """Show today calendar"""
        print(calendar.month(datetime.now().year, datetime.now().month))
    elif len(a) is 1:
        """Case 2: user enter one parameter"""
        try:
            """Show calendar for the month given and current year"""
            print(calendar.month(datetime.now().year, int(inputU)))
        except:
            """The information given by the user is not valid"""
            print("\n Not a valid month")
    elif len(a) == 2:
        """Case 3: user enter two parameters"""
        try:
            """Show calendar for the month and year entered"""
            print('\n__Calendar__\n', calendar.month(
                                                     int(a[1]),
                                                     int(a[0])))
        except:
            """The information given by the user is not valid"""
            print("\nNot a valid month or year \n")
    else:
        """Case 4: user enter more information"""
        print("Input not valid \nTry again enter date: [month] [year]")

cal(inputU)
