# Write a function is_even that will return true if the passed-in number is even. DONE

# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def num_even(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")

print(num_even(3))