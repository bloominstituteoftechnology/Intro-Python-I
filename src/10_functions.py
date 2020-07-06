# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(thing):
    print(bool(thing%2 == 0))
    
is_even(32)
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

print("Even!" if (num%2 == 0) else "Odd")