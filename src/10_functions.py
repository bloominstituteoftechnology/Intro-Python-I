# Write a function is_even that will return true if the passed-in number is even.

def is_even(x):
    isEven = False
    if x % 2 == 0:
        isEven = True
    return isEven

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

check = is_even(num)
if check == True:
    print("Even!")
else:
    print("Odd")

