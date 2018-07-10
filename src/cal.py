# Use the 'calendar' module to draw calendars to the console
# https://docs.python.org/3.6/library/calendar.html
#
# Use the sys module to look for command line arguments in the `argv` list
# variable.
#
# If the user specifies two command line arguments, month and year, then draw
# the calendar for that month.

# Stretch goal: if the user doesn't specify anything on the command line, show
# the calendar for the current month. See the 'datetime' module.

# Hint: this should be about 15 lines of code. No loops are required. Read the
# docs for the calendar module closely.

import sys
import calendar
import datetime

# sys.argv[1] = 1
# sys.argv[2] = 2011
# month = input("Please enter the a month")
# year = input("Please enter the year")
month = sys.argv[1] 
# print(month)
year = sys.argv[2] 

print(calendar.month(int(year), int(month)))

  # print(datetime.datetime.now())
# print(sys.copyright)
# print(sys.platform)
# print(sys.api_version)
# print(sys.version)
#print(sys.winver)

# print("This is the name of the script: ", sys.argv[0])
# print("Number of arguments: ", len(sys.argv))

# print("The arguments are: " , str(sys.argv))