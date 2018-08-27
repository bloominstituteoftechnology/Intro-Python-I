# Write a function is_even that will return true if the passed in number is even.
def f1(num):
    if num % 2 is 0:
        return "Even!"
    else:
        return "Odd"
# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
print(f1(num))
