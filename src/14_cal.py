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
# print("system print", len(sys.argv[0]))


# def make_calendar(args):


cal = calendar.TextCalendar(calendar.SUNDAY)
# print("cal test:", cal)
d = datetime.today()
# print("datetime test", d)

print(cal.prmonth(d.year, d.month))
# if len(sys.argv) == 1:
#     print(cal.prmonth(d.year, d.month))
# elif len(sys.argv) == 2:
#     month = int(sys.argv[1])
#     print(cal.prmonth(d.year, month))
# elif len(sys.argv) == 3:
#     month = int(sys.argv[1])
#     year = int(sys.argv[2])
#     print(cal.prmonth(year, month))
# else:
#     print("user needs to enter date in a format of  month and then year")

# original = raw_input('Enter a month and year: ')
# raw_input

# pyg = 'ay'

# original = raw_input('Enter a word:')

# if len(original) > 0 and original.isalpha():
#   word = original.lower()
#   first = word[0]
#   new_word = word + first + pyg
#   new_word = new_word[1:len(new_word)]
# else:
#     print 'empty'
