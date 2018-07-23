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
for obj in waypoints:
    print("\n", obj.values())

# or

for obj in waypoints:
    for value in obj.values():
        print("\n", value)

# Add a new waypoint to the list

newWaypoint = {
    "lat": 99,
    "long": 0,
    "name": "a fourth place"
}

waypoints.append(newWaypoint)

print("\nWaypoints:\n", waypoints)
