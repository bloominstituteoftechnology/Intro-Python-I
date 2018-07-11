# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 100.5018,
        "lon": 13.7563,
        "name": "Bangkok"
    },
    {
        "lat": 139.6917,
        "lon": 35.6895,
        "name": "Tokyo"
    },
    {
        "lat": 172.6362,
        "lon": 43.5321,
        "name": "Christchurch"
    }
]

# Write a loop that prints out all the field values for all the waypoints

for i in waypoints:
    print("latitude: {}, longitude: {}, name: {}".format(i["lat"], i["lon"], i["name"]))