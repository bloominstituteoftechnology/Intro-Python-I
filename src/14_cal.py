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

args = sys.argv
print(args)

month = datetime.today().month
year = datetime.today().year

if len(args) == 1:
    pass
elif len(args) == 2:
    month = int(args[1])
elif len(args) == 3:
    month = int(args[1])
    year = int(args[2])
else:
    print("Error: Must be in format [month] [year]")


calendar.TextCalendar().prmonth(year, month)







#a, b = input("Enter a two values, first being the month number and second being the year number, comma separated: ").split(",")
#print("First number is {} and second number is {}".format(a, b))

''' try:
    a = input("Enter number for month: ")
except SyntaxError:
    a = None

try:
    b = input("Enter number for year: ")
except:
    b = None

print(a)
print(b)
'''




'''


a = input("Enter number for month (one or two digits): ")
b = input("Enter number for year (four digits): ")


if a == "" and b == "":
    print(calendar.month(2019, 6))

elif b == "":
    print(calendar.month(2019, int(a)))
elif int(a) <= 12 and b.count == 4:
    print(calendar.month(int(b), int(a)))
else:
    print("Please check your format")


'''

