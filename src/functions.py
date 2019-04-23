# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(n):
    if int(n) % 2 == 0:
        print('is even')
        return True
    else:
        print('is odd')
        return False
        

is_even(2)
is_even(7)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def check_even(num):
    if num % 2 == 0:
        print("Even!")
    else: 
        print("Odd")


check_even(num)


