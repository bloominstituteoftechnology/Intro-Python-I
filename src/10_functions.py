# Write a function is_even that will return true if the passed number is even.

# YOUR CODE HERE


def is_even(number):
    if number % 2 == 0:
        return "true"

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def is_even(number):
    if number % 2 == 0:
        return "Even!"
    else:
        return "Odd"

print(is_even(num))
