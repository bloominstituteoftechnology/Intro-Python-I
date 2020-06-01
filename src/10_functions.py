# Write a function is_even that will return true if the passed-in number is even.

def is_even(some_number):
    if some_number % 2 == 0:
        return True

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num) is True:
    print('Even!')
else:
    print('Odd')
