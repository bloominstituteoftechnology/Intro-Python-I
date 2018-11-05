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
        "lat": 69,
        "lon": 69,
        "name": "69 town"
    },
    {
        "lat": 1111,
        "lon": 2222,
        "name": "3333 town"
    }
]

# Write a loop that prints out all the field values for all the waypoints

for location in waypoints:
    print(location)

# Add a new way point to the list

waypoints.append({"lat": 777, "lon": 777, "name": "luck town"})
