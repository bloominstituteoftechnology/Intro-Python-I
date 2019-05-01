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
newWaypoint = {
        "lat": 45,
        "lon": -95,
        "name": "a fourth place"
    }
waypoints.append(newWaypoint)

print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"

def update_Dict(n):
    """update values"""
    n['name'] = "not a real place"
    n['lon'] = -130
    
    return n

[update_Dict(n) for n in waypoints if n['name'] == "a place"]

# Write a loop that prints out all the field values for all the waypoints
[[print(v) for k,v in n.items()] for n in waypoints]