# Write a function is_even that will return true if the passed-in number is even.


def is_even(a):
    if round(int(a)/2) * 2 == int(a):
        return print('Even!')
    return print('Odd')


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

is_even(num)
