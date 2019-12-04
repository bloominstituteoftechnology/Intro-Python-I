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
 
 0

You have a dictionary within a list. 
You must first extract the dictionary from the list and then process the items in the dictionary.
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
#append takes only one arg; look into adding multiple args
# YOUR CODE HERE
waypoints.append({"lat": 44, "lon": -140, "name": "can you see me now"})
print('Can you see me',waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE
for w in waypoints:
    w.update((key, "not a real place") for key, value in w.items() if value == 'a place' )
    w.update((key, -130) for key, value in w.items() if value == -121)
    print(w)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE


for w in waypoints:
    for k, values in w.items():
        print(values)
        
        #k could also be written as keys 