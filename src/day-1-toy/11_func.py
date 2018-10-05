# Write a function is_even that will return true if the passed in number is even.
def even_check(a):
    return(a%2)==0

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
num = int(4)

if even_check(num):
    print("Even!")
else:
    print("Odd")

