# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(val):
    return True if val % 2 == 0 else None


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if is_even(num):
    print("Even")
else:
    print("Odd")
