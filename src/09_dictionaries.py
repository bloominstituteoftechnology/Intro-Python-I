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
waypoints.append({"lat": 50, "lon": -125, "name": "place again"})
print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# for d in my_dicts:
#     d.update((k, "value3") for k, v in d.items() if v == "value2")

# YOUR CODE HERE
waypoints[0] = {"lat": 43, "lon": -130, "name": "not a real place"}
print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
# for index in range(len(waypoints)):
#     for value in waypoints[index]:
#         print(waypoints[index][value]) how does it know that value is supposed to be the value and not the key?  
                                        # Why is it printed with [index]

for points in waypoints:
    for val in points.values():
        print(val)        