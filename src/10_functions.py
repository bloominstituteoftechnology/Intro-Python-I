# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    return (True if n % 2 == 0 else False)
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
absNum = abs(num)
print(absNum)
x = is_even(absNum)
print(x)
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
print('Even!' if (x) else 'Odd')
