# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if (num % 2 == 0):
        print("true")
    else:
        print("false")

is_even(13)
is_even(12)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def even_or_odd(num):
    if (num % 2 == 0):
        print("Even")
    else:
        print("Odd")


even_or_odd(num)
