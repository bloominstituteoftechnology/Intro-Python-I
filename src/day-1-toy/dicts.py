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
        "lat": 33,
        "lon": -121,
        "name": "a fourth"
    }, 
    {
        "lat": 31,
        "lon": -123,
        "name": "fifth place"
    }, 
    {
        "lat": 32,
        "lon": -122,
        "name": "sixth place"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for point in waypoints:
    f"Latitude: {point['lat']}"
    f"Longitude: {point['lon']}"
    f"Name: {point['name']}"

# Add a new waypoint to the list

waypoints.append({
    "lat": "23",
    "lon": "32",
    "name": "seventh place"
})

waypoints