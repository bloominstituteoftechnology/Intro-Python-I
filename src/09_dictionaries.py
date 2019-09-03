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
waypoints.append(dict([('lat', 54), ('lon', -154), ('name', '54th avenue')]))
print(waypoints[3])
# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
for x in waypoints:
    if x['name'] == "a place":
        x['lon'] = -130
        x['name'] = 'not a real place'
print(waypoints[0])
# Write a loop that prints out all the field values for all the waypoints
num = 1
for x in waypoints:
    print(f'location {num}')
    num += 1
    for y in x:
        print(f'{y}: ', x[y])
