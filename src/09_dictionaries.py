#Notes
# # create a new empty dictionary
# d = {}

# # create a dictionary with at least 2 key : value pairs
# d = {'apple': 'is a fruit', 'cucumber': 'is a vegetable '}

# # access & print an element in the dictionary
# print(d['apple'])

# #iterate throu dictionary
# for key, value in d.items():
#     print(f'{key}: {value}')


# # Tuples vs. Lists
# ls = [1, 2, 3, 4] # List
# tup = (1, 2, 3, 4) # Tuple

# ls[3] = 5
# for item in ls:
#     print(item)

# tup[3] = 5 # Can not be immutable. Similar to setting to const vs let  
# for item in tup:
#     print(item)


# # Set
# s = {'a', 'b', 'c'}
# s.add('d')
# s.remove('a')
# for item in s:
#     print(item)
# if 'a' in s:
#     print('a is in the set')
# if '7' not in s:
#     print('no numbers')


"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE

waypoints.append({"lat": 20, "lon": 20, "name": "a different place"})
print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE

for i in waypoints:
	if i["name"] == "a place":
		i["name"] = "not a real place"
		i["lon"] = -130
print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for item in waypoints:
	print(item.values())