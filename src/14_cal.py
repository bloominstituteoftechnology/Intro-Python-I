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
import datetime

# Pseudocode
# 1. get user input
user_input = sys.argv

c = calendar.TextCalendar(calendar.SUNDAY)

current_month = datetime.datetime.now().strftime("%m")
current_year = datetime.datetime.now().strftime("%Y")

mm = int(current_month)
yy = int(current_year)

format_current = c.prmonth(yy, mm)


arg_month = user_input[1]
m = int(arg_month)
arg_year = user_input[2]
y = int(arg_year)
arg_length = len(user_input)

length_2 = c.prmonth(y, m)
length_1 = c.prmonth(yy, m)
error = "Please enter arguments for month and year (ex: python3 14_cal.py 4 2015)"

# 3. Else If user enters one argument, assume it is a month , print the calendar for that month of the current year. ([month] 2020)
if arg_length == 2:
    c = calendar.TextCalendar(calendar.SUNDAY)
    print(length_1)
# 4. Else If user enters two arguments, assume they gave the month and year. Print the calendar for given month and year.
elif arg_length == 3:
    c = calendar.TextCalendar(calendar.SUNDAY)
    print(length_2)

# 2. If user doesn't enter any input, print the calendar for the current month ('datetime' module)
elif arg_length == 1:
    print(format_current)
# 5. Else, print statement to the terminal indicating proper format that your program expects arguments to be given.
else:
    print(error)
# 6. Then exit the program.













# def print_calendar(user_input):
  
#     user_month = user_input[0]
#     user_year = user_input[1]

#     if not user_input:

    


