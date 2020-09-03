#https://www.youtube.com/watch?v=Q6WyXTFLerw
#https://code4coding.com/python-program-to-check-a-number-is-even-or-odd/
# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HEREv

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_even(num):
    if num % 2 == 0:
        print(f"Number {num} is even!")
    else: 
        print(f"Number {num} is odd.")

#Function call
is_even(num)

"""
14
prints: Number 14 is even!
"""