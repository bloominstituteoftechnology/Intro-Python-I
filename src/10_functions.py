# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even = [num for num in numbers if num % 2 == 0]
print(is_even)
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if (num % 2) == 0:
    print("{0} Even!".format(num)) ## remove {0} just to show odd/even
else:
    print("{0} Odd".format((num)))

