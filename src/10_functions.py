# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        return "True"

is_even(num = 4)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
def print_even_or_odd(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")

print_even_or_odd(num)

# YOUR CODE HERE

