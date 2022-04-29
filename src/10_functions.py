# Write a function is_even that will return true if the passed-in number is even.
# n % 2 ==0 checks for an even number. If it is divided by 2 and doesn't have a remainer, print True! 

def is_even(n):
    if n % 2 == 0:
        return True

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num) == True:
    print("Even!")
else:
    print("Odd")

