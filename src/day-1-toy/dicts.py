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
        "lon": 100,
        "name":"my place"
    },
        {
        "lat": 12,
        "lon": 11,
        "name":"my place2"
    },
        {
        "lat": 45,
        "lon": 122,
        "name":"my place3"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for point in waypoints:
    print(point)
# Add a new waypoint to the list
waypoints.append({"lat": 12, "lon":11, "name": "new place1"})