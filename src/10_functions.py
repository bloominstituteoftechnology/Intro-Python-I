# Write a function is_even that will return true if the passed-in number is even.

def is_even(n):
    if n%2:
        return 'False'
    else:
        return 'True'

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even(n):
    if n%2:
        return 'Odd'
    else:
        return 'Even!'

num = input("Enter a number: ")
print(is_even(int(num)))

