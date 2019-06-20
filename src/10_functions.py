# Write a function is_even that will return true if the passed number is even.

# YOUR CODE HERE


def is_even(number):
    if number % 2 == 0:
        return "true"
    else:
        return "false"

# Read a number from the keyboard

num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

result = is_even(num)

if result == "true":
    print("Even!")
else:
    print("Odd")
