## Personal notes while learning python

#console.log in js
name = "Jesse" # creates a new variable(let, const, var in js terms)
print("Hello," + name)


# creates a variable
name = "Jesse"


# create an empty list
p = []

# create a list with some numbers
q = [10, 60, 20, 5]

# add an element to p
print(p)
p.append(77)
print(p)


# print all values in each list for loop example
for (index, element) in enumerate(q):
    print(f'{index}: {element}')
print(enumerate(q))

# if statement in one line
evens = [num for num in numbers if num % 2 == 0]

# dictionaries
d = {} # create a new dictionary

d = {'apple': 'is a fruit', 'cucumer': 'is a vegetable'} # dictionary example with two key value pairs

print(d['apple']) # access & print an element in the dictionary

# iterate through dictionary
for key, value in d.items():  # key is what we're referring to in the dictionary, can be called whatever you want.
    print(f'{key}: {value}')