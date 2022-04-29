print('Hello World')

# Print statement with string variable
name = 'Felix'
print('Hello, ' + name)

# Print statement with functional string
print(f'Hello, {name}')

# lists
l = []

# creat list with numbers
num_list = [1, 2, 3, 4]

# ad element to empty list
l.append(77)

# print all values in the num_list
for element in num_list:
    print(element)

# enumerate returns a tuple with the index number, value
for (i, elem) in enumerate(num_list):
    print(f'Element {i} is {elem}')

# how to print in a range, defaults to start at 0 to stay consistent
# with zero indexing
for x in range(10):
    print(x)

# list comprehension
numbers = [1, 2, 3, 4, 5]
print(numbers)

# long way
squares = []
for num in numbers:
    squares.append(num*num)
print(squares)

# with list comprehension
squares2 = [num*num for num in numbers]
print(squares2)

# lets do only even numbers
evens = [num for num in numbers if num % 2 ==0]
print(evens)

# create a new list containing only the names that start with 's' so that
# they are properly capitalized (regardless of how the name originally appears)

names = ['Sarah', 'Jorge', 'sam', 'bobby', 'steph']

# To explain this we are iterating along all the entries in the names list, 
# then using a conditional to check the first letter of that name, lower cased, 
# to see if it is an 's', then we keep that name and capitalize it.
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)

# dictionaries
d = {}

dict2 = {'foo': 12, 'bar': 20}

print(dict2['bar'])

for k in dict2:
    print(f'{k} is {dict2[k]}')