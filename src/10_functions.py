# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    if int(num) % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
result = is_even(num)
print(result)

# Print out "Even!" if the number is even. Otherwise print "Odd"
if num % 2 == 0:
    print("Even!")
else:
    print("Odd!")

