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

time = datetime.today()
month = time.month
year = time.year
args = sys.argv

def get_calendar(m=month, y=year):
  c = calendar.TextCalendar(calendar.SUNDAY)
  full_calendar = c.formatmonth(y,m)
  print(full_calendar)

if len(args) == 1:
  get_calendar()

elif len(args) == 2:
  try:
    raise ValueError('Please enter your month as a number..text is not allowed')
    arg_month = int(args[1])
    get_calendar(arg_month)    
  except ValueError as err:   
    print('Oh no you ran into an issue. {}'.format(err))
elif len(args) == 3:
  try:
    raise ValueError('Please enter your month and year as a number..text is not allowed')
    arg_month = int(args[1])
    arg_year = int(args[2])
    get_calendar(arg_month,arg_year)
  except ValueError as err:
    print('Oh no..you forgot something. {}'.format(err))  
else:
  print('Something went wrong..please enter the value as numbers')    

    
