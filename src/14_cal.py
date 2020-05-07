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

""" current_cal = calendar.month(2020, 5)
user_input = None
month = None
year = None

def curr_cal(*args):
   print(args[1]) 

def get_user_input():
    global user_input
    user_input  = [int(x) for x in input("14_cal.py [month] [year] ").split()] 
    print('this is user_input', user_input)
    if 2 < len(user_input) > 0:
        global month, year
        month = user_input[0]
        year= user_input[1]
        print('month is ' + str(month) + ' year is ' + str(year))
    else:
      print('NOPE')

        

def calendar_program():
    get_user_input()
    print(user_input)
    if len(user_input) == 0:
      #print calendar for current month
      print('current month')
      print(current_cal)
    elif len(user_input) == 1:
      month = (user_input[0])
      print(calendar.month(2020, month))
    elif len(user_input) == 2:
      month = (user_input[0])
      year = (user_input[1])
      print(calendar.month(year, month))
    else:
      print('the format that your program expects arguments to be given')

calendar_program()  """

###Variables

##Gives a list from user_input
#sys.argv
arg_count = len(sys.argv)

month = datetime.now().month
year = datetime.now().year

#[cal.py, month, year]

#If args == 1 - calendar for current month and year - no user input
if arg_count == 1:
  month
  year
#2 arg - name of program and month
elif arg_count == 2:
  #month
  month = int(sys.argv[1])
  year
elif arg_count == 3:
  #month and year
  month = int(sys.argv[1])
  year = int(sys.argv[2])
else:
  print('Try again!\n cal.py [month] [year]')
  sys.exit(1)

cal = calendar.TextCalendar()
cal.prmonth(year, month)