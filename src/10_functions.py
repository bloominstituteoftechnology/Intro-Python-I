# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if(int(num) % 2 == 0):
        return True
    else:
        return False

def confirm_even(fn_value):
    if(fn_value):
        print("Even!")
    else: 
        print("Odd!")

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
confirm_even(is_even(num))

