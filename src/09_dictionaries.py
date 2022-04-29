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

import pprint
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
print("-----" * 5)
pprint.pprint(waypoints)
print("-----" * 5)

# Add a new waypoint to the list
# YOUR CODE HERE

waypoints.append(
    {
        "lat": 25,
        "lon": -150,
        "name": "a fourth place"
    }
)

pprint.pprint(waypoints)
print("-----" * 5)


# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
waypoints[0]["lon"] = -130
waypoints[0]["name"] = "not a real place"

pprint.pprint(waypoints)
print("-----" * 5)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for d in waypoints:
    lat = d['lat']
    lon = d['lon']
    name = d['name']
    print(f"{name} has {lat} latitue and {lon} longitude")
print("-----" * 5)
