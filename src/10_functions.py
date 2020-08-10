# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    if num % 2 == 0:
        print('true')
    else:
        print('false')


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
is_even(num)


def is_evenn(num):
    if num % 2 == 0:
        print('EVEN')
    else:
        print('ODD')


num = input("Enter a number: ")
num = int(num)

is_evenn(num)
