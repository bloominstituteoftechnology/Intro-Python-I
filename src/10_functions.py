# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


##
def test(a,b=10):

    def test2():
        print("Inner function")

    print("A and B are",a,b)
    test2()
    return 0



test(20,30)

