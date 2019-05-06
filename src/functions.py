# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
# def is_even(n):
#     if (n%2==0):
#         return True
# PM recommendation - it's less code and it's return True/False not only True
def is_even(n):
    return (n%2 == 0)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if is_even(num):
    print ('Even!')
else:
    print ('Odd')

