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
import pprint

"""
Learning some examples on how to produce
yearly calendars:
"""
# This produces calendar for the year 2020
# cal = calendar.TextCalendar(calendar.SUNDAY)
# print(cal.formatyear(2020, 2, 1, 1, 3))

# This prints out a calendar for April in 2015
# pprint.pprint(calendar.monthcalendar(2015, 4))

# year = int(sys.argv[1])
#
# # Show every month
# for month in range(1, 13):
#
#     # Compute the dates for each week that overlaps the month
#     c = calendar.monthcalendar(year, month)
#     first_week = c[0]
#     second_week = c[1]
#     third_week = c[2]
#
#     # If there is a Thursday in the first week,
#     # the second Thursday is # in the second week.
#     # Otherwise, the second Thursday must be in
#     # the third week.
#     if first_week[calendar.THURSDAY]:
#         meeting_date = second_week[calendar.THURSDAY]
#     else:
#         meeting_date = third_week[calendar.THURSDAY]
#
#     print('{:>3}: {:>2}'.format(calendar.month_abbr[month],
#                                 meeting_date))

"""
14_cal.py Assignment starts here:
"""
if(len(sys.argv) == 1):
    month = datetime.now().month
    year = datetime.now().year
    print(year, month)


elif(len(sys.argv) == 2):
    month = int(sys.argv[1])
    year = datetime.now().year

elif(len(sys.argv) == 3):
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    print(year, month)

print(calendar.month(year, month))
