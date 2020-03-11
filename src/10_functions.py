# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    return True if num % 2 == 0 else False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
# is_even(num)

val = is_even(num)

if val == True:
    print(str(num) + " is even")
else:
    print(str(num) + " is odd")
