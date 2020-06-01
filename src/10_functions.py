# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
# define a function by def
def is_even(x):
    if x % 2 == 0:
        return True # in order to work we need to add a 4times space bar, otherwise it is giving us an indentation message 

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
result = is_even(num)

if result:
    print("Even!")
else:
    print("Odd")
