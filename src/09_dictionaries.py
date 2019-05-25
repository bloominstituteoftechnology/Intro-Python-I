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
waypoints.append({
    "lat": 88,
    "lon": -99,
    "name": "Bangkok"
})

print(waypoints)
print("access first dictionary:", waypoints[0]["lat"])

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE

waypoints[0]["lon"] = -130
waypoints[0]["name"] = "not a real place"
print("updated waypoints[0]", waypoints[0])

#alternative for updating multiple key-value pairs waypoints[0].update({"lon": -130, "name": "not a real place"})

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for value in waypoints[2].values():
    print("just value for waypoints[2]:", value)

for value in waypoints[1].values():
    print("just value for waypoints[1]:", value)

for value in waypoints[0].values():
    print("just value for waypoints[0]:", value)

for key in waypoints[0].keys():
    print("just keys for waypoints:", key)