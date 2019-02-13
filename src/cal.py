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
class MyCalendar:
  def __init__(self, month=None, year=None):
    self.now= datetime
    if month!=None and year!=None:
      self.month= month
      self.year=year
    elif month!=None and year==None:
      self.month=month
      self.year= self.now.year
    elif month==None and year==None:
      self.month=self.now.month
      self.year= self.now.year
  def __str__(self):
    return calendar.month(self.year, self.month)

month= input('Please provide a month: ')
year=input('Please provide a year: ')
myCalendar= MyCalendar(int(month),int(year)).__str__()
print(myCalendar)


