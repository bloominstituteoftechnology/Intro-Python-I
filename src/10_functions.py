# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False

print(is_even(2)) # Returns true
print(is_even(3)) # Returns false

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def is_EvenOrOdd(num):
    if (num % 2 == 0):
        print("Even!")
    else:
        print("Odd")

is_EvenOrOdd(num)
