# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
def is_even(n):
    if (n % 2 == 0):
        print("Even!")
    else:
        print("Odd")

num = input("Enter a number: ")
is_even(int(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"