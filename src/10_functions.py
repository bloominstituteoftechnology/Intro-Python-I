# Write a function is_even that will return true if the passed-in
# number is even.

# YOUR CODE HERE


def is_even(x):
    """function that cheks is a number is even or not"""
    if (num % 2) == 0:
        return True
    else:
        return False
# Read a number from the keyboard
num = int(input("Enter a number: "))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
print('Even!' if is_even(num) is True else 'Odd')
