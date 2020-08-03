"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
#[expression for item in list]

#number_list = [ x for x in range(20) if x % 2 == 0]
#print(number_list)

array1 = [ y for y in range(6) if y > 0]
print(array1)



# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

#[expression for item in list]

array2 = [ y**3 for y in range(10)]
print(array2)




# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

#array3 = [ y for y in range(3) if y.upper()]

array3 = [ a[y].upper() for y in range(len(a))]
print(array3)

upper_lambda = lambda x: x.upper()
lambda1 = upper_lambda(a[0])

print(lambda1)

array5 = [ upper_lambda(a[y]) for y in range(len(a))]
print(array5)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

str_x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?

#obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
#print(obj)
even_array1 = [ int(str_x[y]) for y in range(len(str_x)) if int(str_x[y]) % 2 == 0]
print(even_array1)


