# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")
number = int(num)

def is_even(number):
    if (number % 2 == 0):
        print("Even!")
    else:
        print("Odd")
# Print out "Even!" if the number is even. Otherwise print "Odd"

is_even(number)