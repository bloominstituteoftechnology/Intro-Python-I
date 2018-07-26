# Write a function is_even that will return true if the passed in number is even.
def is_even(num):
  if int(num) % 2 == 0: # convert to int before calculating
    return True


# Read a number from the keyboard
num = input("Enter a number: ")
# Input from user is interpreted as string, need to convert to int

# Print out "Even!" if the number is even. Otherwise print "Odd"
if is_even(num) == True:
  print("EVEN!")
else:
  print("Odd.")
