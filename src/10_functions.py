# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def isEven(num):
    if num %2 == 0:
        return True
    return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


# YOUR CODE HERE
def printOut(number):
    if isEven(number):
        print("Even!")
    else:
        print("Odd")

printOut(num)