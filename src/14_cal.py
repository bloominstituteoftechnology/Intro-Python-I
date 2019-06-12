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

user_month_and_year = input("Enter a month and year separated by a comma: ").replace(" ", "").split(",")

def create_new_calendar(*args):

	rendered_calendar = calendar.TextCalendar()

	month = datetime.today().month
	year = datetime.today().year
	day = datetime.today().day

	if len(args) == 1:
		try:
			int_month = int(args[0])
			one_date = datetime(year, int_month, day)
			print(rendered_calendar.prmonth(one_date.year, one_date.month))
		except:
			print(rendered_calendar.prmonth(year, month))
		
	elif len(args) == 2:
		two_date = datetime(int(args[1]), int(args[0]), day)
		print(rendered_calendar.prmonth(two_date.year, two_date.month))
	else:
		print("Please enter two numbers. The first should be between 1 and 12 representing a month. The second should be four digits representing a year.")

create_new_calendar(*user_month_and_year)
