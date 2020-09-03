# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(new_num):
    if new_num % 2 == 0:
        return True

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def even_or_odd(some_number):
    if some_number % 2 == 0:
        print("Even!")
    else: 
        print("Odd")

even_or_odd(num)

