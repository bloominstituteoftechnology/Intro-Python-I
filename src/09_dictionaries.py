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

# print(waypoints[0]["new_item"] = "blah")

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({'lat':44, 'lon':45, 'name':'a fourth place'})
print(waypoints[3])

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
# waypoints.insert(0,{'lat':43, 'lon':-130, 'name':'not a real place'})


""" updating a dictionary"""
# waypoints[0] = {'lat': 43, 'lon': -130, 'name': 'not a real place'}
# waypoints[0]['name'] = 'not a real place'
# waypoints[0]['lon'] = -130

""" swapping values in a dictionary  + assigning multiple values at a time via tuples """
(waypoints[0]['name'], waypoints[0]['lon']) = ('not a real place', -130)
# (x,y) = (y,x)
print(waypoints)


# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

# Printing out each latitude and longitude 
for points in waypoints:
    print(points['lat'], points['lon'])

# Printing out all the key:value pairs 
# for points in waypoints:
#     for k,v in points.items():
#         print(k,v)
