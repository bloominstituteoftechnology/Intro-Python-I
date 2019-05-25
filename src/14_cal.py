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

# first attempt, probably overthinking 
# c = calendar.TextCalendar(firstweekday=6)
# def help():
#     print("cmd: python cal.py [month] [year]")
# def main(args):
#     if len(args) == 0:
#         t = datetime.now()
#         s = c.formatmonth(t.year, t.month)
#         print(s)  
#     elif len(args) == 1:
#         if (args[0] == "-h" or args[0] == "--help"):
#             help()
#         else:
#             t = datetime.now()
#             s = c.formatmonth(t.year, int(args[0]))
#             print(s)
#     elif len(args) == 2:
#         s = c.formatmonth(int(args[1]), int(args[0]))
#         print(s)
#     else:
#         help()
# if __name__ == "__main__":
#     main(sys.argv[1:])

#second attempt, much simpler
# if(len(sys.argv) == 1):
#     m = datetime.now().month
#     y = datetime.now().year
#     print(calendar.month(y, m))
# elif len(sys.argv) == 2:
#     m = int(sys.argv[1])
#     y = datetime.now().year

#     print(calendar.month(y, m))
# elif len(sys.argv) == 3:
#     m = int(sys.argv[1])
#     y = int(sys.argv[2])

#     print(calendar.month(y, m))
# else:
#     print('Please enter month and year like MM YYYY')
#     sys.exit()

#third attempt, the simplest!
if len(sys.argv) == 1:
  print("Input a Year in yyyy format and Month in mm format")
elif len(sys.argv) == 2:
  mm = int(sys.argv[1])
  print(calendar.month(datetime.now().year,mm))
elif len(sys.argv) == 3:
  mm = int(sys.argv[1])
  yy = int(sys.argv[2])
  print(calendar.month(yy,mm))

sys.exit()