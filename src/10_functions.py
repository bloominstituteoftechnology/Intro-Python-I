# Write a function is_even that will return true if the passed-in number is even.
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        print("Even!")
        return True
    else:
        print("Odd")
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

is_even(num)
