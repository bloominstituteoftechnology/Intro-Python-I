# Write a function is_even that will return true if the passed in number is even.
def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

print(is_even(40))

# Read a number from the keyboard
num = input("Enter a number: ")
print("The number you entered is", num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
def odd_or_even(num):
  if num % 2 == 0:
    return "Even!"
  else:
    return "Odd!"

print(odd_or_even(142))
print(odd_or_even(131))