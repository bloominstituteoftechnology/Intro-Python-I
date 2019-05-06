# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if x%2 == 0:
        return True

print(is_even(2))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def what_is_it(num):
    if num%2 == 0:
        print("Number Is Even!")
    else:
        print("Number Is Odd!")

what_is_it(num)
