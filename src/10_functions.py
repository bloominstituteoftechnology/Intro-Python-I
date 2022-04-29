# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# Divisible by 2 = even

def is_even(n):
    answer = 'It is even!' if n % 2 == 0 else 'It is odd :('
    print(answer)

is_even(4)

