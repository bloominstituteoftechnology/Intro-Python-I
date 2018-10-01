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
        "lat": 23,
        "lon": 22,
        "name": "a fourth place"
    },
    {
        "lat": 121,
        "lon": -121,
        "name": "a fifth place"
    },
    {
        "lat": 101,
        "lon": -101,
        "name": "a sixth place"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for place in waypoints:
    print(place.items())

# Add a new waypoint to the list
waypoints.append({
    "lat": 19,
    "lon": 21,
    "name": 'a seventh place'
})
