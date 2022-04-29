"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []

starting_array = [y for y in range(6) if y > 0 ]
#*result*  = [*transform*    *iteration*         *filter*     ]


print(starting_array)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

cubic_comprehension = [i**3 for i in range(10)  ]
#*result*  = [*transform*    *iteration*         *filter*     ]


print(cubic_comprehension)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a_list_of_str = ["foo", "bar", "baz"]

# Define intense_string
def intense_string(string, intense=False):
    """can make all letters capitol in a string"""

    # Make string uppercase if intense is True
    if intense is True:
        # Make uppercase
        string_upper = string.upper()
    else:
        # if intense is false
        string_upper = string

    # Return echo_word_new
    return string_upper

  """can make all letters capitol in a string"""

    # Make string uppercase if intense is True
    if intense is True:
        # Make uppercase
        string_upper = string.upper()
    else:
        # if intense is false
        string_upper = string

    # Return echo_word_new
    return string_upper


for i in a_list_of_str: 
  print(intense_string(i , intense=True))

#y = []

#print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.
input_number = int(input("Enter a number :"))
numbers  = [i           for i in range(input_number)   if i % 2 == 0]
print(numbers)

# What do you need between the square brackets to make it work?
#y = []

#print(y)