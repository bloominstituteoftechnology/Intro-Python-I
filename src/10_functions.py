# Write a function is_even that will return true if the passed-in number is even.
# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        return num
    else:
        pass


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
if is_even(num):
    print("Even!")
if not is_even(num):
    print("Odd")

# Read a string from the keyboard
s = input("Enter some characters: ")

# Write a function that reverses the input string s
# YOUR CODE HERE


def reverse(string):
    return string[::-1]


print(reverse(s))
