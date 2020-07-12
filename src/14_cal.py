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

#* function: val_prms validates inbound parameters
def val_prm(prm1, prm2=None):
  err = []

  # Is prm1 or prm2 not numeric
  if not prm1.isnumeric():
    err.append("month value: {prm1} is not numeric".format(prm1 = prm1))

  if prm2 != None and not prm2.isnumeric():
    err.append("year value: {prm2} is not numeric".format(prm2 = prm2))

  # Is prm1 or prm2 an invalid numeric value
  if prm1.isnumeric() and (int(prm1) < 1 or int(prm1) > 12):
     err.append("month value: {prm1} is invalid".format(prm1 = prm1))

  if prm2 != None and prm2.isnumeric() and (int(prm2) < 1900 or int(prm2) > 3000):
    err.append("year value: {prm2} is invalid".format(prm2 = prm2))

  return err

  
#* function: gen_cal generates the text calendar for a particular month and year
def gen_cal(mth:int=None, yr:int=None):
  # Get today's date
  to_day = datetime.today()

  # Create a calendar object
  cal_obj = calendar.TextCalendar()

  # Construct a return string
  ret_str = cal_obj.formatmonth(to_day.year, to_day.month)

  # Return the calendar for the current month and year
  if mth==None and yr==None:
    return ret_str

  # Return the calendar for the passed month in the current year
  if yr==None:
    ret_str = cal_obj.formatmonth(to_day.year, mth)
    return ret_str

  # Return the calendar for the passed month & year
  ret_str = cal_obj.formatmonth(yr, mth)
  return ret_str

#* main:
# Determine the number of command line parameters
prms_len = len(sys.argv)
prm1 = None
prm2 = None
err = []

# Validate the passed arguments
if len(sys.argv) == 3:
  prm1 = sys.argv[1]
  prm2 = sys.argv[2]
  err = val_prm(prm1, prm2)

if len(sys.argv) == 2:
  prm1 = sys.argv[1]
  err = val_prm(prm1, prm2)

# Do we have any validation errors
if len(err) != 0:
  # Validation errors: message user
  print("One or more errors are present: {err_str}".format(err_str="; ".join(err)))
  print("Usage: `python3 14_cal.py <month> [<year>]` (e.g. python3 14_cal.py 8 1999; python3 14_cal.py 8)")
  quit()

# Print out the calendar for the passed month and year
if prm1 != None:
  prm1 = int(prm1)
if prm2 != None:
  prm2 = int(prm2)
print(gen_cal(prm1, prm2))
