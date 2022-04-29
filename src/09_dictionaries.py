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
print('Initial:')
"""print the intial dictionary"""
[print(n.values()) for n in waypoints]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({"lat": 45, "lon": -103, "name": "my place"})
print('\nNew waypoint added:')
"""print dictionary after first change to compare results"""
[print(n.values()) for n in waypoints]

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
for n in waypoints:
    """
    go throught each value of the elements
    and compare if the element is 'a place'
    and then change the values in the dictionary
    """
    if 'a place' in n.values():
        n['lon'] = -130
        n['name'] = 'not a real place'

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
"""print dictionary after second change to compare results"""
print('\nLoop & Modification:')
[print(n.values()) for n in waypoints]
