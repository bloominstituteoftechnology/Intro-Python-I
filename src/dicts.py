# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [{
    "lat": 4.7902,
    "lon": 1.2220,
    "name": "nowhere1"
},{
    "lat": 5.7902,
    "lon": 1.2220,
    "name": "nowhere2"
},{
    "lat": 6.7902,
    "lon": 1.2220,
    "name": "nowhere3"
}
]

# Write a loop that prints out all the field values for all the waypoints
for a in waypoints:
    print(a["lat"], a["lon"], a["name"])