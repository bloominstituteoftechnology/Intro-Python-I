# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
# Read a number from the keyboard
num = input("Enter a number: ")
print(num)
print(type(num))
num = int(num)
print(type(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def is_even(value):
    if value % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(num))
