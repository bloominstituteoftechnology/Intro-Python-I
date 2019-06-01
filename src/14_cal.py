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
from datetime import datetime

def grab_input():
   user_input = input("Enter calendar month/year: ")
   cal(user_input)

def check_month(month):
   if int(month) > 0 and int(month) <= 12:
      return True
   else:
      return False

def check_year(year):
   if int(year) > 0 and int(len(year)) == 4:
      return True
   else:
      return False

def cal(arg):
   #get current date time for zero and one inputs
   now = str(datetime.utcnow()).split("-")[1::-1]
   #if no input is provide print calendar for current month/year
   if len(arg) == 0:
      print(calendar.month(int(now[1]), int(now[0])))
   #else find if user had provided month/year or just month
   #error check to make sure month is valid
   #if just month print that month with current year else print the month and year requested
   else:
      if len(arg) < 3:
         if  check_month(arg):
            print(calendar.month(int(now[1]), int(arg)))
         else:
            print("Invalid month! Please enter month between 01 - 12: ")
            grab_input()
      elif len(arg) == 6 or len(arg) == 7:
         month_year = arg.split("/")
         if check_month(month_year[0]):
            if check_year(month_year[1]):
               print(calendar.month(int(month_year[1]), int(month_year[0])))
            else:
               print("Invalid year! Please enter calandar month/year in the following format:\tmm/yyyy\n")
               grab_input()
         else:
            print("Invalid month! Please enter month between 01 - 12: ")
            grab_input()
      else:
         print("Invalid input! Please provide calander month/year in the following format:\tmm/yyyy\n")
         grab_input()

grab_input()