# Write a function is_even that will return true if the passed in number is even.
def is_even(n):
    return n % 2 == 0

# Read a number from the keyboard
num = int(input("Enter a number: "))

# Print out "Even!" if the number is even. Otherwise print "Odd"
if is_even(num):
    print("Even!")
else:
    print("Odd")

# print("Even!" if is_even(num) % 2 == 0 else "Odd")