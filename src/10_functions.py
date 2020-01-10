# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(50))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def print_even(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd :(")


print(print_even(55))
