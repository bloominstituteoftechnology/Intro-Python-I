# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
num = input("Enter a number: ")
num = int(num)

def even_stevens(x):
    if x%2==0:
        print("Even!")
    elif x%2!=0:
        print("Odd!")
    else:
        print("Not applicable!")

even_stevens(num)




