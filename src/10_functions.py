# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if (x % 2) == 0:
        return True
    return False
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(is_even(num))
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_even2(x):
    if (x % 2) == 0:
        print("Even!")
    else:
        print("Odd")

# num = input("Enter a number: ")
# num = int(num)
print(is_even2(num))