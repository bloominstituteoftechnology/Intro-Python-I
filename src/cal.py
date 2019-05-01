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

# userInput = input(“Input month and year seperated by a comma:“).split(‘,’)

# # ask of month and year
# year = int(input("Please Enter the year Number: "))
# month = int(input("Please Enter the month Number: "))

"""
if len(sys.argv) == 1:
    print(calendar.month(year, month))
  elif len(sys.argv) == 2:
    print(calendar.month(year, int(sys.argv[1])))
  elif len(sys.argv) == 3:
    print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
else:
  sys.exit("invalid number")
"""

# cur_year = datetime.now().year
# cur_month = datetime.now().month

# if len(sys.argv) == 1:
#     print(calendar.month(cur_year, cur_month))


# # if :
# c = calendar.TextCalendar(calendar.SUNDAY)
# print(c.prmonth(datetime.now().year, datetime.now().month))
# # else:
# print(calendar.month(year, month))

today = datetime.today()
thisyear = today.year
thismonth = today.month

if __name__ == "__main__":
  if len(sys.argv) == 1:
      print(calendar.month(thisyear, thismonth))
  
  if len(sys.argv) == 2:
    
    m = int(sys.argv[1])
    print(calendar.month(thisyear, m))
  if len(sys.argv) == 3:
    m = int(sys.argv[1])
    y = int(sys.argv[2])
    print(calendar.month(y, m))
  if len(sys.argv) > 3:
    print("Run the program from CLI with the format: `python calendar.py month [year]`")


