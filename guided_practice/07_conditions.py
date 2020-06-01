"""
Conditions
"""

# # 1. Comparing or evaluating expressions
x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

# # 2. "and" & "or"
name = "Sean"
age = 31
if name == "Matt" and age == 31:
    print("Your name is Matt, and you are also 31 years old.")

if name == "Matt" or name == "Sean":
    print("Your name is either Matt or Sean.")

# # 3. "in"
name = "Matt"
if name in ["Matt", "Sean"]:
    print("Your name is either Matt or Sean.")

# # 4. "if", "elif", "else"
statement = False
another_statement = True
if statement is True:
    # do something
     pass
 elif another_statement is True:  # else if
     print("another statement is True")
     pass
 else:
     # do another thing
     pass

# # 5. "is" matches instances and not values
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False

# # 6. "not" inverts a boolean
print(not False)  # Prints out True
print((not False) == (False))  # Prints out False


"""
YOU DO
3 minute timer
"""
# # Modify the supplied code so that all of the statements evaluate to True
# # change this code
number = 5
second_number = 5
first_array = [number - 2, number-1,number]
second_array = [3, 4, 5]

print(bool(number > 15))

print(bool(first_array))

print(len(second_array) == 2)

print(len(first_array) + len(second_array) == 5)

print(first_array and first_array[0] == 1)

print(not second_number)
