# Write a function is_even that will return true if the passed-in number is even.

def is_even(number):
    if number % 2 == 0:
        print(number, "is even")
        return True
    return False

# YOUR CODE HERE
# type some code
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

print(is_even(num))