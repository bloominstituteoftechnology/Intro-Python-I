# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

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

# Write a loop that prints out all the field values for all the waypoints
for index in range(len(waypoints)):
    for key in waypoints[index]:
        print(key)

# Add a new waypoint to the list
newWay = {
    "lat": 47,
    "lon": -47,
    "name": "a fourth place"
}

waypoints.append(newWay)

print(waypoints)