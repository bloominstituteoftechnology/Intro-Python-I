x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12
print(x + int(y))

# Write a print statement that combines x + y into the string value 57
my_x = str(x)
if my_x + y == "57":
    print(my_x + y)
else:
    print("Test failed. We are not both strings")