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
from argparse import ArgumentParser

def make_argparser() -> ArgumentParser:
  """
  Parse command line arguments.
  """
  parser = ArgumentParser(description='Specify year and month')
  parser.add_argument('year', type=int, help='please enter a year in the form YYYY')
  parser.add_argument('month', type=int, help='please add a month in the form M or MM')

  return parser

if __name__ == "__main__":
  args = make_argparser().parse_args()

  calendar.TextCalendar().prmonth(args.year, args.month)