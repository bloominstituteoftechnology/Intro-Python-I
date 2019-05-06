# Write a function is_even that will return true if the passed-in number is even.
def is_even(num):
    if num % 2 == 0:
        return True


print(is_even(4))

# YOUR CODE HERE
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
print('even') if num % 2 == 0 else print('odd')
