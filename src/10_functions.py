# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def even(num): 
    print(num % 2 == 0)


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def even_odd(num):
    if num == 0:
        print('enter an even or odd number')
    elif num % 2 == 0:
        print('Even!')
    else:
        print('Odd!')

print(even_odd(2))