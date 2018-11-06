# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = int(input("Enter a number: "))

def is_even(num):
    if num%2:
        print('Odd!')
    else:
        print('Even!')

is_even(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"