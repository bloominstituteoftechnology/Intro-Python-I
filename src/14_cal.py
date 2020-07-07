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

import calendar
from datetime import datetime

currentMonth = datetime.now().month
currentYear = datetime.now().year

array = []
# array.append(input("Enter year and month:"))
x = input("Enter comma-separated month and year: ").split(',')
x = [(i) for i in x]

array.extend(filter(None, x))

if not array:
    print(calendar.prmonth(currentYear, currentMonth, w=0, l=0))
elif len(array) == 1 and [x for x in array if x.isdigit() and int(x) in range(1, 13)]:
    print(calendar.prmonth(currentYear, int(array[0]), w=0, l=0))

elif len(array) == 2 and [x for x in array if x.isdigit()]:

    if not array[0].isdigit() or not array[1].isdigit():
        print("Wrong input format!!!")

    else:

        month = int(array[0])
        year = int(array[1])
        if month in range(1, 13):
            print(calendar.prmonth(year, month, w=0, l=0))
        else:
            print("month is from 1 to 12")

else:
    print("Input is not in correct format, can't see the calendar.")
quit()
