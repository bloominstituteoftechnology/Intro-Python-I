# Write a function is_even that will return true if the passed-in number is even.

def is_even():
    try:
        x = int(raw_input("Enter a number: "))
        if num % 2 == 0:
            return x, 'true'
        else:
            return x, 'false'

print is_even()

# YOUR CODE HERE
# type some code
# Read a number from the keyboard
#num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

number = int(input('Number: '))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")