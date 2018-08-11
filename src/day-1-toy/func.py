# Write a function is_even that will return true if the passed in number is even.
def even_num(y):
    if y % 2 == 0:
        return y

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"

# So it reads it off the keyboard as a string?
# have to convert to num?

num = int(num)

if even_num(num):
    print("even")
else:
    print("odd")