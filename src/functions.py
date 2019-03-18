# Write a function is_even that will return true if the passed-in number is even.

def iseven(x):
    return x % 2 == 0

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def printevenodd(x):
    if iseven(x):
        print("Even!")
    else:
        print("Odd")

printevenodd(num)