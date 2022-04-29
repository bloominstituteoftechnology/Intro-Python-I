# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
while True:
    def is_even(n):
        if (not n % 2):
            return n
    # Read a number from the keyboard
    num = input("Enter a number: ")
    num = int(num)

    # Print out "Even!" if the number is even. Otherwise print "Odd"

    # YOUR CODE HERE
    if is_even(num):
        print("Even!")
    else:
        print("Odd")