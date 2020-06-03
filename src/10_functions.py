# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def oddOrEven(x):
    try: int(x)
    except: print("that is not a number")
    else:
        y = int(x)
        if (y == 0 or (y % 2) == 0):
            print("Even")
        else:
            print("Odd")

oddOrEven(num)

