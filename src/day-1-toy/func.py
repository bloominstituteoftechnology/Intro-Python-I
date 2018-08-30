# Write a function is_even that will return true if the passed in number is even.
def evenCheck(num):
    if (int(num) % 2 == 0):
        print("true")
    else: print("odd")
# Read a number from the keyboard
num = input("Enter a number: ")
evenCheck(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"
