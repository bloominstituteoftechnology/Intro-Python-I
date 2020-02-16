#!/usr/bin/env python

# run file by typing `./14_cal.py <month> <year>

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

argument_length = len(sys.argv)
custom_calendar = calendar.TextCalendar();

def convert_date_str_to_int(values):
  return [int(value) for value in values]

def create_calendar_options(month=datetime.today().month, year=datetime.today().year, width=5, length=1):
  return {
    "themonth": month,
    "theyear": year,
    "w": width,
    "l": length
  }

def print_calendar(calendar, **options):
  print(calendar.formatmonth(**options))

def extract_month_year_from_datetime(date=datetime.today()):
  return str(date).split(' ')[0].split('-')[0:2]

# if year or month is left out, print cal based on today
if (argument_length == 1):
  year, month = convert_date_str_to_int(extract_month_year_from_datetime())
  options =  create_calendar_options()

  print_calendar(custom_calendar, **options)
  exit(0)

if (argument_length == 2): 
  # assumes it was a month entered
  month = convert_date_str_to_int(sys.argv[1:2])[0]
  options = create_calendar_options(month)
  print_calendar(custom_calendar, **options)
  exit(0)

  print_calendar(custom_calendar, **options)

# if there's all arguments necessary
if (argument_length == 3):
  month, year = convert_date_str_to_int(sys.argv[1:3])
  options = create_calendar_options(month=month, year=year)
  print(options)
  print_calendar(custom_calendar, **options)
  exit(0)

print('Usage: ./14_cal.py [month] [year]')



