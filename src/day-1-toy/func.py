# Write a function is_even that will return true if the passed in number is even.

def is_even(num):
    if int(num)%2 == 0:
        return 'true'
    else:
        return 'false'

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"

def print_even(num):
    if is_even(num):
        print('Even!')
    else:
        print('Odd')

print_even(num)
