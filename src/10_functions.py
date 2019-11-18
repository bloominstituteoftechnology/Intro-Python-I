# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(test):
    if(test % 2 == 0):
        print("Even")
        return True
    else:
        print("Odd")
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
is_even(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
