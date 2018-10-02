# Write a function is_even that will return true if the passed in number is even.
def is_even(item):
    if item % 2 == 0:
        return True

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
num = int(num)

if is_even(num):
    print("Even!")
else:
    print("Odd")