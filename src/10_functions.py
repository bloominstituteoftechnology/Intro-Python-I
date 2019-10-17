# Write a function is_even that will return true if the passed-in number is even.

def is_even(x):
    if x%2==0:
        return True
    else:
        return False


print(is_even(3))
# YOUR CODE HERE


# Read a number from the keyboard

# x='hello'
# print(x.isnumeric())



# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def my_function():
    x='string'
    while x.isnumeric()==False:
        x=input("please input a number here:")
    if x.isnumeric()==True:
        if float(x)%2==0:
            print("Even!")
        else:
            print("Odd")
        


my_function()