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
waypoints.append({"lat": 53, "lon": -125, "name": "north carolina"})

# Modify the dictionary with name "a place" such that its longitude
waypoints[0] = [{"longitude": "a place"}]

# print(waypoints)
# value is -130 and change its name to "not a real place"
waypoints[0] = [{"not a real place": -130}]
print(waypoints)

# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

# for lat, lon, name in waypoints:
#     print("Lattitude and Longitude are %s, %s and the name of this place is %s" %(lat, lon, name))
    

for dic in waypoints:
    print(dic)
    # for key in dic:
    #     print(dic[key])

print(waypoints)