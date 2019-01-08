#<<<<<<< master
# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.
=======
#"""
#Dictionaries are Python's implementation of associative arrays.
#There's not much different with Python's version compared to what
#you'll find in other languages (though you can also initialize and
#populate dictionaries using comprehensions just like you can with 
#lists!). 

#The docs can be found here:
#https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#For this exercise, you have a list of dictionaries. Each dictionary
#has the following keys:
# - lat: a signed integer representing a latitude value
# - lon: a signed integer representing a longitude value
# - name: a name string for this location
"""
#>>>>>>> master

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "Spain"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "Colombia"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "Mexico"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for item in waypoints:
    print(item.values())

# Add a new waypoint to the list
waypoints.append({
    "lat": 22,
    "lon": -181,
    "name": "Texas"
})

print(waypoints)
