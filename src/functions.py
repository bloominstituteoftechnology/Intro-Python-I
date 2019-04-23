# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(number):
    if number == 0:
        return 0
    elif number % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

result = is_even(num)
if result == True:
    print("Even!")
elif result == 0:
    print("Input was equal to Zero! Try again.")    
else:
    print("Odd")
