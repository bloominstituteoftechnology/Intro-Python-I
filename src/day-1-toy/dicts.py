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
        "lon": -119,
        "name": "a third place"
    },
    {
        "lat": 45,
        "lon": -120,
        "name": "a third place"
    },
    {
        "lat": 46,
        "lon": -121,
        "name": "a third place"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for place in waypoints:
    print(place.items())


# Add a new waypoint to the list

waypoints.append({
    "lat": 10,
    "lon": -12,
    "name": "added place"
})
