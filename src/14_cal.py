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

# Current date
today = datetime.today()
month = today.month
year = today.year

# CLI arguments are kept in sys.argv (list). 
# Need everything but the first arg because the first arg is the filename.
cli_args = sys.argv

if len(cli_args) <= 3:
  try:
    if int(cli_args[1]) > 0 and int(cli_args[1]) <= 12 and int(cli_args[2]) > 1900 and int(cli_args[2]) <= 2020:
      # If no cli args
      if len(cli_args) == 1:
        print(calendar.month(year, month))

      # If one cli arg
      if len(cli_args) == 2:
        print(calendar.month(year, int(cli_args[1])))

      # If two cli args
      if len(cli_args) == 3:
        print(calendar.month(int(cli_args[2]), int(cli_args[1])))
    else:
      print("ERROR: The CLI arguments must be in a numeric format. Month 1-12. Year 1900-2020.")
  except:
    print("ERROR: The CLI arguments must be in a numeric format. Month 1-12. Year 1900-2020.")

else:
  print("ERROR: When running this program in the CLI, include either 0, 1, or 2 arguments. If 1 it assumes the month(numeric format). If 2, the month and then the year (both in numeric format)")