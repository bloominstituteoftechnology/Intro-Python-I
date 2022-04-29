# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

# 10
# https://github.com/LambdaSchool/Intro-Python-I/blob/master/src/10_functions.py
#

# Write a function is_even that will return true if the passed-in number is even.

def is_even(number):
    if number%2 == 0:
        return True
    else:
        pass

is_even(3)
is_even(4)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even2(num):
    if num%2 == 0:
        return print("Even!")
    else:
        return print("Odd")

is_even2(num)