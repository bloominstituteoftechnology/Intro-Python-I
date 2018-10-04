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

for x in waypoints:
    for y in x.values():
        print(y)


# Add a new waypoint to the list

new_waypoint = {
    "lat": 90,
    "lon": -1,
    "name": "a fourth place"
}

waypoints.append(new_waypoint)

for place in waypoints:
    for k, v in place.items():
        print('{}: {}'.format(k, v))
