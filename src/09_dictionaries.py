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
waypoints.append({
    "lat": 40,
    "lon": 40,
    "name": "a fourth place"
})

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.
for index in range(len(waypoints)):
    if waypoints[index]["name"] == "a place":
        waypoints[index]["lon"] = -130
        waypoints[index]["name"] = "not a real place"

# Write a loop that prints out all the field values for all the waypoints
print('WAYPOINTS:')
for waypoint in waypoints:
    # (lat, lon, name) = [value for key, value in waypoint.items()]
    print(f'{waypoint["name"]:>20s}: ({waypoint["lat"]}, {waypoint["lon"]})')

# STRETCH: List all key/value pairs for each dictionary in the list
for index in range(len(waypoints)):
    print(f'@ waypoints[{index}]:')
    for key, value in waypoints[index].items():
        if isinstance(value, int):
            print(f'    "{key}" : {value},')
        else:
            print(f'    "{key}" : "{value}",')
