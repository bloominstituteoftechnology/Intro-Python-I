# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard

# Print out "Even!" if the number is even. Otherwise print "Odd"

def is_even():
    '''
    Asks user for a number and prints whether it is even or odd
    '''

    # takes user input string
    num = input("Enter a number: ")
    
    # converts user input string to an int
    num = int(num)
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

is_even()
