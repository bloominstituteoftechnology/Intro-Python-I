# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"


def even_or_odd(num):
    return 'true' if num % 2 == 0 else 'false'


print(even_or_odd(num))
