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
import calendar
import sys

args = len(sys.argv) # this line gets the args passed length and sets it to args

if args == 2:
  month = None # null == None
  year = int(sys.argv[1]) # sets arg at index 1 and casts as a integer to year because only two args were declared, the first one is the script name.

elif args == 3:
  month = int(sys.argv[1])
  year = int(sys.argv[2])
else:
  print("usage: cal.py [month] year")
  sys.exit(1)

# Make a new calendar
c = calendar.TextCalendar()

if month != None:
    # If the user specified a month, print that month
    c.prmonth(year, month)
else:
    # Otherwise just print it for the year
    c.pryear(year)