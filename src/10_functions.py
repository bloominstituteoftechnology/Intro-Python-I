# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if x % 2== 0 :
        return True
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
is_even(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"
def is_odd(x):
    if x %2 ==0:
        print("Even!")
    else :
        print("Odd")
# YOUR CODE HERE
is_odd(num)
