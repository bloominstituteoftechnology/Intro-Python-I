# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        print('yes, this is an even number...')
    else:
        print('bro, this number is odd')

is_even(num)
