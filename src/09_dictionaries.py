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
waypoints.append({"lat": 100, "lon": -10, "name": "Nate's house"})
print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.
waypoints[0]['name'] = 'not a real place'
waypoints[0]['lon'] = -130
print(waypoints)

# YOUR CODE HERE

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for num in range(len(waypoints)) :
    print(waypoints[num])


# One primary use-case is to associate keys with values
# Dicts provide efficient fetching of keys
# e = {"foo": 11, 10: "bar"}
# print(e)
# iterate through dict key-value pairs

# for key in e:
#     print(e[key])


# for key, val in e.items():
#     print(key, val)

# the `items` method on dicts is similar to the enumerate function
