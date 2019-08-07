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
