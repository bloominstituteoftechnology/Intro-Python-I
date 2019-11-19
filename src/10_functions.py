# Write a function is_even that will return true if the passed-in number is even.


def isEven(x):
    return(x % 2 == 0)


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
if isEven(num) == True:
    print("Even!")
else:
    print("Odd")
