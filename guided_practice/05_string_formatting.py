"""
String Formatting
"""

# 1. The "%" operator is used to format a set of variables
# enclosed in a "tuple", together with a format string,
# which contains normal text together with "argument specifiers",
# special symbols like "%s" and "%d".

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# # 2. To use two or more argument specifiers, use a tuple (parentheses)
 # This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# 3. Any object which is not a string can be formatted
# using the %s operator as well

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers
# with a fixed amount of digits to the right of the dot.

# This prints out: A list: [1, 2, 3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)
 