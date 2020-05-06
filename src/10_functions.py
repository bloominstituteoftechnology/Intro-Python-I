# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def even(number):
    return number % 2 == 0
    print(even(13), '\n')
    print(even(82), '\n')


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
print("Even" if even(num) is True else "Odd")
