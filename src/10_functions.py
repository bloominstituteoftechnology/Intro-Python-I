# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    return True if x%2 == 0 else False

while True:
# Read a number from the keyboard
    num = input("Enter a number: ")
    num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE

    eval = is_even(num)

    if eval:
        print('Even!')
    else:
        print('Odd')

    stop = input("Again? (y/n)")
    if str(stop) == 'n':
        break