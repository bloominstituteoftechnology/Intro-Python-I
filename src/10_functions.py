# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

num = input("Enter a number: ")
def is_even(num):
    # Read a number from the keyboard
    num = int(num)
    if num % 2 == 0:
        print("true")
is_even(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"
def is_even_or_odd(num):
    # Read a number from the keyboard
    num = int(num)
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")
is_even_or_odd(num)

# YOUR CODE HERE
