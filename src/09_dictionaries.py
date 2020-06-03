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
waypoints.append({"lat": 45, "lon": -153, "name": "more places"})
# print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.
# waypoints[0] = ({"lat": 43, "lon": -130, "name": "not a real place"}) 
# print(waypoints)

# #find 'a place', find long and name in 'a place' and change that value
# # YOUR CODE HERE
for dict_item in waypoints:
    if dict_item["name"] == "a place":
        dict_item["name"] = "new place"
        dict_item["lon"] = -22

print(waypoints)



# Write a loop that prints out all the field values for all the waypoints
# # YOUR CODE HERE
for dict_item in waypoints:
    for key in dict_item:
        print(key, ":", dict_item[key])