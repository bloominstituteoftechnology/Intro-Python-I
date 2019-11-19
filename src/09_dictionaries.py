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
waypoints.append({"lat": 12, "lon": 13, "name": "beach"})
print(waypoints)
# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
waypoints[0]["lon"] = -130
waypoints[0]["name"] = "not a real place"
print(waypoints)
print("")

# Write a loop that prints out all the field values for all the waypoints
for x in range(len(waypoints)):
    print("lat:" + str(waypoints[x]["lat"]))
    print("lon:" + str(waypoints[x]["lon"]))
    print("name:" + waypoints[x]["name"] + "\n")
