# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num): 
    if num % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
print(is_even(num))

if is_even(num) == True:
    print("Even")
else:
    print('ODD')

# YOUR CODE HERE

