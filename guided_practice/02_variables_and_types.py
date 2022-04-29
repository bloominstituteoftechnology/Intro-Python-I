"""
Variable and Types
"""
# # 1. Integers
myint = 9
print(myint)

# # 2. Floating point numbers
myfloat = 7.245
print(myfloat)
myfloat = float(7)
print(myfloat)

# # 3. Strings can use " or '
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# # 4. Apostophes
mystring = "Don't worry about apostrophes"
print(mystring)

# # 5. Simple Operations
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# 6. Simultaneous assignemnt
a, b = 3, 4
print(a, b)

# # 7. Can avoid temp pattern
a = 3
b = 4
print(a, b)
temp = a
a = b
b = temp
print(a, b)

a = 3
b = 4
print(a, b)
a, b = b, a
print(a, b)

# 8. Mixing operators with strings and numbers
# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)
        