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
from calendar import Calendar, TextCalendar
from datetime import datetime, date

month = int(sys.argv[1]) if len(sys.argv) > 1 else date.today().month
year = int(sys.argv[2]) if len(sys.argv) > 2 else date.today().year

# Uneccessary, but a good exercise
def construct_calendar_string(year, month):
  weeks = Calendar().monthdatescalendar(year, month)
  
  weekdays = ["Mon ", "Tues", "Wed ", "Thur", "Fri ", "Sat ", "Sun "]
  months = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November",
            "December"]

  weekday_header = "│ " + " │ ".join(weekdays) + " │"
  width = len(weekday_header)
  title = str(months[month-1]) + " " + str(year)
  box_top = "┌" + "┬".join(["──────"] * len(weekdays)) + "┐"
  box_layer = "├" + "┼".join(["──────"] * len(weekdays)) + "┤"
  box_bottom = "└" + "┴".join(["──────"] * len(weekdays)) + "┘"

  calendar_string = "".join([" "] * ((width - len(title)) // 2)) + title + "\n"
  calendar_string = calendar_string + box_top + "\n"
  calendar_string = calendar_string + weekday_header + "\n"
  for w in weeks:
    calendar_string = calendar_string + box_layer + "\n"
    calendar_string = calendar_string + "│ " + " │ ".join([ str(d.day).ljust(4) for d in w ]) + " │" + "\n"
  calendar_string = calendar_string + box_bottom

  return(calendar_string)

if __name__ == "__main__":
  print(construct_calendar_string(year, month))
  #print(TextCalendar().formatmonth(year, month))


