# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

num = input("Enter a number: ")
num = int(num)

def is_even(num):
    if num % 2 == 0:
        print(f'{num} is even')
        return True #has to be capitalized or undefined 
    else:
        print(f'{num} is odd')
        return False #has to be capitalized or undefined 


print(is_even(10))
print(is_even(97))
# Read a number from the k eyboard

"""
works!
if (num % 2) == 0:
    print(f'{num} is even')
else:
     print(f'{num} is odd')

"""


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

