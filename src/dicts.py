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
    },
    {
        "lat": 42,
        "lon": -124,
        "name": "booga"
    },
    {
        "lat": 53,
        "lon": -110,
        "name": "balooga"
    },
    {
        "lat": 40,
        "lon": -140,
        "name": "whale"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for dict in waypoints:
    for key in dict:
        print('{}: {}'.format(key, dict[key]))
# Add a new waypoint to the list
waypoints.append({
    "lat": 45,
    "lon": -112,
    "name": "fake"
})
