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

# m = datetime.today().month
# y = datetime.today().year

# d = datetime.today()

# argss = input("Please enter month and year: ").split(" ")

# def calendarr(*args):
#   if(len(sys.argv) == 0):
#     print(calendar.month(d.year, d.month))
#   if(len(sys.argv) == 1):
#     print(calendar.month(d.year, int(args[0])))
#   if(len(sys.argv) == 2):
#     print(calendar.month(int(args[1]), int(args[0])))
#   else:
#     print("Must enter in the format: month, year")


# calendarr(*argss)


now = datetime.now()

if len(sys.argv) == 3:
    month = sys.argv[1]
    year = sys.argv[2]
elif len(sys.argv) == 2:
    month = sys.argv[1]
    year = now.year
elif len(sys.argv) == 1:
    month = now.month
    year = now.year
else:
    print("please provide args in the format [month] [year] and try again")
    print("exiting...")
    exit()
c = calendar.month(int(year), int(month))


# cal_args = input("Enter a month and year: ").split(" ")
# print(cal_args)

# def render_calendar(*args):
#     print(len(args))
#     d = datetime.now()
#     if len(args) == 0:
#         print(calendar.monthcalendar(d.year, d.month))
#     elif len(args) == 1:
#         print(calendar.monthcalendar(d.year, int(args[0])))
#     elif len(args) == 2:
#         print(calendar.monthcalendar(int(args[1]), int(args[0])))
#     else:
#         print("When running this program, please input:  month [year]")

# render_calendar(*cal_args) 

# print(calendar.month(yy, mm))
# print(calendar.month(d.year, d.month))
# # print(calendar.month(d.year, int(args[0])))
# print(sys.argv)