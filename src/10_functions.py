# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number):
    """Checks if a number is even or odd. Returns True if even, False if odd."""
    ret = False
    if number % 2 == 0:
        ret = True
    
    return ret

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if is_even(num):
    print("Even!")
else:
    print("Odd")
