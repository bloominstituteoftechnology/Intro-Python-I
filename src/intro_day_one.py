# if statements
#in python, whitespace is important
# name = "Sean"

# if name != "Sean":
#     print("Hey, you aren't Sean")
# else:
#     print(f"Hello {name}")


#in python, arrays are called "lists"

#create an empty list

# empty = []

#create a list with numbers

# nums = [2, 5, 6, 7]
# print(nums)

# add a number to our nums list
# nums.append(11)

# let't print nums
# print(nums)


# let's print out every value int he numbs list, one at a time
# for i in nums:
#     print(i)


# what if we want to print along the length of a list?
# for i in range(len(nums)):
#     print(i)

# to get value with its associated index
# for i in range(len(nums)):
#     print(i, nums[i])


# another way to print our the elements from a list with their associated index
# for i, v in enumerate(nums):
#     print(i, v)


# how do we define a function in python
# def mult2(n):
#     return n*2
# n = 50

# print(mult2(n)) # this prints 100


# define a function that receives a list of numbers and multiplies every number by 2
# should this function affect the input list?
# or should it return a new list with the multiplied values
# 

# def mulby_2(l):
#     # affect the input list, iterate through evey value and multiply by 2
#     for i in range(len(l)):
#         l[i] *=2

# nums = [2, 4, 5, 7]

# mulby_2(nums)
# print(nums)


# to return a new list without affecting the old one
def mulby_2_new(l):
    # creates a new list with updated values
    new_list = []

    for i in range(len(l)):
        new_list.append(l[i]*2)
    return new_list

nums = [2, 4, 5, 7]
print(mulby_2_new(nums))

