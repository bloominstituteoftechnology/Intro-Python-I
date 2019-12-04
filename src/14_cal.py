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

user = input('Enter the month and date:   ')
user_input = user

import sys
import calendar
from datetime import datetime

def cal(*args):
    if len(args) == 0:
      current_date = datetime.now()
      print(calendar.prmonth(current_date.year, current_date.month))
    elif len(args) == 1 :
      current_date = datetime.now()
      # user_input[0]==(calendar.prmonth(current_date.year, current_date.month))
      print(calendar.prmonth([user_input], current_date.year, current_date.month))
      
      
      
      
      
      
      
      
    # elif (len(args) == 1): #needs to be the calendar that corresponds to that month
    #     current_date = datetime.now()
    #     print(calendar.prmonth(current_date.year)
              
# else:
#     print('Please enter the date and month in the following format: ')
        
  
      
print('none', cal())
print('1 arg', cal(1))
# print('2 args', cal(2019, 3))