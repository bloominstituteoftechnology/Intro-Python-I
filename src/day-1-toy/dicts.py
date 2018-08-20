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


# Add a new waypoint to the list
waypoints.append({"lat":41.05857, "lon":-74.75319, "name":"Newton"})

# Write a loop that prints out all the field values for all the waypoints
for w in waypoints:
    print(w['name'], w['lat'], w['lon'])
