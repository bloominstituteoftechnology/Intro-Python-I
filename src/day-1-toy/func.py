# Write a function is_even that will return true if the passed in number is even.
def isEven(x):
    return int(x)%2==0
# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
if isEven(num):
    print("Even!")
else:
    print("Odd")