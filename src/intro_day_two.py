# JS objects
# swift dictionaries
# java hashmaps?

# init a empty dict
# c = {}

# one primary use case is to associate 
# dicts provide very efficient fetching of keys
# dicts provide de-duplication functionality since they
# never store duplicates of any keys






#create a dict with two key-value pairs

# e = {"foo":12, 11:"bar" }

# #print out the value 12 from the dict

# print(e["foo"])
# print(e[11])

# #we can also iterate through dict key pairs
# for key in e:

#     print(key, e[key])


# #iterate through key value pairs
# for key, val in e.items():
#     print(key, val)
#     #also interpolation
#     print(f"Key is {key} and val is {val}")


#the `items` methodon dicts is similar to the  `enumerate` function for lists in that both 
# give you access to index-value/key-value



##############################
#store all even numbers in the rance 0-100 in a list
#what are some ways we can do this

# evens = []

# #loop through the range
# for i in range(101):
#     #check if the current number is even
#     if i % 2 == 0:


#     #if so, added to the `evens` list
#         evens.append(i)
    

# print(evens)
# # comprehensions allo us to write the above logic in a much more terse fashion
# even = [ i for i in range(101) if i % 2 == 0 ]
# print(even)

# print(evens == even)
##############################

##############################
#create a list of the square values of numbers in the range 1-10
# square = []
# for i in range(1, 11):
#     square.append(i**2)
# print(square)

# list comprehension version
# s = [i**2 for i in range(1, 11)]
# print(s)
##############################

##############################
#create a new list containing only the names that start with `s`
# and also make sure all of the names are properly capitalized
# names = ["Sarah", "jorge", "sam", "frank", "sandy"]
# s_names = []
# for name in names:
#     #check if the names starts with s
#     if name [0].lower() == 's':
#         s_names.append(name.capitalize())
# print(s_names)
# #in list comprehension
# snames = [name.capitalize() for name in names if name[0].lower() == 's' ]
# print(snames)
##############################

##############################
#comprehensions work just as well with dicts
#populate a fict with all the letter of the alphabet with their corresponding place in alphabet

letters = 'aeuiu'

# alpha = {}
# for i, letter in enumerate(letters):
#     alpha[letter] = i +1

#     print(alpha)
# # in list comprehsension version

alphas = {letter: i+1 for i, letter in enumerate(letters)}
print(alphas)
##############################
