# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard

# Print out "Even!" if the number is even. Otherwise print "Odd"

num = int(input("Enter a number: "))

def is_even():
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")

# call the function!
is_even() 