# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 23,
        "lon": -121,
        "name": "1st place"
    }, 
    {
        "lat": 21,
        "lon": -123,
        "name": "2nd place"
    }, 
    {
        "lat": 23,
        "lon": -122,
        "name": "3rd place"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for v in waypoints:
    values = v.values()
    print(values)
# Add a new waypoint to the list
# ?
waypoints.update({"lat": 44, "lon": 24, "name": "Forth"})
waypoints
