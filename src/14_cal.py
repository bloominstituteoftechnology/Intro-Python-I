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
print(int(10))

#how do you write a function that accepts user input? ---use input() function, user passes string in terminal:
#  x = input("Enter comma-separated numbers: ").split(',')
#if user gives no inputs then print calendar for current month
#if user gives 1 input assume its the month. print the calendar for that month of current year
#two args = month, year - calendar for that month and year
#if user gives any other inputs, print a statement for what arguments should be given and exit program (exit())
# print(calendar.month(2020, 6))


#default arguments should be current month and current year
#set conditions for if the month is a string anything other than 1-12 for a prompt explaining how to use it
#set conditions for if the year is a string anything other than a number for a prompt explaining how to use it
#how to specify if a string does not equal '1' -'12'
def userCalendar(month = 6, year = 2020):
  month = input("enter month you would like a calendar for: ")
  year = input("enter year you would like a calendar for: ")
  if month == '':
    month = 6
  elif month.isnumeric != True and int(month) > 12 or int(month) < 1:
    print('must enter a number from 1 to 12 for month value')
    return None
  if year == '':
    year = 2020
  elif year.isnumeric() != True:
    print('must enter a number for the year value')
    return None
  month = int(month)
  year = int(year)
  print(calendar.month(year, month))
  #set variable month to take the month of user's choice
  
  #set variable year to take the year of users choice
  
  #if user gives no inputs print calendar for current month
  
  #if user gives one input print calendar for that month of current year 

  #if two args then treat them as month and year
userCalendar()