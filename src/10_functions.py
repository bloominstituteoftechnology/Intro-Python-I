# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        return "True"

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def print_is_even_is_odd(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")

print(print_is_even_is_odd(num))