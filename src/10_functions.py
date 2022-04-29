# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    return not num & 1


# Read a number from the keyboard
num1 = input("Enter a number: ")

num = int(num)


# Print out "Even!" if the number is even. Otherwise print "Odd"

print('Even!' if is_even(num) else 'Odd')
