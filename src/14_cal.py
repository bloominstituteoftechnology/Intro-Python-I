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




# some global variables 
# Setting it initially as the current month and
# the current year
the_mon = datetime.today().month
the_yr = datetime.today().year

# if the user inputs bad inputs then the usage message will be outputted
usage_needed = 1

# getting the length of the arguments that are passed in in the 
# sys.argv.
numArgs = len(sys.argv)
# entering this if statement is there are options on the command line
if numArgs > 1:
  # getting any of the args from the command line
  for i in range(len(sys.argv)):
    if i == 1:
      if sys.argv[i].isnumeric():
        mon = int(sys.argv[i])
        if mon > 0 and mon <= 12:
          # assignment of the month 
          the_mon = mon
          # printing out the usage is not needed
          usage_needed = 0 
    if i == 2:
      
      if sys.argv[i].isnumeric():
        # getting the year
        yr = int(sys.argv[i])
        # checking to make sure it is not neg
        if yr >= 0:
          the_yr = yr
        # if a neg number is passed in the usage will need to be printed out
        else:
          usage_needed = 1
      else:  
        usage_needed = 1
else:
  # if enters here there were no arguments (options) added to the 
  # command line so no need to print the usage statement
  usage_needed = 0



# using the flag usage_needed to see what 
# we will be printing
if usage_needed:
  # printing the usage
  print("""
        To use this program, you may enter optional arguments after
         the entering the program name as thus:\n\n
         `14_cal.py [month] [year]`\n
         If only one option is used it will be used as a month.
         The month can be from the range of 1-12, while the year can
         be in the range of 0 to whenever.
        """)
else:
  print(calendar.month(the_yr,the_mon))

