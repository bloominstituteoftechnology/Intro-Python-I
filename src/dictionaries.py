"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictinaries. Each dictionary
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
waypoints.insert(len(waypoints), {
    "lat": 93.2650,
    "lon": 44.9778,
    "name": "Minneapolis, MN"
})

print(waypoints)
# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE

#function():
#input(w,x)
#
if any(d["name"] == 'a place' for d in waypoints):
    match = next((l for l in waypoints if l["name"] == "a place"), None)
    print(match)
    print(waypoints[waypoints.index(match)])
    #input(y,z)
    waypoints[waypoints.index(match)].update({"lon": -130})
    waypoints[waypoints.index(match)].update({"name": "not a real place"})
    # waypoints[waypoints.index(match)]["not a real place"] = waypoints[waypoints.index(match)].pop("a place")
    print(waypoints[waypoints.index(match)])
# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
#peer code review Daniel Ferrer
for i in waypoints:
    print(i.values())
