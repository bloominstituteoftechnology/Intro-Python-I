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
from datetime import date

cal = calendar.TextCalendar(firstweekday=0)
today = date.today()

if len(sys.argv) == 1: # Zero arguments - print calendar for this month and year
	print(cal.formatmonth(today.year, today.month))

if len(sys.argv) == 2: # One argument - assume it's the month, print calendar for the month provided of current year
	try:
		month = int(sys.argv[1])
		print(cal.formatmonth(today.year, month))
	except:
		print("Invalid month argument. Enter a number 1-12 for month.\nExample: 14_cal.py 12 for December")
		sys.exit()
if len(sys.argv) == 3: # 2 arguemnts - assume first is month and second is year, print calendar for month and date provided
	try:
		month = int(sys.argv[1])
		year = int(sys.argv[2])
		print(cal.formatmonth(year, month))
		sys.exit()
	except ValueError:
		print("Invalid month or year input. Enter a number 1-12 for month, and optionally a number up to 4 digits for year.\nExample: 14_cal.py 1 2020 for Jan 2020")
		sys.exit()
if len(sys.argv) > 3:
	print("More than 2 arguments were provided to program.\nEnter a number 1-12 for month, and optionally a number up to 4 digits for year.\nExample: 14_cal.py 1 2020 for Jan 2020\nExample: 14_cal.py 12 for December")
	sys.exit()
