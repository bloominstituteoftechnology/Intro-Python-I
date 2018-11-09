# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


def even_or_odd():
    if num % 2 == 0:
        return str(num) + " is even."
    else:
        return str(num) + " is odd."


print(even_or_odd())

