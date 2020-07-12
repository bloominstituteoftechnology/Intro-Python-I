# Using List Comprehensions

# Create a new list containing the squares of all values in 'numbers'
numbers = [1, 2, 3, 4, 5]
print(numbers)

# The long way
squares = [num*num for num in numbers]
# for num in numbers:
#     squares.append(num*num)
print(squares)

# create a new list containing only even values of 'numbers'

evens = [num for num in numbers if num % 2 == 0]
print(evens)

evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
        print(evens)

# Create a new list containing only the names that start with 's' so they are
# propererly capitalized(regardless of how the name originally appears)

names = ["Sarah", "Jorge", "sam", "bobby", "steph"]
s_names = [name.capitalize() for name in names if name[0].lower() =='s']
print(s_names)

