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

# Add a new waypoint to the list
all_values = []
for waypoint in waypoints:
    print(f"===> {list(waypoint.values())}")
    for value in list(waypoint.values()):
        all_values.append(value)

print('all values ==>', all_values)


newWaypoint = {
    "lat": 47,
    "lon": -133,
    "name": "a firth place"
}

waypoints.append(newWaypoint)
print('new waypoints arr ==>', waypoints)
