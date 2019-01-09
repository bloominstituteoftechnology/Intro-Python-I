"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
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

x = input("Enter a month and optionally a year: ").split(' ')

print(f'input: {x}')

if len(x) == 1:
  if x[0] == '':
    print('current date')
  elif int(x[0]) > 0 and int(x[0]) < 13 :
    print(f'selected month {int(x[0])}')
  else:
    print('please enter a month first then optionally a year "02 2018"')
    
elif len(x) == 2:
  if int(x[0]) > 0 and int(x[0]) < 13:
    selectedMonth = int(x[0])
  else:
    print('Month format invalid...')
  
  if int(x[1]) > 0 and int(x[1]) <= 9999:
    selectedYear = int(x[1])
  else:
    print('Year format invalid')

if selectedMonth and selectedYear:
  print(f'Month: {selectedMonth}, Year: {selectedYear}')