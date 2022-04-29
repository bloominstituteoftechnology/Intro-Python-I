# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(sumnum):
    if sumnum % 2 == 0:
        return True
    elif sumnum % 2 == 1:
        return False


print(is_even(1))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if num % 2 == 0:
    print("Even!")
elif num % 2 == 1:
    print("odd")
