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
# import calendar
from calendar import *
from datetime import *

# import calendar import *

# make sure we have the right number of command line parameters

if len(sys.argv) == 1:
    # print "\nSyntax: hexcal month year (where month is 1 - 12)\n"
    # sys.exit(1)
    today_month = date.today().month
    today_year = date.today().year
    default = monthcalendar(today_year, today_month)
    print "%s %d\n" % (month_name[today_month], today_year)
    for week in default:
        for day in week:
            if day == 0:
                print "  ",
            else:
                print "%d" % day,
        print
    sys.exit(1)
    # return print("end")

# convert the two command line parameters to numerical values
# (they come in as strings)
if len(sys.argv) == 2:
    month = int(sys.argv[1])
    year = date.today().year
    default = monthcalendar(year, month)
    print "%s %d\n" % (month_name[month], year)
    for week in default:
        for day in week:
            if day == 0:
                print "  ",
            else:
                print "%d" % day,
        print
    sys.exit(1)
else:

    try:
        month = int(sys.argv[1])
        year = int(sys.argv[2])

    # get the matrix of days and weeks in the month
        monthMatrix = monthcalendar(year, month)

    except ValueError, message:
        print "Error:", message
        sys.exit(2)

# print out the heading
    print "%s %d\n" % (month_name[month], year)

# print out each day in hex; if the day = 0, then leave it blank
    for week in monthMatrix:
        for day in week:
            if day == 0:
                print "  ",
            else:
                print "%d" % day,
        print
