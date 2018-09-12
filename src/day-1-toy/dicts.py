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

# Write a loop that prints out all the field values for all the waypoints
for entry in waypoints:
    print("Latitude: " + str(entry['lat']))
    print("Longitude: " + str(entry['lon']) + "\n")


# Add a new waypoint to the list
waypoints.append({'lat': 12, 'lon': 15, 'name': 'a fourth place'})
print(waypoints)
