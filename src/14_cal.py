# python3 src/14_cal.py

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

using_calendar = True

while using_calendar:
    # give game start message to the user that explains the game and waht is expected
    print("Welcome to Calendar")

    user_input = input("Enter month and year: ").split()
    c = calendar.TextCalendar(calendar.SUNDAY)
    today = datetime.today().strftime("%Y-%m")
    year_current, month_current = today.split('-')
    year_current, month_current = int(year_current), int(month_current)

    # if the user doesn't specify any input
    if user_input == []:
      # print the calendar for the current month
      data = c.formatmonth(year_current, month_current)
      print(data)
      play_again = input("Would you like to see Calendar for another date? Y or N?")
      if play_again.lower() =="n":
        # exit the program
        using_calendar = False

    # if the user specifies arguments
    elif user_input is not None:
      # if the user specifies two arguments, assume they passed in
      # both the month and the year
      if len(user_input) == 2:
        month, year = user_input
        month, year = int(month), int(year)
        if month <= 12:
          # print the calendar for that month and year
          data = c.formatmonth(year, month)
          print(data)
          play_again = input("Would you like to see Calendar for another date? Y or N?")
          if play_again.lower() =="n":
            # exit the program
            using_calendar = False
        else:
          print("Please, make sure your input is in the correct format")
          play_again = input("Would you like to see Calendar for another date? Y or N?")
          if play_again.lower() =="n":
            # exit the program
            using_calendar = False

      # if the user specifies one argument, assume they passed in a month
      elif len(user_input) == 1:
        month = user_input[0]
        month = int(month)
        if month <= 12:
          # print the calendar for that month and a current year
          data = c.formatmonth(year_current, month)
          print(data)
          play_again = input("Would you like to see Calendar for another date? Y or N?")
          if play_again.lower() =="n":
            # exit the program
            using_calendar = False
        else:
          # print a usage statement to the terminal indicating 
          # the format that your program expects arguments to be given
          print("Please, make sure your input is in the correct format")
          play_again = input("Would you like to see Calendar for another date? Y or N?")
          if play_again.lower() =="n":
            # exit the program
            using_calendar = False
      
      else:
          print("Please, make sure your input is in the correct format")
          play_again = input("Would you like to see Calendar for another date? Y or N?")
          if play_again.lower() =="n":
            # exit the program
            using_calendar = False
