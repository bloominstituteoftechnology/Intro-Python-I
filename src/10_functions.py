# Write a function is_even that will return true if the passed-in number is even.

def is_even(number):

    '''Takes in an input, checks if it is an integer. If it is,
    it returns true if the integer is even. Otherwise it returns false
    if the integer is not even.'''

    if type(number) != int:
        return "This is not an interger"

    if number % 2 == 0:
        return 'True'

    else:
        return 'False'

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if num % 2 == 0:
    print('Even!')
else:
    print('Odd')
