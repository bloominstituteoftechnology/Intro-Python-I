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

month_entry = input('Enter the month, enter one or two digits, depending on the month: ')
year_entry = input('Enter the year, four digits for the year: ')

today = datetime.today()
print(today)
if month_entry == "" and year_entry == "":                       # When user does not provide any information 
    print(calendar.month(today.year, today.month))
elif month_entry == "" and year_entry != "":                     # When user provide the year only
    print(calendar.month(int(year_entry), today.month))   
elif month_entry != "" and year_entry == "":                     # When user provide the month only
    print(calendar.month(today.year, int(year_entry)))          
elif month_entry != "" and year_entry != "":                     # When user provides both month and year. I need to work on the input validation. good for now
    print(calendar.month(int(year_entry), int(month_entry)))
else:    
    print('Please, provide information as requested. Example: for January type 1. For 2019 year type 2019')

