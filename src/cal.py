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

# year = int(input("Please Enter the year Number: "))
# month = int(input("Please Enter the month Number: "))
# userInput = input("Input month and year seperated by a comma:").split(',')
#   if len(sys.argv) == 1:
#     print(calendar.month(cur_year, cur_month))


# now = datetime.datetime.today()



# def makeCal(a = now.month,b = now.year ):
#   myCal = calendar.TextCalendar(calendar.SUNDAY)
#   str = myCal.formatmonth(b, a)
#   print(str)

# if len(userInput) == 1 and len(userInput[0]) == 0:
#   makeCal()
# if len(userInput) == 1 and len(userInput[0]) > 0:
#   makeCal(int(userInput[0]))
# if len(userInput) == 2:
#   makeCal(int(userInput[0]), int(userInput[1]))
# if len(userInput) > 3:
#   print("provide no more then two arguments")

cur_year = datetime.now().year
cur_month = datetime.now().month

try:
   if len(sys.argv) == 1:
       print(calendar.month(cur_year, cur_month))
   elif len(sys.argv) == 2:
       print(calendar.month(cur_year, int(sys.argv[1])))
   elif len(sys.argv) == 3:
       print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
except:
   print("\nPlease enter 'python cal.py [month] [year]'.\
          \nNote month and year are optional but must be an integer.\
          \n")