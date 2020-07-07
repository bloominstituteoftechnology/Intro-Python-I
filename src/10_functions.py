# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(is_even(2))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
numInput = num % 2

if numInput > 0:
    print("Odd")
else: 
    print("Even!")


