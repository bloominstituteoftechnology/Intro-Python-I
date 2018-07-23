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

# Strip off first element of argv
args = sys.argv[1:]

# Make sure that arg count is what we expect
if len(args) != 2:
  raise ValueError('Expected month and year as inputs')

# Create text calander and print it to console
cal = calendar.TextCalendar()
cal.prmonth(int(args[1]), int(args[0]))
