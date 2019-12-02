# Write a function is_even that will return true if the passed-in number is
# even.

# YOUR CODE HERE


def is_even(n):
    '''Take in a number and determine if it is even or not'''
    assert(n > 0)
    if n % 2 == 0:
        return True
    else:
        return False


# Read a number from the keyboard
# num = input("Enter a number: ")
# num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


# YOUR CODE HERE
def print_wrap():
    num = input("Enter a number: ")
    num = int(num)
    outs = is_even(num)
    if outs is True:
        print('Even!')
    else:
        print('Odd')


print_wrap()
