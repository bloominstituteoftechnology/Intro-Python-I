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
# var myCar = new Object();
# myCar.make = 'Ford';
# myCar.model = 'Mustang';
# myCar.year = 1969;
my_place = {}
# my_place2 = dict()
my_place['lat'] = 55,
my_place['lon'] = 125,
my_place['name'] = 'my place'
new_waypoints = waypoints.__add__([my_place])
# new_waypoints2 = waypoints.append(my_place)
# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.
waypoints[0]['lon'] = -130
waypoints[0]['name'] = 'not a real place'
# YOUR CODE HERE

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for x in waypoints:
    print(x['lon'],x['lat'],x['name'])

for i in range(len(waypoints)):
    print(waypoints[i]['name'], waypoints[i]['lon'], waypoints[i]['lat'])