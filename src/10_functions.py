# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(a):
    if a % 2 == 0:
        return True
is_even(4)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def is_it_even(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")
is_it_even(num)