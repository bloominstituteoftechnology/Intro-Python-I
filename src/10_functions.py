# Write a function is_even that will return true if the passed-in number is even.

def is_even(x):
	if x % 2 == 0:
		return True


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print("is_even", is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"
if is_even(num):
	print("is_even Even!")
else:
	print("is_even Odd")
