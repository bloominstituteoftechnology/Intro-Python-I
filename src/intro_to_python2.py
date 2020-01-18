""" Intro to Python II - Guided Project
    This document contains examples for CS Intro to Python, module 2. Examples
    will highlight unique syntax rules in Python. Students will continue to
    practice creating elements such as lists, dictionaries, and functions. 
    Additionally, we will look at the CS problem-solving framework and practice
    using it to break down more complex problems.
"""
# RECAP: How do we...
# create a list of floating point temperatures?
temps = [54.2, 56.3, 101.3, 99.7]

# in a single line, create a new list containing all of the temperatures from
# the above list that are greater than 90.0?
hot_temps = [t for t in temps if t > 90.0]

# create a dictionary students in which their `id` is the key and their name
# is the `value`?
students = {}

# add a new student to our dictionary? 
students[4050]="Josh"
students[3045]="James"
print(students)

# modify an existing student entry?
students[1023]="Tom"
print(students)

# When we write functions in different languages, it is important to know if
# arguments are passed by REFERENCE or VALUE.
n=5 
nums = [1,2,3]

def mult2(x): # x is a single integer value to be doubled
    return x * 2
    

def mult2_list(x): # x is a list of integer values to be doubled
    for i in range(len(x)):
        x[i] *= 2

print(mult2(n))
print(n)

mult2_list(nums)
print(nums)

# UPER - Given a number of people, number of pizzas, and number of slices per
# pizza, write a function to evenly divide the slices between each person.
# 1. Understand
# - How do we know #s? (passed as args in fuction)
# - Is everyone eating? (yes)
# - Min/Max (positive int values)
# - Half slices? (no)
# - Cost per slice? (n/a)
# - Slices same size? (yes)
# - Return # slices per person? (yes + # of leftovers that no one gets) 

# 2. Plan
#def divide_pizza(people, pizzas, slices):
    # Find total num of slices (pizza*slice)
    # Do division
        # Find "floor" (slices per person)
        # Find remainder (leftovers)
    # Return info as string

# 3. Execute
def divide_pizza(people, pizzas, slices):
    total_slices = pizzas * slices
    # Do division
    slices_per_person = total_slices // people
    leftovers = total_slices % people

    # Return info as string
    return f'Each person gets {slices_per_person} slices and there are {leftovers} extra'

print(divide_pizza(4,2,8))
print(divide_pizza(5,3,8))
# 4. Reflect


# UPER - Prompt a user to enter three, uique numbers as input, print out 
# which number is the largest of the three. 
# 1. Understand
    # - are all the numbers different/duplicates?
    # - lists items
    # - reference numbers back 
    # - set 
# 2. Plan
    # - We have to return the largest of the three
# 3. Execute
def calc_largest():
    # TODO
    pass
# 4. Reflect
# UPER - Write a function that returns the "centered" average of an array of 
# ints, which we'll say is the mean average of the values, except ignoring the 
# largest and smallest values in the array. 
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3
# 1. Understand
# 2. Plan
# 3. Execute
def centered_average(nums):
    # TODO
    pass
# 4. Reflect