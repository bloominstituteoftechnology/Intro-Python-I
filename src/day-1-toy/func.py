# Write a function is_even that will return true if the passed in number is even.
def is_even(n):
    return n % 2 == 0

print(is_even(2))
print(is_even(3))
print(is_even(8))
print(is_even(9))
# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
# perhaps we can use a ternary statement; would be cleaner, right?
# a if condition else b

odd_or_even = "Even!" if int(num) % 2 == 0 else "Odd"

print(odd_or_even)