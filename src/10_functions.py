# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(numbers):
    if numbers % 2 == 0 :
        return True
    else:
        return False


# Read a number from the keyboard
num = int(input("Enter a number: "))
num2 = num % 2

# Print out "Even!" if the number is even. Otherwise print "Odd"
if num2 > 0:
     print("This is an odd number")
else:
    print("This is an even number")
# YOUR CODE HERE
