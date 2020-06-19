# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def check_even(num):
    if num % 2 == 0: # <- this is the defenition of even
        return f"Number: {num} is even!"
    else:
        return f"Number: {num} is odd!"



# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE1

print(check_even(num))
