# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")


def is_even(value):
    if int(value) % 2 == 0:
        return True
    else:
        return False


print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"


def is_even2(value):
    if int(value) % 2 == 0:
        print('Even')
    else:
        print('Odd')


is_even2(num)
