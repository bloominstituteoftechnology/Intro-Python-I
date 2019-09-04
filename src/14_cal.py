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


def main():


  # no arguments
  if len(sys.argv) == 1:
      this_month = datetime.now().month
      this_year = datetime.now().year
      print(calendar.month(this_year, this_month))

  # month argument
  elif len(sys.argv) == 2:
    this_month = int(sys.argv[1])
    if this_month < 1 or this_month > 12:
      print("Please enter a month between 1 and 12")
      return

    this_year = datetime.now().year
    print(calendar.month(this_year, this_month))

  # month and year argument
  elif len(sys.argv) == 3:
    month = int(sys.argv[1])
    if this_month < 1 or this_month > 12:
      print("Please enter a month between 1 and 12")
      return
    year_txt = sys.argv[2]
    year = int(year_txt[year_txt.find('[')+1:year_txt.find(']')])
    print(calendar.month(year, month))

  # more than 2 arguments
  else:
    print("Program only takes two arguments at the most")

if __name__ == "__main__":
    main()