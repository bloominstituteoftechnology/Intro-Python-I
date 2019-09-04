# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)


def is_even(num):
    if num %2 == 0:
        return True
    else:
        return False
            





print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_odd(num):
    if num %2 == 0:
        return "Even"
    else:
        return "Odd"
            
print(is_odd(num))

