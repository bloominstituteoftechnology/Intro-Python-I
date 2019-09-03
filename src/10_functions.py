# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    print(num, 'num')
    if (num % 2) == 0:
        return True
    else:
        return False


print(is_even(10))
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
if (num % 2) == 0:
    print(f"{num} is even")
else:
    print("{num} is odd")

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
