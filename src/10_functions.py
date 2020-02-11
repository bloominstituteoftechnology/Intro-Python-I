# Write a function is_even that will return true if the passed-in number is even.

# * SOLUTIONS BELOW:
# * OPEN INTERPRETER && RUN: python3 10_functions.py


def is_even(number):
    if(int(number) % 2) == 0:
        print('Even number')
        return True
    elif(int(number) % 2) != 0:
        print('Odd number')
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

is_even(num)
