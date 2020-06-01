import os

# print(f"Hello {os.getlogin()}. How are you?")
print(f"Hello {str(os.getlogin())}")




# create an empty list 

# set the empty list to a variable p

p = []

​

# create a list with numbers 

q = [1, 2, 3, 4, 5, 6]

​

# add a number to our q list 

q.append(77)

​

# where is the appended value getting to the list? 

# print(q)

​

# `append` method adds to the end of the list 

​

# what if we append to the beginning of a list? 

q.insert(0, 90)

​

# print(q)

​

# how to print out all the elements of a list 

# let's use a for loop to do this 

# for elem in q:

#     print(elem)

​

# combine our above loop with string interpolation

# to print a short message with each list element 

# for elem in q:

#     print(f'Element: {elem}')

​

# print each list element with a short message that 

# also tells us the element's index in the list 

# the `enumerate` function gives us access to each 

# list element as well as its index 

# for i, elem in enumerate(q):

#    print(f'Index: {i}, Element: {elem}') 

​

# `_` in Python denotes "I'm tossing this value"

# for _ in q:

​

# In Python, how do we loop a certain number of times?

# We can use the `range` function for this

# range(start=0, end, step=1)

# range is exclusive on the `end`

# for num in range(1, 11, 3):

#     print(num)

​

# use `range` in conjunction with lists to iterate 

# over the length of a list 

# for index in range(len(q)):

#     print(q[index])

​

# how do you loop through a range backwards? 

# if we want to loop from 10 down to 1

# for i in range(10, 0, -1):

#     print(i)

​

# how can I loop past the length of a list?

for i in range(20):

    # if i is in bounds of our list

    if i < len(q):

        print(q[i])

    # otherwise we're past the bounds of our list 

    else:

        print(i)

