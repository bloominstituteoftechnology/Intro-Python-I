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


# Import libraries and modules:
import calendar
import datetime
import sys


# Get arguments the user inputted when running this file (14_cal.py):
arguments = sys.argv

# Get the current month and year:
today = datetime.date.today()

# String to print if user enters the wrong type of argument when calling this file:
error_string = """If you enter any arguments, please enter as "filename.py [month] [year]", 
where both month and year are integers."""

if len(arguments) == 1:
    date = today
    cal = calendar.month(theyear=date.year, themonth=date.month)
    print("\n", cal)

elif len(arguments) == 2:
    try:
        input_month = int(arguments[-1])
    except ValueError as value_error:
        sys.exit(f"\nError: {str(value_error).split()[-1]} \nReason: {exit_string}\n")
    date = datetime.date(year=today.year, month=input_month, day=today.day)
    cal = calendar.month(theyear=date.year, themonth=date.month)
    print("\n", cal)

elif len(arguments) == 3:
    try:
        input_month = int(arguments[-2])
        input_year = int(arguments[-1])
    except ValueError as value_error:
        sys.exit(f"\nError: {str(value_error).split()[-1]} \nReason: {exit_string}\n")
    date = datetime.date(year=input_year, month=input_month, day=today.day)
    cal = calendar.month(theyear=date.year, themonth=date.month)
    print("\n", cal)

else:
    print(f"Error: {exit_string}")
