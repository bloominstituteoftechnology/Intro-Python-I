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
from os import name, system

import sys

import calendar
import time

# define our clear function
def clear():
    print("\n" * 100)
    # # for windows
    # if name == "nt":
    #     _ = system("cls")

    # # for mac and linux(here, os.name is 'posix')
    # # The clear command also works for Windows if they are using PS
    # else:
    #     _ = system("clear")


prompt1 = input("Please Select Monthly or Yearly Calendar \n: ")
time.sleep(2)
clear()


def calendar_question(prompt1):
    res1 = f"{prompt1} isn't a valid answer :( \n Try again!"
    res2 = "Okay you want a Yearly? \n Coming right up!"
    res3 = "Okay you want a Monthly? \n Coming right up!"
    if prompt1 == str("y"):
        print(res2)
        calendar_maker(prompt1)
        time.sleep(2)
        clear()
    elif prompt1 == str("m"):
        print(res3)
        calendar_maker(prompt1)
        time.sleep(2)
        clear()
    else:
        print(res1)
        time.sleep(2)
        clear()


year = input("Please enter a 4 digit year \n: ")
month = input("Please enter a 2 digit month \n:")


def calendar_maker(prompt1):
    year = input("Please enter a 4 digit year \n: ")
    month = input("Please enter a 2 digit month \n:")
    if prompt1 == str("y"):
        print(year)
        print(calendar.calendar(year))
        time.sleep(10)
        clear()
        exit()
    else:
        print(year)
        print(month)
        print(calendar.month(year, month))
        time.sleep(10)
        clear()
        exit()
