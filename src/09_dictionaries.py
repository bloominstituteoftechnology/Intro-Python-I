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
waypoints.append(
    {
        "lat": 40.4, 
        "lon": 112, 
        "name": "a fourth place"
    }
)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# One option to update is: 
# for item in waypoints:
#     item.update((k, "not a real place") for k, v in item.items() if v == "a place")
#     item.update((k, 130) for k, v in item.items() if v == -121)

# Another more direct option is: 
waypoints[0]['lon'] = 130
waypoints[0]['name'] = "not a real place"

# Write a loop that prints out all the field values for all the waypoints
for index in range(len(waypoints)):
    print(f'--- Waypoint {index + 1} ---')
    for key, value in waypoints[index].items():
        print(f'{key}: {value}')
    print('\n')