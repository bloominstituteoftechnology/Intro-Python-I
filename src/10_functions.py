# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    if n == 0:
        print("Your number is not odd nor even....It's just 0")
    elif n % 2 == 0:
        print("even")
    else:
        print("odd")

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
is_even(num)

