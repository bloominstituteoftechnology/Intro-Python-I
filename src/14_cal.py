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

def get_calendar():
    now = datetime.now()
    current_month = now.month
    current_year = now.year

    input_date = input("Please select a date, exp MM/YYYY:").split('/')

    def show_cal(month = current_month, year = current_year):
        try:
          print(calendar.monthcalendar(int(year), int(month)))
        except:
          print("please input a proper month and year in the following format 'MM/YYYY'")
          get_calendar()
        
    if len(input_date) > 2:
      print("Please input only Month and Year")
    if (input_date[0]) == '':
      show_cal()
    else:
      show_cal(*input_date)

get_calendar()
