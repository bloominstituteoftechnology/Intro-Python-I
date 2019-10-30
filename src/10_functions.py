# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def boolean(i):
    if i % 2 == 0:
        return True
    else:
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def f(i):
    if boolean(i):
        print("Even!")
    else:
        print("Odd")


f(num)
