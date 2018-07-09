# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 18,
        "lon": -234,
        "name": "Somewhere"
    },
    {
        "lat": 32,
        "lon": 324,
        "name": "End of the World"
    },
    {
        "lat": 435,
        "lon": -45,
        "name": "Happy Place"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for way in waypoints:
    print(way['name'], way['lat'], way['lon'])