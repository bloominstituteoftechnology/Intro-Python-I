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

 https://w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-20.php
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
    "lat": 42.59,
    "lon": -87.82,
    "name": "Kenosha"
})

print(waypoints)
# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
waypoints[0]['lon'] = -130
waypoints[0]['name'] = 'not a real place'

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for v in waypoints:
    print(str(v.values()))

u_value = set( val for dic in waypoints for val in dic.values())
print("Unique Values: ",u_value)

"""
Answer:
[{'lat': 43, 'lon': -121, 'name': 'a place'}, {'lat': 41, 'lon': -123, 'name': 'another place'}, {'lat': 43, 'lon': -122, 'name': 'a third place'}, {'lat': 42.59, 'lon': -87.82, 'name': 'Kenosha'}]
dict_values([43, -130, 'not a real place'])
dict_values([41, -123, 'another place'])
dict_values([43, -122, 'a third place'])
dict_values([42.59, -87.82, 'Kenosha'])
Unique Values:  {-123, -122, 'not a real place', 41, 42.59, 43, 'another place', -87.82, 'Kenosha', 'a third place', -130}
"""