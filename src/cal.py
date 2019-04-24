"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
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
"""

import sys
import calendar
from datetime import datetime

cal= calendar.Calendar()
textCal= calendar.TextCalendar()
timeNow = datetime.now()

strTimeNowMonth = str(timeNow)[5:7]
if strTimeNowMonth[0] == "0":
  strTimeNowMonth = int(strTimeNowMonth[1])
else:
  strTimeNowMonth = int(strTimeNowMonth)
strTimeNowYear = int(str(timeNow)[:4])

# print(strTimeNowMonth)
# print(strTimeNowYear)

print('calendar.py [month] [year]')
cmd = input('[1-12] [XXXX]: ')
print(f"Answer: {cmd}")

print(type(cmd))

if len(cmd) is 0:
  textCal.prmonth(strTimeNowYear, strTimeNowMonth, w=0, l=0)
elif len(cmd) <= 2:
  if cmd[0] == "0":
    textCal.prmonth(strTimeNowYear, int(cmd[1]), w=0, l=0)
  else:
    textCal.prmonth(strTimeNowYear, int(cmd), w=0, l=0)
elif len(cmd) > 2 and cmd.find(" ") >= 0 and len(cmd) <= 7:
  if len(cmd) == 7:
    inputYear = int(cmd[3:])
  elif len(cmd) == 7:
    inputYear = int(cmd[2:])
  print(type(inputYear))
  if cmd[0] == "0":
    textCal.prmonth(inputYear, int(cmd[1]), w=0, l=0)
  else:
    textCal.prmonth(inputYear, int(cmd), w=0, l=0)
else:
  print("Incorrect Formatting: Provide 1 or 2 characters for the month (1 or 01), space, 4 characters for the year.")






