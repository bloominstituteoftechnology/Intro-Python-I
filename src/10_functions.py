# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even():
    if num % 2 == 0:
        return True

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if num % 2 == 0:
    print('even')
elif num % 3 == 1:
    print('odd')

