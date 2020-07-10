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
tmpPt = {"lat": 39, "lon": -84, "name": "a fourth place"}
waypoints.append(tmpPt)
print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.
for i, doc in enumerate(waypoints):
    if doc['name'] == "a place":
        doc['lon'] = -130
        doc['name'] = "not a real place"

        waypoints[i] = doc

print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
for i, doc in enumerate(waypoints):
    print(f'Waypoint #{i} - name: {doc["name"]}, lat: {doc["lat"]}, lon: {doc["lon"]}')
