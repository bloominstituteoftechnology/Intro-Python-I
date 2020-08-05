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

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.



# YOUR CODE HERE

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

# ------------------ CLASS WORK

# init an empty dict 
d = {}

# One primary use case is to associate keys with values
# Dicts provide very effcient fetching of keys
# Dicts provide de-duplication functionality since they never store duplicates of any keys

# Create a dict with two key-calue pairs
e = {"foo": 12, 111: "bar"}

# Print out the value 12 from the dict
print(e["foo"])
print(e[11])

# Iterate through dict ket pairs
for key in e:
    print(key, e[key])

# Iterate through  key valye pairs
for key, val in e.items():
    
