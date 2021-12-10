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
waypoints.append({"lat": 0, "lon": 0, "name": "null island"})

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

waypoints = [ {"lat": w["lat"], "lon" : -130, "name" : "not a real place"} if w["name"] == "a place" else w for w in waypoints ]

# Write a loop that prints out all the field values for all the waypoints

# No; it's bad practice to write a loop when subsequent calls don't depend on an updated state. It's less efficient, harder to read, harder to reason about, and longer to write a loop in such cases. I won't stupe to the level of these instructions.
[ print( "lat:", w["lat"], " lon:", w["lat"], " name:", w["name"] ) for w in waypoints ]
