# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if int(num) % 2 == 0:
        return True
    return False


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_even2 ( num ):
    if (num % 2 == 0):
        print('Even!')
        
    else:
        print('Odd')


num = input("Enter a number: ")
num = int(num)
is_even2(num)
print(is_even(num))


