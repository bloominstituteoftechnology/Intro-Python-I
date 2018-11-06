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
        "lat": 44,
        "lon": -135,
        "name": "a fourth place"
    }

]

# Write a loop that prints out all the field values for all the waypoints
for k, v in waypoints.items():
    print("Code : {0}, Value : {1}".format(k, v))
# Add a new waypoint to the list
