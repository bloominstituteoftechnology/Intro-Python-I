# Write a function is_even that will return true if the passed in number is even.

num = input("Enter a number: ")


def even_odd(num):
    ans1 = "Even!"
    ans2 = "Odd!"
    default = f"{num} is not a number!"
    if (num).isdigit() == False:
        return default
    elif int(num) % 2 == 0:
        return ans1
    else:
        return ans2


# print(even_odd(num))
#
#
#
#
#
# Import numbers for some better capabilities.
# import numbers

# # We want screen clearing capabilities for EVERYONE.
# from os import name, system

# # import sleep to show output for some time period
# from time import sleep


# # define our clear function
# def clear():

#     # for windows
#     if name == "nt":
#         _ = system("cls")

#     # for mac and linux(here, os.name is 'posix')
#     # The clear command also works for Windows if they are using PS
#     else:
#         _ = system("clear")


# # Clear the console first, let's be gentleman about this.
# # Code will flow like this:
# # input => number check => integer check => Even Check => End
# clear()
# # Take input from user
# num = raw_input("Enter a number: ")
# # Clear the console
# clear()
# # Inform the user we have received their number.
# print(f"What do you think the output of {num} will be?")
# # Pause for a few seconds so they can read it.
# sleep(4)
# # Clear the screen again to stop clutter.
# clear()
# # Initalizing checkers!
# def main(num):
#     Print(f"We're going to see if we can work with {num} first!")
#     sleep(4)
#     clear()
#     is_num(num)


# # check for number status first. If no, then reject with error.
# def is_num():
#     default = print(f"{num} is not a number!, try again with a NUMBER!")
#     if (num).isdigit() == False:
#         return default
#     else:
#         is_int(num)


# Print(f"So, I guess {num} is a number! Good Job!")
# sleep(4)
# clear()
# Print(f"Now let's see if {num} is an integer. I only work with real Numbers.")
# sleep(4)
# clear()

# # check for integer status.
# def is_int():
#     resp1 = print(f"{num} isn't an integer, but that's okay. We can fix it!")
#     resp2 = print(f"{num} is an integer! Perfect!")
#     if isinstance(num, int) == True:
#         return resp2
#         sleep(4)
#         clear()
#         even_odd(num)
#     else:
#         return resp1
#         sleep(4)
#         clear()
#         int(num)
#         even_odd(num)


# # Even or Odd
# def even_odd():
#     ans1 = print("Even!")
#     ans2 = print("Odd!")
#     if num % 2 == 0:
#         return ans1
#     else:
#         return ans2
