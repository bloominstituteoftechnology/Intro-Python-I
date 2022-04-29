# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(n):
    return 

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

# ---------------------------------------

# How do we define a function in Python?
def mult2(n):
    return n * 2

# we are defining a variable called num = 50
num = 50
print(mult2(num))

# define a function that receives a list of numbers
# and multiplies every number in the list by 2
# should this function affect the input list?
# or should it return a new list with the multiplied values?
def mult2_list(l):
    # affect the input list
    # iterate over every list element
    for i in range(len(l)):
        # update it to be equal to the current value * 2
        l[i] = l[i] * 2
        # (short hand version of this would be l[i] *= 2)

nums = [10, 60, 4, 15]
mult2_list(nums)
print(nums)

def mult2_new_list(l):
    #creates a new list with the updated values
    new_list = []

    for i in range(len(l)):
        new_list.append(l[i] * 2)

    # we need to return the "new_list" so that it can make its way outside of this function
    return new_list

    print(mult2_new_list([3, 5, 34, 10, 15]))