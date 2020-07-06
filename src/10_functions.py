# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number_list):
    for i in number_list:
        if i % 2 == 0:
            return "Even"
        else: 
            return "Odd"
x = [1]
y = [2]
print(is_even(x))
print(is_even(y))

# Read a number from the keyboard
num = input(12)
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def is_even(number_list):
    for i in number_list:
        if i % 2 == 0:
            return "Even"
        else: 
            return "Odd"

print(is_even(num))